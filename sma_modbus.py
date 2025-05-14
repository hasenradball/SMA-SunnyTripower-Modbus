"""Script for connect to the SMA SunnyTripower inverter"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sma_modbus import SunnyTripower as sunny_tripower

# Main
if __name__ == "__main__":
    tic = time.perf_counter()
    sunny_obj = sunny_tripower("192.168.178.33")
    sunny_obj.connect()
    print("SMA Sunny Tripower Test\n")
    print(f'Device unit ID  : {sunny_obj.read_device_unit_id()}')
    print(f'Device class    : {sunny_obj.get_device_class()}')
    print(f'Serial Number   : {sunny_obj.get_serial_number()}')
    print(f'Software Packet : {sunny_obj.get_software_packet()}')
    print(f'Device Type     : {sunny_obj.get_device_type()}')
    print("\n")
    print(f'Status of Device : {sunny_obj.get_status_of_device()}')
    print(f'Grid Relay state : {sunny_obj.get_grid_relay_status()}')
    print ("\n")
    print(f'Total yield     : {sunny_obj.get_total_yield_Wh()} Wh')
    print(f'Total yield     : {sunny_obj.get_total_yield_kWh()} kWh')
    print(f'Total yield     : {sunny_obj.get_total_yield_MWh()} MWh')
    print(f'Daily yield     : {sunny_obj.get_daily_yield()} Wh')
    print(f'Operating mode  : {sunny_obj.get_operating_mode()}')
    print(f'Locking state   : {sunny_obj.get_locking_state()}')
    print ("\n")
    print(f'DC Current In : {sunny_obj.get_dc_current_in()} A')
    print(f'DC Voltage In : {sunny_obj.get_dc_voltage_in()} V')
    print(f'DC Power In   : {sunny_obj.get_dc_power_in()} W')
    print ("\n")
    print(f'Active Power  : {sunny_obj.get_active_power()} kW')
    print(f'AC Current    : {sunny_obj.get_ac_current()} A')
    sunny_obj.close()
    toc = time.perf_counter()
    print(f'\nINFO: test finished in {toc-tic:.3f} s')

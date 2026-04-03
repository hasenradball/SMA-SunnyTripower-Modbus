"""Script reading data from SMA SunnyBoy and send to mariaDB"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
from sma_modbus import SunnyTripower as sunny_tripower
from mariadb_config import MARIA_DB_CONFIG
from maria_db_mysql import MariaDBMysql as maria_db

# Main
if __name__ == "__main__":
   sunny_obj = sunny_tripower("192.168.178.29")
   power_total = sunny_obj.get_active_power()[0]
   i1_ac = sunny_obj.get_ac_current()[0]
   # Leistung Verbraucher
   p_load = sunny_obj.get_actual_power_of_load()
   # Leistung Netzbezug
   p_grid_in = sunny_obj.get_actual_power_of_grid_import()
   # Leistung Netzeinspeisung
   p_grid_out = sunny_obj.get_actual_power_of_grid_export()
   # Leistung PV Erzeugung
   p_pv_prod = sunny_obj.get_actual_power_of_pv_production()
   # Leistung Eigenverbrauch
   p_own_usage = sunny_obj.get_actual_power_of_internal_consumtion() 

   maria_obj = maria_db(MARIA_DB_CONFIG)
   maria_obj.insert_by_sql_insert_stmt("leistung", ("`p_act_sum`"), (power_total))
   maria_obj.insert_by_sql_insert_stmt("strom", ("`i_ac_l1`"), (i1_ac))

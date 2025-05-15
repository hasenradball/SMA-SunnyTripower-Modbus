# SMA-Sunny-Tripower-SE-Modbus
Python solution connecting the SMA SunnyTripower SE inverters.

![SMA-SunnyBoy](./docs/SMA/SMA-Sunny_Tripower_SE.jpg)

## Contents
* [Prerecquisites](#prerecquisites)
* [Installation Steps](#installation-steps)
* [Library Installation](#library-installation)
* [Library Usage](#library-usage)
* [License](#license)
* [Helpful Links](#helpful-links)

## Prerecquisites
1. For this library you need python3
2. For the use of this python code it is necessary to install the python libs:
    - `pymodbus v3.9.2`
    - `pyserial`
> Remark: for `pymodbus` use the minimum version of 3.9.x, testetd with pymodbus==3.9.2

## Installation steps
### Make python ready to use
1) Create a python3 virtual environment in your home folder, see:<br>
[https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

```
python -m venv ~/my_python_venvs
```
2. Install the needed python packages

> the pymodbus Documentation you will find here:<br>
[https://pymodbus.readthedocs.io/en/v3.9.2/](https://pymodbus.readthedocs.io/en/v3.9.2/)

```
~/my_python_venvs/bin/python -m pip install pymodbus==3.9.2
~/my_python_venvs/bin/python -m pip install pyserial
```
You can check the state by:

```
~/my_python_venvs/bin/python -m pip list
```



 ### Make your SMA Inverter ready to use
1. make sure that your SMA Device supports the modbus protocol
2. make sure that the SMA Device has started/enabled the TCP Server to communicate via modbus

## Library Installation
Install the library from github.<br>
Lets assume you want to install it in the following path: `~/git_repos`

```
cd ~
mkdir git_repos
cd git_repos
git clone https://github.com/hasenradball/SMA-SunnyTripower-Modbus.git
```
## Library Usage

Check the python code in the script `sma_modbus.py` and change the settings if necessary.<br>
Especially the `ip-address` has to be adapted to your settings in the following line:

```
sunny_obj = sunny_tripower("192.168.xxx.xxx", UnitID)
```
The device UnitID has the value `3` as default. If you are not sure you can use the function `read_device_unit_id()` to check.<br>
The UnitID can be set to values of `3...123`, the values `1` and `2` are reserved.<br>

Thus the constructor has a default parameter for the UnitID = 3, the instanciation can also be done like:
```
sunny_obj = sunny_tripower("192.168.xxx.xxx")
```
### Check the UnitID
```
sunny_obj = sunny_tripower("192.168.xxx.xxx")
print(sunny_obj.read_device_unit_id())
```

### Check the Communication
After updated the ip and the UnitID if necessary you can check the communication.


```
cd /path/to/your/installation/folder

~/my_python_venvs/bin/python sma_modbus.py
```

The result could look like this example:

```
SMA Sunny Tripower Test

Device unit ID  : 3
Device class    : Hybrid-Wechselrichter
Serial Number   : xxxxxxxx
Software Packet : 50665988
Device Type     : SUNNY TRIPOWER 6.0 SE (STP6.0-3SE-40)


Status of Device : Ok
Grid Relay state : closed


Total yield     : 92710 Wh
Total yield     : 93 kWh
Total yield     : 0 MWh
Daily yield     : 7928 Wh
Operating mode  : Netzparallelbetrieb (GriOp)
Locking state   : Information liegt nicht vor (NaNStt)


DC Current In : (6.158, 6.795, 0.0, 0.0) A
DC Voltage In : (439.2, 157.3) V
DC Power In   : (2705, 1069) W


Active Power  : (3.706, 1.234, 1.232, 1.239) kW
AC Current    : (5.116, 5.105, 5.102) A

INFO: test finished in 0.419 s

```
That's it!


# License
This library is licensed under MIT Licence.

# Helpful Links
* [ESP8266-01-Adapter](https://esp8266-01-adapter.de)

# Thinkpad Fan Control GUI

![Screenshot](https://i.imgur.com/OefITyn.png)

This is an application for controlling fan speed on IBM/Lenovo ThinkPads on Linux. Based on the script by Dev Aggarwal.

It can also monitor CPU temp and fan RPM. 

## Supported Devices
Tested on
```
ThinkPad x280 (working)
ThinkPad T480s (working)
```

## How it Works?
 + Parses `sensors` command to show CPU temp and fan RPM
 + Modifies `/proc/acpi/ibm/fan` to change fan speed

## Dependencies
`sudo apt install lm-sensors python3 python3-tk`

## Setup
+ Open this file, using command -- `sudo nano /etc/modprobe.d/thinkpad_acpi.conf` 
+ Add line `options thinkpad_acpi fan_control=1`
+ Reboot. 
+ `python3 gui.py`


---

Note: You are required to have the Linux kernel with `thinkpad-acpi` patch. (Ubuntu, Solus and a few others already seem to have this)

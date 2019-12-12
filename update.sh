#!/bin/bash

# esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART erase_flash
# esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART --baud 460800 write_flash -z 0x1000 libs/micropython/esp32-idf3-20191210-v1.11-633-gb310930db.bin

echo "Upload: robot.py"
ampy -p /dev/cu.SLAB_USBtoUART put robot.py
echo "Upload: motor_dc.py"
ampy -p /dev/cu.SLAB_USBtoUART put motor_dc.py
echo "Upload: boot.py"
ampy -p /dev/cu.SLAB_USBtoUART put boot.py
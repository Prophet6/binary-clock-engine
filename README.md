# Commands sent to the pi for setup:

* [placed "wpa_supplicant.conf" file at root of the SD card] - allows wifi connection
* [placed an empty file named "SSH" at root of the SD card] - allows SSH connection

sudo apt-get update

sudo apt install python3-gpiozero

## Optional commands:

sudo apt install emacs # not necessary

Transfering to the Pi from a remote pc with python installed, such as PowerShell:

scp Binary_Clock_v1.py pi@raspberrypi.local:testing/

## Other Info:

date: 1001101000110010011101001 or 11111100101.1001.10101

time: 1000011110 or 0.101.101010


25 or 22 (including 2 decimal points)
10 or 12 (including 2 decimal points)



Decimal date:     20210921
True binary date: 1001101000110010011101001
Mock binary date: 011111100101 1001 10101  

Decimal time:     170202
True binary time: 101001100011011010       
Mock binary time: 10001 000010 000010      

tbd = 25
mbd = 21
tbt = 18
mbt = 17
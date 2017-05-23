sensortag
=========

-  Make sure the sensor is on (i.e., the green led blinks, if not press
   the on/off button) and run: ``sudo hcitool lescan`` This command scan
   for bluetooth devices and you should see on line something like:
   B0:B4:48:BE:CC:06 CC2650 SensorTag, the address might be different
   depending on the sensor
-  copy this address
-  run ``rosrun sensortag sensortagRead.py COPIED_ADDRESS``



Original page: https://github.com/strands-project/sensortag/blob/master/README.md
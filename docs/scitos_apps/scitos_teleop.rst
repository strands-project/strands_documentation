Scitos Teleop
-------------

The scitos\_teleop package is designed to work with a Logitech Wireless
Gamepad F710.

Install udev rule for gamepad
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To copy the udev rule to ``/etc/udev/rules`` run

::

    rosrun scitos_teleop create_udev_rules

this will make the jaoypad availabe as ``/dev/input/rumblepad``

Running and using the teleop node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Source the corresponding setup.bash:
   ``source <your_catkin_workspace>/devel/setup.bash``
-  Launch the rumblepad control:
   ``roslaunch scitos_teleop teleop_joystick.launch``
-  If the simulator or scitos\_node is running, you should now be able
   to control the robot using the joypad.
-  Please also have look at:
   https://github.com/strands-project/scitos\_apps/tree/master/scitos\_cmd\_vel\_mux
   which represents a nice way of giving the joystick priority over the
   navigation stack.
-  Controlling the robot (if you do not press any buttons, the rumbelpad
   control will not interfere with any autonomous behaviour but can be
   used to emergency stop the robot or reset the bumper after a crash):
   You can find a cheat sheet in the doc directory of scitos\_teleop.
-  Dead-Man-Switch: top left shoulder button, keep pressed to move robot
   or head.
-  Moving the robot: move the robot with the left joystick or D-Pad
   (toggel between those with the "Mode" button).
-  Emergency stop: lower left sholder button. Has to be pressed down
   completely. Be aware that the gamepad is turning itself off after a
   certain time and that this button does not turn it on automatically.
   You have to press one of the other buttons in order to turn it back
   on.
-  Freerun: "Back" button on the pad. (Move robot around manually)
-  Reset/Re-enable motors: "Start" button on the pad. (Use after
   emergency stop or bumper crash)
-  Move the head including eyes: use right joystick.
-  Move head to zero position: top right shoulder button.
-  Turn head 180 degrees: Y button.
-  Move eye lids: use lower right shoulder button.

Troubleshooting
~~~~~~~~~~~~~~~

If you get a message like:
``[ERROR] [1372933726.815471480]: Couldn't open joystick /dev/.... Will retry every second.``
you can export the joystick device, e.g.:
``export JOYSTICK_DEVICE=/dev/input/js1`` and start the launch file
again. If you installed the udev rule as mentioned above this should not
happen. Try to follow the instruction for installing the udev rule
again.


Original page: https://github.com/strands-project/scitos_apps/blob/hydro-devel/scitos_teleop/README.md
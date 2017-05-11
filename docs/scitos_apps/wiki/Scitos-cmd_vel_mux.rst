Installation
~~~~~~~~~~~~

-  Run ``catkin_make``
-  Source the environment
-  Run rosdep

   ::

       rosdep install scitos_cmd_vel_mux

Usage
~~~~~

-  Run

   ::

       roslaunch scitos_cmd_vel_mux mux.launch

-  Remap your navigation stack /cmd\_vel output to
   /cmd\_vel\_mux/input/navigation
-  Run

   ::

       roslaunch scitos_teleop_mux.launch

   This runs the scitos\_teleop and remaps the joystick output to
   /cmd\_vel\_mux/input/joystick. Now the joystick will always have
   priority as soon as you press the dead-man-switch.

Inputs
~~~~~~

Sorted by priority of incoming commands (high to low): \*
/cmd\_vel\_mux/input/joystick: For teleoperation \*
/cmd\_vel\_mux/input/webapp: For teleoperation over the browser \*
/cmd\_vel\_mux/input/navigation: For the navigation stack \*
/cmd\_vel\_mux/input/default: For everything that is not aware of the
arbitration

To add input topics or change priorities modify: param/mux.yaml

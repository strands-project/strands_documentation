scitos\_cmd\_vel\_mux
---------------------

This package provides a launch and parameter file that is tailored to a
scitos A5 robot using the navigation stack and a teleoperation node like
``scitos_teleop``.

Installation
~~~~~~~~~~~~

-  Run ``catkin_make``
-  Run dependencies are installed via rosdep.

Usage
~~~~~

-  Run

   ::

       roslaunch scitos_cmd_vel_mux mux.launch

-  Remap your navigation stack ``/cmd_vel`` output to
   ``/cmd_vel_mux/input/navigation``
-  Run

   ::

       roslaunch scitos_teleop_mux.launch

   This remaps the joystick output to ``/cmd_vel_mux/input/joystick``
   and now the joystick will always have priority as soon as you press
   the dead-man-switch. Or you can run any other teleoperation node and
   do the remapping yourself.




Original page: https://github.com/strands-project/scitos_apps/blob/hydro-devel/scitos_cmd_vel_mux/README.md
Set-up
~~~~~~

This is just a simple example set-up and might differ from yours. If you
are familiar with ROS and/or using one of the set-up files from
strands\_systems you can skip this part. \* Create a ros workspace:
``mkdir -p ros-ws/src && cd ros-ws/src`` \* Clone the github repository:
``git clone https://github.com/strands-project/scitos_apps.git`` \*
Setting up the catkin workspace: in ros-ws/src run
``catkin_init_workspace`` \* Change to the root directory of the
repository which is ros-ws in our case. \* Make sure that scitos\_apps
is in the same workspace as scitos\_common or is overlaying the
scitos\_common workspace to enable the emergency stop for the robot. \*
Run ``catkin_make`` in ros-ws (catkin\_make builds all binary files and
creates environment variables like the setup.bash) Now everything should
be built and you go to the next part which describes the usage of the
scitos\_teleop package.

Usage:
~~~~~~

Launch files: \* Source the environment variables
``source devel/setup.bash`` \* Run one of the following launch files: \*
teleop\_joystick\_core.launch: This launches the core functionalities of
the rumblepad: emergency stop, motor reset, freerun and the action
button topic is published. \*
teleop\_joystick\_just\_[base/head].launch: This launches
teleop\_joystick\_core.launch and the control for the head or base
depending on the file you choose. \* teleop\_joystick.launch: This
launches all the functionalities of the rumblepad and gives you fulkl
control. \* teleop\_joystick\_mux.launch: This launches all the
functionalities of the rumblepad and relies on the scitos\_cmd\_vel\_mux
(see [[Scitos-cmd\_vel\_mux]]).

Buttons: See `Cheat
Sheet <https://github.com/strands-project/scitos_apps/blob/master/scitos_teleop/doc/joypad-cheat-sheet.jpg>`__


Original page: https://github.com/strands-project/scitos_apps/wiki/Scitos-teleop
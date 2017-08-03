Getting the source code
=======================

If you want to get source code of all released packages from strands_desktop, you can use ``rosinstall_generator`` to generate a rosinstall file which is added/merged to a catkin ws using ``wstool`` http://wiki.ros.org/wstool 
 
.. code:: sh

    ROSDISTRO_INDEX_URL=https://raw.github.com/strands-project/rosdistro/strands-devel/index.yaml rosinstall_generator      strands_desktop --rosdistro indigo --deps --upstream --exclude-path ~/code/ros-install-osx/indigo_desktop_full_ws/src/ > ~/strands_ws/strands_desktop.rosinstall
    
**Note that you need to change paths in this example to fit yours.**
 
This creates an installation file for wstool. In this case the ``--exclude-path`` is used to ignore packages you already have (e.g. the ones produced by the main ROS installation) and ``--upstream gives`` you git repos where the selected branch is the tagged release, i.e. the most recently released branch. 
 
Setting up a robot from scratch
===============================

Get the code
------------
*TODO* link this to appropriate tutorial

You have several options how to obtain STRANDS system:

- you can install it via Ubuntu packages
- you can obtain all source code
- you can clone only the repositories which you are interested in 

I. Basic STRANDS system running on ROS Indigo and Ubuntu Trusty
-------------------------------------------------------------

a) Code
~~~~~~~~

For this step, you need:

- https://github.com/strands-project/strands_systems.git branch:indigo_devel 

  * This repository contains the most important launch files which you will need to get the basic system running
  
- https://github.com/strands-project/mongodb_store.git **branch:hydro_devel** (you need to change)

  * The robot stores a huge variety of its data into MongoDB

If you are using SCITOS robot, you can also use:

- https://github.com/strands-project/scitos_drivers  branch:indigo_devel

  * This repository contains Scitos G5 drivers that interface ROS to MIRA 
  
- https://github.com/strands-project/scitos_common.git branch:indigo_devel

  * This package contains robot-specific definitions of the SCITOS robot such as the URDF description of the robot's kinematics and dynamics and 3D models of robot components.
  
- https://github.com/strands-project/scitos_apps.git branch:hydro_devel

  * This repository contains docking, teleoperation and other useful applications which are dependent on the used robot
  
If you are using another robot, you will need to provide functionality covered by the three aforementioned repositories. 

b) Changes
~~~~~~~~~~~

Even if you use SCITOS robot, your exact configuration of the robot will differ. Therefore, you must change ``scitos.xacro`` and ``scitos_calibration.xacro`` in ``scitos_common/scitos_description/urdf/`` to fit your robot. 

**Chest camera for improved navigation**

Our robot is equipped with a depth camera on its chest in order to detect objects in front of the robot and improve its navigation. Its position and angle are important for the correct functioning of the navigation. You could put the chest camera calibration into the scitos.xacro. However, we experienced that the chest camera is the first thing to be "attacked" by kids during demos or by people during transfering the robot.  Therefore, we **do not** have the chest camera specified in the ``scitos_common/scitos_description`` but in ``strands_movebase/strands_description`` in order to load its position from calibration data database. Details about this calibration are provided later in this tutorial. 

c) Compiling
~~~~~~~~~~~~

If you are using SCITOS robot, your ```~/.bashrc``` file should look something like: 

.. code:: sh

 source /opt/ros/indigo/setup.bash
 source /localhome/strands/strands_ws/devel/setup.bash
 export MIRA_PATH="/opt/MIRA:/opt/SCITOS:/opt/MIRA-commercial:/localhome/strands/strands_ws/src"
 
When you compile aforementioned code, it will probably complain about version of MIRA. In that case, you can change the version version from 0.23.1 to 0.29 (or your version) in scitos_drivers/scitos_mira/CMakeLists.txt line 88

If you have SCITOS robot very similar to STRANDS robots, the rest should compile without issues. 

d) Running
~~~~~~~~~~

First, create a folder `mongodb_store` when mongo database will be saving data. This folder can be anywhere, but you must guarantee that the user running the system has writing access to this folder. 





To test, if everything works fine, you need to modify two launch files in ``strands_system/strands_bringup``:

* ``strands_robot.launch`` (especially if you are using a different robot or sensors) See different parameters of the launch file. 
* ``strands_cameras.launch`` (in order to launch cameras on the robot, we use separate launch file). We use two Asus Xtion cameras, one on a pan-tilt unit on top of the robot, one as a chest camera as explained above. In our setting, the chest camera is plugged into a main control pc, where navigation should run. In contrast, head camera is plugged into additional pc with a good graphic card with GPUs. If your setting is similar, you need provide this launch file with head_ip and chest_ip paramaters and with head_camera and chest_camera boolean flags to enable/diable them.

Then, run:

.. code:: sh

  roscore
  roslaunch --wait strands_bringup strands_robot.launch
  roslaunch strands_bringup strands_cameras.launch head_camera:=true head_ip:=(specify)
  rosrun rviz rviz
  
If you display the robot model in rviz, it will not look correct. This is due to the fact that is mising ``/map`` frame. Hence, run, for example, ``rosrun gmapping slam_gmapping`` to get the frame. 

To check: 

* your robot model and TF, if all transformation look correct. 
* the data publish by laser scanner (if you have any), cameras rgb pictures and registred point clouds
* move the robot by joystick if you have any. If you use Logitech gamepad as we do and you are using our code, you need to keep pressed button LB while moving the robot. 

If everything looks good, you are ready for the next step!
  
.. include:: mapping.rst











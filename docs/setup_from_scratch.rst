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

Basic STRANDS system running on ROS INDIGO with Ubuntu Trusty
-------------------------------------------------------------
For this, you need:

- https://github.com/strands-project/strands_systems.git branch:indigo_devel 

  * This repository contains the most important launch files which you will need to get the basic system running
  
- https://github.com/strands-project/mongodb_store.git **branch:hydro_devel** (need to change)

  * The robot stores a huge variety of its data into MongoDb

If you are using SCITOS robot, you can also use:

- https://github.com/strands-project/scitos_drivers  branch:indigo_devel
- https://github.com/strands-project/scitos_common.git branch:indigo_devel
- https://github.com/strands-project/scitos_apps.git branch:hydro_devel




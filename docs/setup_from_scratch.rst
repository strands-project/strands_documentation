TODO: move this code setting somewhere else
=====
Getting the source code
=====

If you want to get all release packages from strands_desktop as source code, you can do it by using``rosinstall_generator`` to generate a rosinstall file which is added/merged to a catkin ws using ``wstool``: 
http://wiki.ros.org/wstool 

 **Note that you need to change address in this example to fit yours.**
 ``ROSDISTRO_INDEX_URL=https://raw.github.com/strands-project/rosdistro/strands-devel/index.yaml rosinstall_generator strands_desktop --rosdistro indigo --deps --upstream --exclude-path ~/code/ros-install-osx/indigo_desktop_full_ws/src/ > ~/strands_ws/strands_desktop.rosinstall``
 
 This creates an installation file for wstool. In this case the ``--exclude-path`` is used to ignore packages you already have (e.g. the ones produced by the main ROS installation) and ``--upstream gives`` you git repos where the selected branch is the tagged release, i.e. the most recently released branch. 
 

=====
Setting a robot from scratch on ROS INDIGO with Ubuntu Trusty
=====

Get the code
--------
You have several options how to obtain STRANDS system:
- you can install it via Ubuntu packages
- you can obtain all source code
- you can clone only the repositories which you are interested in 

Basic STRANDS system running
--------
For this, you need:
- https://github.com/strands-project/scitos_drivers  branch:indigo_devel
- https://github.com/strands-project/scitos_common.git branch:indigo_devel
- https://github.com/strands-project/strands_systems.git branch:indigo_devel
- https://github.com/strands-project/scitos_apps.git branch:hydro_devel
- https://github.com/strands-project/mongodb_store.git branch:hydro_devel!!! (need to change)


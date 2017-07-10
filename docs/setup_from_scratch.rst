TODO: move this code setting somewhere else
=====
Getting the source code
=====

 ``ROSDISTRO_INDEX_URL=https://raw.github.com/strands-project/rosdistro/strands-devel/index.yaml rosinstall_generator strands_desktop --rosdistro indigo --deps --upstream --exclude-path ~/code/ros-install-osx/indigo_desktop_full_ws/src/``

In this case the ``--exclude-path`` is used to ignore packages you already have (e.g. the ones produced by the main ROS installation) and ``--upstream gives`` you git repos where the selected branch is the tagged release, i.e. the most recently released branch. 

The workflow is to use ``rosinstall_generator`` to generate a rosinstall file which is added/merged to a catkin ws using rosws: 
http://wiki.ros.org/wstool







=====
Setting a robot from scratch
=====

Get the code
--------
You have several options how to obtain STRANDS system:
- you can install it via Ubuntu packages
- you can obtain all source code
- you can clone only the repositories which you are interested in 

Basic STRANDS system running
--------


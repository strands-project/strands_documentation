1. Some Previous Steps
----------------------

1. Enable the LCAS package repositories:
2. Add the LCAS public key to verify packages:

   ``curl -s http://lcas.lincoln.ac.uk/repos/public.key | sudo apt-key add -``
3. Add the LCAS repository:

   ``sudo apt-add-repository http://lcas.lincoln.ac.uk/repos/release``
4. update your index:

   ``sudo apt-get update``
5. Install the package "uol\_cmp3641m" which will install all required
   packages:

   ``sudo apt-get install ros-indigo-turtlebot-gazebo``

2. Launch Simulation
--------------------

1. Define ``TURTLEBOT_GAZEBO_WORLD_FILE``:

   ``export TURTLEBOT_GAZEBO_WORLD_FILE=/opt/ros/indigo/share/turtlebot_gazebo/empty.world``

2. Launch Simulation:

   ``roslaunch turtlebot_gazebo turtlebot_world.launch world_file:=$(rospack find turtlebot_gazebo)/worlds/empty.world``

3. Launch RVIZ:

   ``rosrun rviz rviz``

4. Keyboard teleop:

   ``roslaunch kobuki_keyop keyop.launch``

2. Create 2D Map
----------------

1. run gmapping after all steps in 2:

   ``rosrun gmapping slam_gmapping``

2. Navigate using Move\_base:
-----------------------------

1. simple version:

   ``roslaunch turtlebot_navigation amcl_demo.launch map_file:=/my_2dmap.yaml``

2. check link:
   ``http://wiki.ros.org/turtlebot_navigation/Tutorials/Autonomously%20navigate%20in%20a%20known%20map``

2. Create Topological Map
-------------------------

TOM check this also needs to be running
https://github.com/LCAS/Rusty/blob/indigo-devel/rusty\_simulation/scripts/robot\_pose\_publisher.py

1. Launch MongoDB:

   ``roslaunch mongodb_store mongodb_store.launch db_path:=/path/to/mongodb``

2. Launch Topological Navigation:

   ``roslaunch topological_navigation topological_navigation_empty_map.launch map:=Name_of_your_map``

3. Launch RVIz:

4. Add Interactive markers to edit your map




Original page: https://github.com/strands-project/lamor15/wiki/ICRAI-workshop
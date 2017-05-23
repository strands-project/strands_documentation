The repo contains the catkin package package octomap\_launch. To be able
to run it you need the octomap stack. You can get it by running sudo
apt-get install ros-groovy-octomap-mapping. If you also want to
visualize the maps you create you can get the octovis visualizer tool by
running sudo apt-get install ros-groovy-octovis.

roslaunch octomap\_launch octomap.launch map:=(PATH\_TO\_MAP)/map.yaml -
for running the scitos nav stack package for localization and octomap
for map building. You need to have the scitos drivers, including the
laser scanner and the state\_publisher up and running before doing this.

If you want to view the map while building it using octomap, you can
visualize it in rviz by adding a MarkerArray on topic
occupied\_cells\_vis\_array.

To save the map created by octomap, just do rosrun octomap\_server
octomap\_saver -f (FILENAME).bt. You can view the map file by just
typing octovis (FILENAME).bt in the command line. There is an example 3D
map created on the robot in octomap\_launch/example\_maps/map3d.bt that
you can try this out with.


Original page: https://github.com/strands-project/strands_3d_mapping/wiki/Get-up-and-running
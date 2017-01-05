# Strands Documenation
Public documentation for the outputs of the STRANDS Project. 

This readme will guide you through the setup and use of a system which uses the
STRANDS packages. It is assumed that you have a system that is running Ubuntu
14.04.

## ROS and package setup 
### Installing ROS

The first step is to follow the instructions found at
http://wiki.ros.org/indigo/Installation/Ubuntu. The full install of ROS with the
package `ros-indigo-desktop-full` should contain all the packages that are required.

### Installing STRANDS packages

To install the strands packages, you should follow the instructions at
https://github.com/strands-project-releases/strands-releases/wiki.

### Example system

Before setting up your own system, you might like to see what a system might
look like. Instructions for setting up an example system can be found at
https://github.com/strands-project-releases/strands-releases/wiki/Example-STRANDS-System

## Custom system setup

### Database

While the system is running, it will store data in a mongodb database so that
various components can access it. Depending on what tasks you are running, the
database can grow quite large (on the order hundreds of gigabytes), so you
should create the database on a drive with a lot of space.

The database will be automatically created by the database node, but requires
the creation of a directory before it is launched. Running the following will
initialise the database. The database is launched in the same way when the full
system is running - it should be run before any other part of the system runs,
as many of them require it to be up.

```sh
DATA_DIR=/my/data/directory
mkdir -p $DATA_DIR/my_database_dir
roslaunch mongodb_store mongodb_store.launch db_path:=$DATA_DIR/my_database_dir
```

You can see more information about the database system at
https://github.com/strands-project/mongodb_store/tree/hydro-devel/mongodb_store

### Metric map

The metric map is a 2D map of the operating environment, where each cell of a
grid is populated with a value which represents whether that that cell is
occupied by an obstacle, is empty, or has an unknown occupancy state. The
quickest and easiest way to map your environment is using the
[ROS gmapping](http://wiki.ros.org/gmapping) package. How you use this package
will depend on the type of robot you have. The package requires that you have
laser and odometry data being published to the ROS system.

Assuming that your laser data is being published on `/base_scan`, and odometry
on `/odom`, you can start the mapping process as below. The
`maxUrange` parameter defines a threshold on the distance of usable range
measurements received. For example, setting this to 20 will discard any readings
received which are beyond 20 metres.

```sh
rosrun gmapping slam_gmapping scan:=base_scan maxUrange:=20
```

While this runs, you can observe the map being built in the `rviz` utility by
adding a display for the `/map` topic.

Once you are happy with your map, you should save it using the
[`map_server`](http://wiki.ros.org/map_server):

```sh
rosrun map_server map_saver -f my_map map:=my_map_topic
```

This will produce a `.pgm` file and a `.yaml` file. The `.pgm` file contains an
image of the map, which you can manipulate with an image editing program if
necessary. The `.yaml` file contains information about the map. If something
strange is happening with your map, then it might be worth checking that this
file is set up to point to the correct `.pgm` file. You can also adjust the
resolution of the map and its origin in the `.yaml` file.

### Topological map

Once you have a metric map, you need to set up a topological map for the robot
to use for path planning and other actions. The topological map is made up of
nodes, which represent some point of interest or navigation location, and edges,
which are connections between the nodes. The easiest way to set up the
topological map is using the strands utilities created for that purpose.

The following will launch the topological map visualiser, which allows for the
creation of the topological map:

```sh
rosrun topological_navigation visualise_map.py /path/to/my/map.yaml
```

In rviz, display the `/map` topic and the `InteractiveMarkers` topic
`/topological_map_markers/update`. If you have not previously added any nodes to
the map, a single marker should be displayed at the current origin of the map.
You can edit the origin of the map (relative to the bottom left corner of the
`.pgm` image in the `.yaml` file for the map. The marker can be moved in the
plane by clicking the arrow and dragging, and rotated using the ring. Right
clicking the arrow will give you a menu which can be used to create and delete
nodes.

You must also add edges between nodes so that the system can plan paths. This
can be done by adding the topological edge creation tool to rviz

### Routine



### Launching the core nodes



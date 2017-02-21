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

### Using a simulation
```sh
roslaunch --wait topological_utils dummy_topological_navigation.launch map:=tsc2015
```

fast mode: https://github.com/strands-project/lamor15/wiki/Individual-Computer-Setup

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
adding a display for the `/map` topic. Push the robot around in your operation
area. You should try to move relatively slowly. You should also try to ensure
that you revisit previously mapped areas after going around the environment, so
that the map can be properly adjusted.

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

At this point, you may wish to clean up the image to remove dynamic obstacles
from the map. In GIMP, you can do this by using the pencil tool with white
selected.

Along with the base map, it is also possible to provide a "nogo" map, which is
used to more strictly define which areas are passable and which are not. You can
use this to restrict the robot's movement in an area where there are no walls to
obstruct the robot's motion. The nogo map should duplicate the base map. You can
then draw obstacles onto the map in black (255) in the places which you would
like to have a phantom obstacle. The pencil tool in GIMP is again useful. We
recommend creating a new GIMP file with the nogo map on a new layer so that it
can be more easily modified if necessary. GIMP can export the file to a `.pgm`
file.

#### Adding to the map

Sometimes it may be necessary to remap parts of the map due to changes in the
environment. You can use gmapping to do this, and then stitch the images
together in an image editing program. Sometimes, you may need to rotate the
images. You should change the interpolation settings when you do this to "none"
to prevent blurring. If you somehow end up with a blurred map, it is possible to
fix it as follows.

Using GIMP, first make two duplicates of the layer containing the map. In the
first layer duplicated layers, use `colours>threshold`, to extract out the black
regions. A lower threshold of between 190 and 203 seems to be effective, with
the upper at 255. You should tweak the lower threshold so that the grey unknown
areas are white, and most of the obstacles are black. Then, using `select>by
colour`, select the white part of the layer and cut and paste it onto a new
layer (`C-x C-v`). When you paste, a floating selection layer will come up.
Right click this floating selection in the layer list, and send it to a new
layer. You now have two layers, one with free space, and one with obstacles.

In the other duplicated layer, do the same thing, but now extract the obstacles
and unknown regions by thresholding. A lower threshold of between 230 and 240
should work. Select the white region with the colour select tool again, and
delete it. Select the black pixels, and then use `select>shrink` to shrink the
selection by a couple of pixels. 2 or 3 should be sufficient. With this
selection still active, create a new layer. Use the pipette tool, to sample the
"unknown" cell colour from the original map. Paint over the selected area with
the pencil tool so that it has the "unknown" colour. Arrange the three layers so
that the obstacles are on top, unknown regions below, and free space below that.
Finally, merge the three layers by right clicking the obstacle layer and
clicking "merge down". Do this again to merge the newly created layer and the
free space layer.

### Topological map

Once you have a metric map, you need to set up a topological map for the robot
to use for path planning and other actions. The topological map is made up of
nodes, which represent some point of interest or navigation location, and edges,
which are connections between the nodes. The easiest way to set up the
topological map is using the strands utilities created for that purpose.

If you already have a map, you can add it into the database with

```sh
rosrun topological_utils load_yaml_map.py /path/to/my.yaml
```

This yaml file can be produced for a map that exists in the database using

```sh
rosrun topological_utils map_to_yaml.py map_pointset my_topmap.yaml
```

You can see which topological maps already exist in the database with

```sh
rosrun topological_utils list_maps
```

If you haven't yet created a map you can add an empty map to the database with

```sh
rosrun topological_utils insert_empty_map.py my_pointset_name
```

#### Modifying the map
The best way to modify the map is the use the `topological_rviz_tools` package.
This provides some tools and a panel in `rviz` which will allow you to quickly
and easily modify things. If you need more direct access, you can always dump
the map in the database (with `map_to_yaml.py`), edit things in the file, and
then replace the values in the database with the modified values. This can
result in internal inconsistencies, so it is not recommended.

You can launch the rviz tool as follows:

```sh
roslaunch topological_rviz_tools strands_rviz_topmap.launch map:=/path/to/map.yaml topmap:=topmap_pointset db_path:=/path/to/db
```

If you inserted an empty map into the database, you should see something like
the following when you launch:

![Empty launch](images/00_empty_launch.png)

Once you have added a new node to the map, you should delete the `temp_node`.
For instructions on using the rviz topological map editor, see the readme
[here](https://github.com/strands-project/strands_navigation/tree/indigo-devel/topological_rviz_tools).

### Routine



### Launching the core nodes



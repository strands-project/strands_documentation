KTH Meta-rooms dataset
----------------------

![](images/meta_rooms/Robot_s.png)

![](images/meta_rooms/Map.png)

KTH Scitos G5 robot - Rosie

2D Map with waypoints

The data was collected autonomously by a Scitos G5 robot with an RGB-D camera on a pan-tilt, navigating through the KTH office environment over a period of 7 days. Three waypoints have been defined on the 2D map, and each one is visited once per day. Each observation consists of a set of 28 RGB-D images obtained by moving the pan-tilt in a pattern, in increments of 60 degrees horizontally and 30 degrees vertically. The data is a part of the [Strands](http://strands.acin.tuwien.ac.at/index.html) EU FP7 project.

![](images/meta_rooms/instance1_s.png)

![](images/meta_rooms/instance2_s.png)

![](images/meta_rooms/instance3_s.png)

![](images/meta_rooms/instance4_s.png)

Observations acquired by the robot

### Dataset structure

The [data](https://strands.pdc.kth.se/public/metric_sweeps_201312) is structured in folders as follows: *YYYYMMDD/patrol\_run\_YYY/room\_ZZZ*, where:

-   **YYYYMMDD** represents the year, month & day when those particular observations were acquired. Each such folder contains the patrol runs the robot collected on that specific date.
-   **patrol\_run\_YYY** represents one of the patrol runs collected by the robot.
-   **room\_ZZZ** represents a particular observation collected during a patrol run.

Each folder of the type *YYYMMDD/patrol\_run\_YYY/room\_ZZZ* contains the following files:

-   **room.xml** - contains information relevant for the observation (described in the next section)
-   **complete\_cloud.pcd** - the point cloud of the observation (obtained by merging the individual point clouds together)
-   **intermediate\_cloud\*.pcd** - ordered point clouds, each corresponding to an RGB and depth image acquired by the camera while conducting the sweep (28 such point clouds for each observation)

The *room.xml* file accompanying an observation contains the following (relevant) fields:

**RoomLogName** - identifier which associates the observation with the folder structure

**RoomRunNumber** - identifier which denotes when the observation was acquired during the patrol run (i.e. 0 - first, 1 - second, etc.)

**RoomStringId** - identifier which corresponds to the waypoint at which the observation was acquired.

**RoomLogStartTime / RoomLogEndTime** - acquisition time

**Centroid** - observation centroid in the map frame

**RoomCompleteCloud** - complete cloud filename

**RoomIntermediateClouds**

**RoomIntermediateCloud** - intermediate cloud filename

-   **RoomIntermediateCloudTransform** - transform from the RGB-D sensor frame to the map frame, as given by the robot odometry

### Parsing

A parser is provided [here](https://github.com/strands-project/strands_3d_mapping/tree/hydro-devel/metaroom_xml_parser) (can be installed with ` sudo apt-get install ros-indigo-metaroom-xml-parser`) which reads in the data and returns C++ data structures encapsulating the low-level data from the disk. Form more information please refer to [the parser README](https://github.com/strands-project/strands_3d_mapping/tree/hydro-devel/metaroom_xml_parser) ( or [here](https://github.com/strands-project/strands_3d_mapping/blob/hydro-devel/metaroom_xml_parser/include/metaroom_xml_parser/load_utilities.h) for a list of supported methods). Information about how to use the Strands package repository can be found [here](https://github.com/strands-project-releases/strands-releases/wiki).

### Download

This dataset is available for download in a single archive [file](https://strands.pdc.kth.se/public/metric_sweeps_201312.tar.gz) (\~ 12 GB). As an alternative, the individual folders and files can be obtained from [here](https://strands.pdc.kth.se/public/metric_sweeps_201312), and would have to be downloaded manually.

* * * * *

### Condition of use

If you use the dataset for your research, please cite our [paper](https://strands.pdc.kth.se/public/metric_sweeps_201312/ambrus2014metaroom.pdf) that describes it:

        
        Meta-rooms: Building and maintaining long term spatial models in a dynamic world
        Ambrus, Rares and Bore, Nils and Folkesson, John and Jensfelt, Patric
        Intelligent Robots and Systems (IROS), 2014 IEEE/RSJ International Conference on
        
        

We attached a [bibtex](https://strands.pdc.kth.se/public/metric_sweeps_201312/ambrus2014metaroom.bib) record for your convenience.

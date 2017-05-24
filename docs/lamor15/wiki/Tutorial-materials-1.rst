Using the Strands Navigation System
===================================

The `strands
navigation <https://github.com/strands-project/strands_navigation>`__
system is composed by three layers of components:

-  **Action Layer**: The action layer is where all the navigation
   actions that the robot could use are, in other words, in this layer
   you will find the actions that move the robot in the environment,
   these action could be for example `Docking or
   Undocking <https://github.com/strands-project/scitos_apps/tree/hydro-devel/scitos_docking>`__,
   `Door
   passing <https://github.com/strands-project/strands_apps/tree/indigo-devel/door_pass>`__
   or `move base <http://wiki.ros.org/move_base>`__.

-  **Monitored Navigation Layer** : `This
   layer <https://github.com/strands-project/strands_navigation/tree/indigo-devel/monitored_navigation>`__
   monitors the actions in the action layer and in case of failure it
   can activate specific `recovery
   behaviours <https://github.com/strands-project/strands_recovery_behaviours>`__.

-  **Topological Navigation Layer** : `This
   layer <https://github.com/strands-project/strands_navigation/tree/indigo-devel/topological_navigation>`__
   connects the different locations in the environment by means of
   navigation actions and the topology of the environment, to do so it
   use an *occupancy grid map* and a *topological map* that defines
   locations in the space where the robot can navigate to and the means
   to reach such locations.

The goal of this tutorial is to show you how to setup a working
navigation system, from creating the occupancy grid map to set up the
topological navigation system.

Creating occupancy grid map
===========================

For creating the map we are going to use
`gmapping <http://wiki.ros.org/gmapping>`__, however you can use maps
created with other methods. We are going to see a first example using a
simulation.

1. The first step is to launch a simulation, for convenience there is a
   tmux script in the lamor\_bringup package, to run it execute:
   ``rosrun lamor_bringup sim_start.sh``

2. Once this is started switch to tab 2 (``ctrl``\ + b + 2) and press
   ``enter``, this will open a screen like this: |Sim Screen shot|

   Please note that the robot is on the charging station, this is not a
   coincidence, it is to have all maps zeroed in the charging station.

3. the next step is to start gmapping, open a new tab and run:
   ``rosrun gmapping slam_gmapping``

4. run Rviz, ``rviz`` |Rviz shot|

5. click on the morse window and use arrows to navigate the robot, you
   should see in rviz how the map is being created: |Rviz shot|

6. Once you are happy with your map, you can save it running
   ``rosrun map_server map_saver`` this will create map.pgm and map.yaml
   files, but you will notice that this map might be a bit too big fro
   your liking, you can solve this problem by running
   ``rosrun map_server crop_map map.yaml`` this will create cropped.pgm
   and cropped.yaml the final result should look something like this
   |map| you can rename your map as you wish, but don't forget that the
   image field in the yaml file must correspond to the name (and path if
   you wish) of your map image.

Creating the Topological Map
============================

**RViz** can be used to edit topological maps on system runtime, one
easy way of creating a map is inserting a basic *topological map* and
editing it using *RViz*. The Following steps will guide through this
process.

1. It is necessary to insert a basic map in the DB and run the
   navigation system based on it:
   ``rosrun topological_utils insert_map.py $(rospack find topological_utils)/support/empty.tmap topological_map_name environment_name``

2. Once this is done you can run **Rviz**, ``rosrun rviz rviz`` and
   create two *marker array* interfaces
   ``/topological_node_zones_array`` and ``/topological_edges_array``
   optionally an additional *marker array* interface can be created
   ``/topological_nodes_array``. This will allow the visualization of
   the topological map.

3. After this the map can be edited using interactive markers:

-  **Adding Nodes:** for this objective there is one interactive marker
   topic called ``/name_of_your_map/add_rm_node/update`` that will put a
   green box on top of the robot. Drive the robot where you want to add
   a new node and press on the green box that will add a node there
   connected to all close by nodes by a *move\_base* action.

-  **Editing Node Position:** with ``/name_of_your_map_markers/update``
   it is possible to move the waypoints around and change their final
   goal orientation.

-  **Removing Unnecessary Edges:** to remove edges there is another
   marker ``/name_of_your_map_edges/update`` that will allow you to
   remove edges by pressing on the red arrows.

-  **Change the Influence Zones:** Finally it is possible to change the
   influence zones with ``/name_of_your_map_zones/update`` and moving
   the vertices of such zones around.

Creating the topological map in simulation
------------------------------------------

1. Run the tmux script tab by tab until tab 3
   ``rosrun lamor_bringup sim_start.sh``

2. Afterwards run:
   ``roslaunch topological_utils create_topological_map.launch met_map:=bandl top_map:=bl_sim``
   or alternatevely you can insert the empty map and run
   ``rosrun lamor_bringup sim_start.sh`` Tabs 0, 1, 2, 4

Local metric map / semantic map
===============================

Description
===========

This set of nodes allows the creation, calibration, storage and querying
of local metric maps as well as the detected dynamic elements. Recorded
data is stored in ``~/.semanticMap/`` and the number of observations
stored for each waypoint can be specified as a launch file parameter, as
well as whether the observations should be stored in mongodb. Detailed
information about how the individual nodes function, input/output topics
and a parameters can be found in the corresponding readme files.

**You cannot run this part of the tutorial in *fast-mode* (wireframe)
simulation. You need the full simulation. Please either work with
someone who has it running or use the provided desktop machines**

Start all the components
~~~~~~~~~~~~~~~~~~~~~~~~

-  Install dependencies

::

    sudo apt-get install sudo apt-get install ros-indigo-semantic-map-launcher

::

    sudo apt-get install ros-indigo-metaroom-xml-parser 

::

    sudo apt-get install ros-indigo-scitos-ptu

Also, please create the following folder (this folder should be created
automatically, however as a precaution please create it yourself):

::

    mkdir ~/.semanticMap/

-  Run dependencies:

Please make sure you are still running the components from the previous
tutorial (mongo\_db, simulator or robot, 2d\_navigation, topological
navigation, head\_camera, etc). In addition, please start:

::

    rosrun scitos_ptu ptu_action_server_metric_map.py

-  if you are running in simulation, you need to emulate the RGBD
   cameras correctly using this command (note that you *cannot* run the
   local metric mapping if you are using the *fast-mode* (wireframe)
   simulation, as you won't have the camera topics needed):

::

    roslaunch strands_morse generate_camera_topics.launch

-  System nodes (note that this command starts all the relevant nodes,
   and you should not start any other nodes when moving on to the next
   sections):

::

    roslaunch semantic_map_launcher semantic_map.launch

Doing a metric sweep (package ``cloud_merge``)
==============================================

The underlying data used by the nodes in this package is obtained by
performing a sweep of the Pan-Tilt Unit and collecting RGBD data at a
number of positions during the sweep.

Relevant nodes
~~~~~~~~~~~~~~

``rosrun cloud_merge do_sweep.py``

``roslaunch cloud_merge cloud_merge.launch``

``rosrun scitos_ptu ptu_action_server_metric_map.py``

Operation
~~~~~~~~~

Prior to starting a sweep, please make sure you are well localized on
the map (you can do this by looking at your robot's position in Rviz).
To start a sweep use the ``do_sweep`` action server:

::

    rosrun actionlib axclient.py /do_sweep

This action server takes as input a string, with the following values
defined: ``complete``, ``medium``, ``short``, ``shortest``. Internally
the action server from ``scitos_ptu`` called
``ptu_action_server_metric_map.py`` is used, so make sure that is
running.

The behavior is the following:

-  If sweep type is ``complete``, the sweep is started with parameters
   ``-160 20 160 -30 30 30`` -> 51 positions
-  If sweep type is ``medium``, the sweep is started with parameters
   ``-160 20 160 -30 30 -30`` -> 17 positions
-  If sweep type is ``short``, the sweep is started with parameters
   ``-160 40 160 -30 30 -30`` -> 9 positions
-  If sweep type is ``shortest``, the sweep is started with parameters
   ``-160 60 140 -30 30 -30`` -> 6 positions (there might be blank areas
   with this sweep type, depending on the environment).

The cloud\_merge\_node acquires data from the RGBD sensor, as the PTU
unit does a sweep, stopping at various positions. As the PTU stops at a
position, a number of RGBD frames are collected and averaged, with the
purpose of reducing noise. Each one of these frames are converted to the
global frame of reference, and merged together to form an observation
point cloud, which is further processed by the ``semantic_map``
``semantic_map_node``.

If the sweep intermediate positions have been calibrated (using the
``calibrate_sweeps`` ``calibrate_sweep_as action server``) and the
parameter ``register_and_correct_sweep`` is set to ``true``, the
collected sweeps are also registered. Note that this registration is for
the intermediate point clouds making up the sweep, and not between two
sweeps.

The observations are stored on the disk, in the folder

``~.semanticMap/``

Waypoint
~~~~~~~~

The acquired observations are indexed according to the waypoint at which
the sweeps were performed. This information is acquired on the topic
``/current_node``, published by the topolofi

Intermediate cloud calibration (package ``calibrate_sweeps``)
=============================================================

As described earlier, each observation consists of a number of point
clouds acquired at intermediate positions during a sweep. However, the
exact pose of the camera optical center (camera frame of reference) with
respect to the body of the robot (the odometry frame of reference) is
not known exactly apriori, and hence when merging together the
intermediate clouds misalignment errors often occur. To account for
this, a calibration procedure has been developed that considers data
from all observations of a particular type recorded so far.

Relevant nodes
~~~~~~~~~~~~~~

::

    rosrun calibrate_sweeps calibrate_sweep_as

Operation
~~~~~~~~~

To start the calibration procedure, call:

::

    rosrun actionlib axclient.py /calibrate_sweeps

The calibration process uses only observations recorded with the type
``complete`` if using the ``do_sweeps.py`` action server from the
``cloud_merge`` package, i.e. with 51 positions.

If using the ``ptu_action_server_metric_map.py`` action server from the
``scitos_ptu`` package to record observations, the parameters are
``-160 20 160 -30 30 30``.

Sweeps recorded with different parameters are ignored for the
calibration. For registration, sweeps with different parameters are also
processed if their parameters are a subset of the ``complete`` sweep
type parameters (e.g. ``comlpete`` sweep type parameters are
``-160 20 160 -30 30 30``; an example subset of those would be
``-160 40 160 -30 30 30``, i.e. fewer pan stops).

Calibration results
~~~~~~~~~~~~~~~~~~~

The calibration results are saved in ``~/.ros/semanticMap``. These are:

-  ``registration_transforms.txt`` the result of the 51 transforms for
   the intermediate poses.
-  ``registration_transforms_raw.txt`` legacy - contains the same data
   as above in a different format, needed by the
   ``strands_sweep_registration`` package.
-  ``camera_params.txt`` contains the optimized camera parameters. This
   is currently disabled, and the stored camera parameters should be the
   same as the input camera parameters.
-  ``sweep_paramters.txt`` the sweep parameters used by the calibration
   (``-160 20 160 -30 30 30``)

Metarooms and dynamic clusters (package ``semantic_map``)
=========================================================

A meta-room contains only those parts of the scene which are observed to
be static, and it is created incrementally as the robot re-observes the
same location over time. Over time, as the robot visits the same
location multiple times, the static part is modelled, and it is used to
extract what is dynamic from subsequent observations.

This package takes room observations as they are constructed by the
``cloud_merge`` package and extracts the corresponding metaroom and also
computes dynamic clusters at each waypoint. Note that one metaroom is
constructed for each waypoint.

Some data is stored on the disk, in the folder

::

    ~.semanticMap/metarooms

Relevant nodes
~~~~~~~~~~~~~~

::

    roslaunch semantic_map semantic_map.launch

Operation
~~~~~~~~~

Once a new sweep has been performed at a waypoint, the corresponding
metaroom is loaded (if it exists, otherwise a metaroom is initialized
with the new observation), and it is used to extract the dynamic
clusters/objects at that waypoint.

Sweep registration
~~~~~~~~~~~~~~~~~~

The NDT algorithm is used to register obseravtions taken at the same
waypoint together. The initial guess is provided by the AMCL robot pose,
however, depending on the scene, the amount of changes between
observations and sensor noise, sometimes the observations are poorly
registered, resulting in poor dynamic clusters. One alternative in that
case is to reset the metarooms, using the service described in the next
section.

ClearMetaroomService
~~~~~~~~~~~~~~~~~~~~

This service resets the metarooms at specific waypoints.

Message type:

::

    string[] waypoint_id
    bool initialize
    ---

If initialize is set to ``True``, the Meta-Rooms at the specific
waypoints are re-initialized with the latest observations collected at
those waypoints. Otherwise, the Meta-Rooms are just deleted.

All vs most recent clusters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default behavior of this node is to return all the dynamic clusters
in an observation, as compared to the corresponding metaroom. However,
sometimes this may mean a lot of information, and for that the parameter
``newest_dynamic_clusters`` is provided (default value ``False``) - if
set to ``True``, the node will compute dynamic clusters by comparing the
latest sweep with the previous one (as opposed to comparing the latest
sweep to the metaroom), thus reporting only the latest dynamic clusters.

Requesting dynamic clusters (package ``object_manager``)
========================================================

This package allows interaction with the dynamic clusters segmented by
the ``semantic_map`` package

Relevant nodes
~~~~~~~~~~~~~~

::

    rosrun object_manager object_manager_node

DynamicObjectsService
~~~~~~~~~~~~~~~~~~~~~

Message tpe:

::

    string waypoint_id
    ---
    string[] object_id
    sensor_msgs/PointCloud2[] objects
    geometry_msgs/Point[] centroids

Given a waypoint id, this service returns all the dynamic clusters
segmented at that waypoint, with their ids, point clouds and centroid.

Service topic: ``ObjectManager/DynamicObjectsService``

The point cloud corresponding to all the dynamic clusters is also
published on the topic ``"/object_manager/objects``

GetDynamicObjectService
~~~~~~~~~~~~~~~~~~~~~~~

Message type:

::

    string waypoint_id
    string object_id
    ---
    sensor_msgs/PointCloud2 object_cloud
    int32[] object_mask
    geometry_msgs/Transform transform_to_map
    int32 pan_angle
    int32 tilt_angle

Given a waypoint id and a cluster id (should correspond to the ids
received after calling the ``DynamicObjectsService``), this service
returns the point cloud corresponding to that dynamic cluster in the
camera frame of reference and a transform to get the point cloud in the
map frame of refence. In addition, a set of angles (``pan_angle``, and
``tilt_angle``) to which to turn the PTU, and a set of indices
representing image pixels corresponding to the dynamic cluster in the
image obtained after turning the PTU to the specified angles. After
calling this service, the requested dynamic cluster is "selected", and
after receiving the ``start_viewing`` mesasge on the
``object_learning/status`` topic, additional views received on the
``/object_learning/object_view`` topic will be added and logged together
with this cluster.

Service topic: ``ObjectManager/GetDynamicObjectService``

The point cloud corresponding to the requested dynamic cluster is also
published on the topic ``/object_manager/requested_object``.

The cluster mask is also published as an image on the topic:
``/object_manager/requested_object_mask``

Note that the clusters are logged to the database when calling the
``DynamicObjectsService`` or the ``GetDynamicObjectService`` (if the
``log_to_db`` argument is set to ``True``). Calling these services
multiple times does not affect (negatively) the logging.

Accessing observation data online (package ``semantic_map_publisher``)
======================================================================

This package provides an interface to observation data previously
recorded and stored on the disk. The data can be queried using the
services described below (note that only some of the services available
are described below; for more information please refer to the package
description).

Relevant nodes
~~~~~~~~~~~~~~

::

    rosrun semantic_map_publisher semantic_map_publisher

WaypointInfoService
~~~~~~~~~~~~~~~~~~~

Message type:

::

    ---
    string[] waypoint_id
    int32[] observation_count

Returns a list of waypoints along with the number of observations
collected at those waypoints.

Service name: ``SemanticMapPublisher/WaypointInfoService``

ObservationService
------------------

Message type:

::

    string waypoint_id
    float64 resolution
    ---
    sensor_msgs/PointCloud2 cloud

Given a waypoint, and a resolution, this service returns the latest
observation collected at that waypoint as a PointCloud with the
specified resolution.

Service name: ``SemanticMapPublisher/ObservationService``

WaypointTimestampService
------------------------

Message type:

::

    string waypoint_id
    ---
    string[] waypoint_timestamps

Given a waypoint, this service returns the timestamps of all the
observations collected at that waypoint, as a list.

Service name: ``SemanticMapPublisher/WaypointTimestampService``

ObservationInstanceService
--------------------------

Message type:

::

    string waypoint_id
    int64 instance_number # convention 0 - oldest available
    float64 resolution
    ---
    sensor_msgs/PointCloud2 cloud
    string observation_timestamp

Given a waypoint id, an instance number and a resolution, this service
returns a particular instance from the observations collected at that
particular waypoint, with the desired resolution, along with the
timestamp of the observation (as opposed to ``ObservationService`` which
returns the latest observation at that particular waypoint). Service
name: ``SemanticMapPublisher/ObservationInstanceService``

Accessing data stored on the disk (package ``metaroom_xml_parser``)
===================================================================

The ``metaroom_xml_parser`` package is used to parse previously saved
room observations. The data will be read into an appropriate data
structure containing: merged point cloud, individual point clouds,
individual RGB and depth images and corresponding camera parameters.

Utilities
---------

A number of utilities are provided by this package, for easy data
manipulation. The definitions can be seen in the file
``load_utilities.h``

Merged cloud utilities
~~~~~~~~~~~~~~~~~~~~~~

The complete cloud datatype is:

``template <class PointType> boost::shared_ptr<pcl::PointCloud<PointType>>``

The utilities for loading only the merged cloud are: \*
``loadMergedCloudFromSingleSweep`` # returns one cloud \*
``loadMergedCloudFromMultipleSweeps`` # returns a vector of merged
clouds, one for each sweep \* ``loadMergedCloudForTopologicalWaypoint``
# same as above

Intermediate cloud utilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The intermediate cloud datatype is:

::

        template <class PointType>
        struct IntermediateCloudCompleteData
        {
            std::vector<boost::shared_ptr<pcl::PointCloud<PointType>>>  vIntermediateRoomClouds;
            std::vector<tf::StampedTransform>                           vIntermediateRoomCloudTransforms;
            std::vector<image_geometry::PinholeCameraModel>             vIntermediateRoomCloudCamParams;
            std::vector<cv::Mat>                                        vIntermediateRGBImages; // type CV_8UC3
            std::vector<cv::Mat>                                        vIntermediateDepthImages; // type CV_16UC1
        };

The utilities for loading the intermediate clouds are: \*
``loadIntermediateCloudsFromSingleSweep`` # just the point clouds \*
``loadIntermediateCloudsCompleteDataFromSingleSweep`` # complete data,
with transforms and images \*
``loadIntermediateCloudsFromMultipleSweeps`` \*
``loadIntermediateCloudsCompleteDataFromMultipleSweeps`` \*
``loadIntermediateCloudsForTopologicalWaypoint`` \*
``loadIntermediateCloudsCompleteDataForTopologicalWaypoint``

Sweep XML utilities
~~~~~~~~~~~~~~~~~~~

The sweep XML is an ``std::string``

The utilities for finding sweep XMLS are: \* ``getSweepXmls`` # takes a
folder where to search as argument. Returns a ``vector<string>`` \*
``getSweepXmlsForTopologicalWaypoint``

Dynamic cluster utilities
~~~~~~~~~~~~~~~~~~~~~~~~~

The dynamic clusters type is:

``template <class PointType> std::vector<boost::shared_ptr<pcl::PointCloud<PointType>>>``

The dynamic cluster utilities are: \*
``loadDynamicClustersFromSingleSweep`` \*
``loadDynamicClustersFromMultipleSweeps`` \*
``loadDynamicClustersForTopologicalWaypoint``

Data collected so far in Strands and available online
=====================================================

A number of datasets (in the formats described above) have been
collected during Strands and made publicly available. For more
information look at:

::

    https://strands.pdc.kth.se/public/

Debugging / troubleshooting
===========================

Bad / incorect dynamic clusters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If for some reason (i.e. poor registration) the meta-rooms have
diverged, the reported dynamic clusters will not be correct. In that
case, use the ``ClearMetaroomService`` service to reset the meta-rooms:

This service resets the Meta-Rooms at specific waypoints.

Message type:

::

    string[] waypoint_id
    bool initialize
    ---

If initialize is set to ``True``, the Meta-Rooms at the specific
waypoints are re-initialized with the latest observations collected at
those waypoints. Otherwise, the Meta-Rooms are just deleted.

Crashes
~~~~~~~

In case there are issues (i.e. nodes crashing) and restarting the nodes
does not solve the problems, you can try deleting the data stored in
``~/.semanticMap``. Note that this operation cannot be undone, and that
data will be lost (if you want to keep that data be sure to move it
somewhere else).

If the issues are still not solved, delete the data logged in
``mongo_db`` in the ``metric_maps`` database (using e.g. ``robomongo``).

.. |Sim Screen shot| image:: http://i.imgur.com/nj9JSHV.png
.. |Rviz shot| image:: http://i.imgur.com/DwR4E0n.png
.. |Rviz shot| image:: http://i.imgur.com/2swlO70.png
.. |map| image:: http://i.imgur.com/CAaEvC1.png


Original page: https://github.com/strands-project/lamor15/wiki/Tutorial-materials-1
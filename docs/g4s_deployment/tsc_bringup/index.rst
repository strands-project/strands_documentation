TSC bringup
===========

OBJECT/HUMAN SEARCH
===================

Requirements
------------

Get the following repositories:

-  https://github.com/kunzel/viper\_ros (branch Y3)
-  https://github.com/kunzel/viper (branch Y3)
-  https://github.com/jayyoung/world\_modeling
-  https://github.com/strands-project/soma (branch 2.0)
-  https://github.com/strands-project/semantic\_segmentation

   -  Run: ``rosrun semantic_segmentation download_rf.sh``

Further, we assume that a topological map, strands 3D mapping, and
mongoDB is used.

Basic Bringup
-------------

The ``tsc_robot_start.sh`` script is used to create tmux sessions which
are populated with the main launchers, and some other things that are
commonly run. By default, the script will bring up a tmux session on the
main PC and each of the side PCs. The session on the main PC will
automatically be attached. You can detach it with "Ctrl-b d". To attach
to a session use ``tmux attach -t sessionid``.

There are several options you can use when running the script. Use
``rosrun tsc_bringup tsc_robot_start.sh -h`` for help.

The script will ask you if you want to kill any existing session with
the requested sessionid (usually the current username). If you don't
kill the session, a new session will not be created.

Examples
~~~~~~~~

The basic script with no parameters will create tmux windows on all
three machines. If you want to be specific about which machine's tmux
session to start, you can do so using the switches ``--main``,
``--left``, or ``--right``. For example,

.. code:: sh

    rosrun tsc_bringup tsc_robot_start.sh --main --left

will set up the tmux sesssions on the main and left PCs.

The ``--kill`` option (with an argument of sessionid) can be used to
kill specific sessions. The switches referring to main, left and right
PCs can be used in conjunction with this. The following will kill the
sessions running on the left and right PCs with the id ``strands``.

.. code:: sh

    rosrun tsc_bringup tsc_robot_start.sh --kill strands --left --right

If you don't want to split the session across the three PCs, you can use
the ``--nosplit`` switch to run only on the main PC.

Getting Started
---------------

-  In order to search for objects/humans, model ROIs and SURFACE ROIs
   using the soma roi manager and note the ROI IDs:
   ``rosrun soma_roi_manager soma_roi.py <name of the map>``

-  ROIs are regions from which the robot searches objects

-  SURFACE ROIs are regions where the robot searches for objects

-  If not already running, launch the following:

-  ``roslaunch soma_manager soma2_local.launch``

-  ``roslaunch semantic_map_launcher semantic_map.launch``

-  On the same machine which runs the MongoDB (eg. bobl), launch the
   object search: ``roslaunch viper_ros object_search.launch`` or
   ``roslaunch tsc_bringup object_search.launch``

-  Start a search by demanding a task:
   ``rosrun  viper_ros demand_object_search_task.py <waypoint> <roi> <surface_roi> <mode>``,
   whereby waypoint is the waypoint name, roi is the region where the
   robot observes from, surface\_roi is the region which the robot
   observes and mode is either 'object' or 'human' (determines how the
   percepts are stored into SOMA).

OBJECT LEARNING
===============

To start the object learning action server run:

::

    roslaunch tsc_bringup object_learning.launch model_path:=/path/to/models record_run:=false

If the parameter ``record_run`` is set to ``true`` a rosbag of the robot
navigating around the object will be recorded using
`rosbag\_openni\_compression <https://github.com/strands-project/data_compression>`__.
The rosbag is saved as ``tracking.bag`` in the folder where the sweep is
saved.

**Note** recording a rosbag can take up to 1GB of disk space per run.

**Note** the xml of the current sweep where the rosbag is saved is
published when the sweep finished on the topic
``/local_metric_map/room_observations``.

To trigger an action run:

::

    rosrun actionlib axclient.py /learn_object

The argument needed is the name of the node (from the topological map)
where to run the ``learn_object`` action.

Nodes started
-------------

The launch file above is equivalent to the following:

-  ``roslaunch semantic_map_launcher semantic_map.launch``
-  dependencies installed through
   `strands\_3d\_mapping <https://github.com/strands-project/strands_3d_mapping>`__
-  ``roslaunch observation_registration_launcher observation_registration.launch``
-  dependencies installed through
   `strands\_3d\_mapping <https://github.com/strands-project/strands_3d_mapping>`__
-  ``roslaunch learn_objects_action learn_objects_dependencies.launch``
-  a list of dependencies can be found
   `here <https://github.com/strands-project/strands_3d_mapping/tree/hydro-devel/learn_objects_action>`__

Debug topics
------------

For debugging, the following topics are useful: \*
``/local_metric_map/merged_point_cloud_downsampled`` - the point cloud
of the sweep \* ``/local_metric_map/dynamic_clusters`` - the detected
dynamic clusters \* ``/object_manager/requested_object_mask`` - the mask
of the dynamic cluster which will be learned \*
``/object_learning/learned_object_xml`` - the xml of the dynamic cluster
learning, pointing to the additional views and masks (among other
things) \* ``/additional_view_registration/registered_view_cloud`` - the
point cloud of the registered additional views \*
``/incremental_object_learning/learned_model`` - learned model using the
RAL16 method \* ``/object_learning/learned_object_model`` - learned
model using the IROS16 method

Point Cloud History Search & Incremental Model Building
=======================================================

Note that you need the **newest** versions of
`strands\_3d\_mapping <https://github.com/strands-project/strands_3d_mapping>`__
and `quasimodo <https://github.com/nilsbore/quasimodo>`__ to be able to
run this. ``quasimodo`` will shortly be merged into
``strands_3d_mapping``. For a lot more info check the `quasimodo
readme <https://github.com/nilsbore/quasimodo/blob/master/README.md>`__.

In the ``tsc_start.sh`` tmux session, tab 10, there is are two panes
that start the entire pipeline for retrieval and incremental model
building. This needs to be started via ssh to set the ``display``
variable correctly. Note that you need to run both

::

    rosrun tsc_bringup tsc_headless.sh

for starting up a virtual display (be sure to type the password), and

::

    DISPLAY=:0 roslaunch tsc_bringup tsc_quasimodo.launch data_path:=/home/strands/.semanticMap

If you want some data to query for, we have uploaded all of the metric
map data from the Birmingham deployment week to the server. Otherwise
you will have to perform at least 20 sweeps with the robot to be able to
query. Get the already collected data with:

.. code:: bash

    wget https://strands.pdc.kth.se/public/semanticMap_BHAM.tar.gz
    tar -zxvf semanticMap_BHAM.tar.gz

Note that the folder is 16GB on disk. If you do not want to replace the
already existing ``~/.semanticMap`` data you can just use the downloaded
folder directly. Then you need to change the ``data_path`` argument of
``tsc_quasimodo.launch`` to ``/path/to/Birmingham/semanticMap``. If you
want to search for the data collected on the robot, it should be the
default ``/home/strands/.semanticMap``.

If you want to add previously collected metric maps to the retrieval
representation (as opposed to processing them as they are collected),
you can also set the parameter ``add_previous_maps:=true``. Processing
only has to be done once. If they have been processed previously (as is
the case for the data on the server), they are loaded automatically. You
will then have to wait to collect new metric maps until the processing
of the previously collected maps has finished.

Debug topics
------------

-  ``/quasimodo_retrieval/visualization`` - An image showing the result
   of there retrieval component. The leftmost image shows the masked RGB
   image of the query object and to the right are rendered views of the
   ten closest matches represented as 3D surfel clouds.
-  ``/models/fused`` - The fused model of the additional view
   observation that is queried at the moment. Published as
   ``sensor_msgs/PointCloud2``, displayed in relation to ``/map``.
-  ``/retrieval_processing/segmentation_cloud`` - The segmentation of a
   metric map cloud, published after a sweep is finished, published as
   ``sensor_msgs/PointCloud2``

Note
----

You can manually trigger a search (i.e. without using the incremental
object building framework) of an object with additional views by
starting

::

    rosrun quasimodo_retrieval quasimodo_retrieve_observation

and then, in another terminal specifying the path to the xml of the
additional views:

::

    rostopic pub /object_learning/learned_object_xml std_msgs/String "data: '/path/to/.semanticMap/201422/patrol_run_56/room_0/2016-Apr-22 14:58:33.536964_object_0.xml'"

You can also use `soma <https://github.com/strands-project/soma>`__ to
visualize the queries over time.

SOMA Visualizer
===============

SOMA Visualizer is a GUI for querying and visualizing SOMA objects.

Using the visual interface, advanced queries with spatio-temporal
constraints can be specified. The returned SOMA objects are displayed in
rviz as point clouds.

Prerequisites
-------------

-  MongoDB (>=2.6)
-  mongodb\_store
-  Qt5

Getting started (general steps)
-------------------------------

1. Start the ros core:

   ::

          $ roscore

2. Launch the ROS datacentre:

   ::

       $ roslaunch mongodb_store mongodb_store.launch db_path:=<path_to_db>

SOMA map manager
----------------

1. Run the soma map manager for storing, reading and publishing 2D map.
   Running this node is essential for running the
   robot\_state\_viewer\_node:
   ``$ rosrun soma_map_manager soma_map_manager_node.py --mapname <map_name>``
   If there are any stored 2D occupancy maps in the datacentre then map
   manager will let you choose the map to be published or you can input
   the name of the stored map as an argument as ``<map_name>``. If not,
   it will wait for map\_server. Run the map\_server with a 2D map:
   ``$ rosrun map_server map_server <map.yaml>`` where ``map.yaml``
   specifies the map you want to load. After running the ``map_server``,
   you should save the published map using the ``soma map manager``.

2. If you want to check the published map, start RVIZ, add a Map display
   type and subscribe to the ``soma/map`` topic:

   ::

       $ rosrun rviz rviz

SOMA Visualizer
---------------

You can run the visualizer by calling
``roslaunch soma_visualizer soma_visualizer.launch``

1. Add a MarkerArray display type in RVIZ and subscribe to the
   ``soma_roi_marker_array`` topic. The drawer will draw when a region
   is selected in the visualizer. Add a pointcloud2 display type and
   subscribe to ``/soma_visualizer_node/world_state_3d`` to visualize
   query results.

2. Run rviz to display the results of the queries. You can go back and
   forth between robot states using the slider. You can choose the time
   interval to be inspected in terms of days,hours and minutes. You can
   also execute advanced queries by setting dates, times, etc, enabling
   them using the checkboxes and by pressing the ``Query`` button. When
   you make changes in query constrains, make sure to press ``Query``
   button for updating the query. You can also export the executed query
   in JSON format using the ``Export JSON`` button. You can reload data
   from databse using ``Reload`` button. The returned objects are also
   displayed in the table view. You can double click on any of the rows
   to see the detailed information and images of that object. If there
   are multiple images, you can go through them by pressing to left and
   right buttons.

**For any query, if more than 50 objects are fetched, only first 50 of
them are fetched with point clouds and images because of the performance
issues**.

.. figure:: https://github.com/hkaraoguz/soma/blob/visualizeraddons/soma_visualizer/doc/soma_visualizer.png
   :alt: marker

   marker


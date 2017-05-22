SOMA Trajectory
===============

SOMA Trajectory is a package to query and display human trajectories. It
includes a simple visual interface to query spatio-temporal constraints.

Prerequisites
-------------

-  MongoDB (>=2.6)
-  mongodb\_store
-  pymongo
-  shapely

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

SOMA Trajectory Visualizer
--------------------------

You can run the visualizer by calling
``rosrun soma_trajectory soma_trajectory_manager.py`` and
``rosrun soma_trajectory visualiser.py``

1. Add an InteractiveMarkers display type in RVIZ and subscribe to the
   ``soma_trajectory`` topic. Trajectories will appear once the query
   submit button on the visualisation is pressed.

2. Run rviz to display the results of the queries. You can choose the
   time interval to be inspected in terms of hours from the hour the
   first trajectory obtained to the hour the last trajectory obtained.
   You can also execute temporal periodic queries by setting days of the
   week, and hours of a day. Whenever a checkbox inside the temporal
   peridic query is ticked, the regular query with the time interval
   will be ignored. A simple analysis is displayed in the message box in
   the bottom of the visualiser for each query.

.. figure:: https://github.com/strands-project/soma/blob/indigo-devel/soma_trajectory/doc/soma_trajectory.png
   :alt: marker

   marker


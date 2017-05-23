table\_detection
================

This package uses the ``primitive_extraction`` package to extract planes
and determines which of the planes are tables based on size, angle with
respect to floor, shape and height above floor. A list of detected
tables is kept locally and in the ``mongodb_store`` and new tables
overlapping with old ones are merged by finding the common convex hull.
All currently found tables can be found by querying all
``strands_perception_msgs/Table`` from the ``mongodb_store``.

The table detection is launched by:

``roslaunch table_detection detection.launch cloud:=/pointcloud2/topic``,

where ``/pointcloud2/topic`` is a point cloud in the frame of reference
of a global map. Currently, the package outputs three visualization
topics in RViz:

-  ``/primitive_extraction/primitive_marker_array`` - All detected
   planes from the last processed point cloud as
   ``visualization_msgs/MarkerArray``.
-  ``/table_detection/primitive_marker_array`` - All detected tables
   from the last processed point cloud as
   ``visualization_msgs/MarkerArray``.
-  ``/primitives_to_tables/table_markers`` - Tracked tables that have
   been determined to be new instances or merged with an old one,
   published as ``visualization_msgs/Marker``.

The launch file has a bunch of options and parameters, notably for
determining what is a table:

-  ``min_height`` - Minimum height of a table plane.
-  ``max_height`` - Maximum height of a table plane.
-  ``max_angle`` - Maximum deviation of table normal from straight up.
-  ``min_side_ratio`` - Minimum ratio of shortest side divided by
   longest side.
-  ``min_area`` - Minimum area of table plane.



Original page: https://github.com/strands-project/strands_tabletop_perception/blob/hydro-devel/table_detection/README.md
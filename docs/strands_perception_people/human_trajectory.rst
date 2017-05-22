Human Trajectory
================

This is a ROS package that extracts human poses information from people
tracker and stitches each pose for each human together. This package can
be run online by subscribing to /people\_tracker/positions or offline by
retrieving human poses from either perception\_people collection or
people\_trajectory collection.

Run this package by typing

::

    roslaunch human_trajectory human_trajectory.launch

The online stitching provides both mini batch trajectories messages
where trajectories are split into chunked and complete batch
trajectories which only publishes complete trajectory messages when the
persons are not detected anymore.

Parameters
----------

-  ``with_logging_manager``: the option (true/false) to subscribe to
   logging manager and get permission to store obtained data
-  ``path_visualisation``: the option to visualise each detected
   trajectory in rviz using Path. However, it only works for online
   construction.
-  ``online_construction``: the option (true/false) to stitch human
   poses online from other packages (bayes\_people\_tracker) or offline
   from perception\_people or people\_trajectory collection in mongodb.
-  ``tracker_topic``: the name of the people tracker topic, default is
   /people\_tracker/positions
-  ``logging_manager_topic``: the name of the logging manager topic,
   default is /logging\_manager/log\_stamped

Note
----

The offline retrieval limits the number of trajectories obtained from
mongodb to 10000 trajectories. To work around the limitation,
OfflineTrajectories class provides a query that can be passed to mongodb
to obtain specific trajectories.

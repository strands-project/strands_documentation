Human aware velocities
======================

This package adjusts the velocity of the robot in the presence of
humans.

Human aware navigation
----------------------

This node sets a navigation target and adjusts the velocity
move\_base/DWAPlannerROS uses to move the robot to a goal. This is
achieved by using the dynamic reconfigure callback of the DWAPlannerROS
to set the ``max_vel_x``, ``max_rot_vel``, and ``max_trans_vel``
according to the distance of the robot to the closest human. As a
consequence the robot will not be able to move linear or angular if a
human is too close and will graduately slow down when approaching
humans. The rotation speed is only adjusted to prevent the robot from
spinning in place when not being able to move forward because this
behaviour was observed even if the clearing rotation recovery behaviour
is turnd off.

This is implemented as an action server.

Parameters
~~~~~~~~~~

-  ``pedestrian_locations`` *Default:
   /pedestrian*\ localisation/localisations\_: The topic on which the
   actual pedestrian locations are published by the pedestrian
   localisation package (bayes\_people\_tracker/PeopleTracker).
-  ``/human_aware_navigation/max_dist`` *Default: 5.0*: maximum distance
   in metres to a human before altering the speed.
-  ``/human_aware_navigation/min_dist`` *Default: 1.2*: minimum distance
   in metres to a human. Robot stops at that distance.
-  ``/human_aware_navigation/timeout`` *Default: 5.0*: time in seconds
   after which speed is reseted if no human is detected any more.

Running
~~~~~~~

::

    rosrun strands_human_aware_velocity human_aware_planner_velocity.py

To start the actual functionality you have to use the actionlib client
architecture, e.g.
``rosrun actionlib axclient.py /human_aware_planner_velocities`` \* goal
type: move\_base/MoveBaseGoal

Human aware cmd\_vel
--------------------

A node to adjust the velocity of the robot by taking the /cmd\_vel topic
and republishing it. In order for this to work you have to remap the
/cmd\_vel output of your node or navigation stack to the input topic of
this node. It relies on the output of the
strands\_pedestrian\_localisation package to provide the actual position
of humans in the vicinity of the robot.

Parameters
~~~~~~~~~~

-  ``pedestrian_location`` *Default:
   /pedestrian*\ localisation/localisations\_: The topic on which the
   actual pedestrian locations are published by the pedestrian
   localisation package (bayes\_people\_tracker/PeopleTracker).
-  ``cmd_vel_in`` *Default: /human*\ aware\_cmd\_vel/input/cmd\_vel\_:
   The topic to which the original /cmd\_vel should be published.
-  ``cmd_vel_out`` *Default: /cmd*\ vel\_: The modified /cmd\_vel.
-  ``threshold`` *Default: 3*: Threshold in seconds to determine which
   person detections from the cache are too old to use.
-  ``max_speed`` *Default: 0.7*: The maximum speed the robot should
   achiev.
-  ``max_dist`` *Default: 5.0*: The distance at which the node starts
   taking detections of humans into account.
-  ``min_dist`` *Default: 1.5*: The cmd\_vel will be 0.0 if there is a
   person closer to the robot than this.

Running
~~~~~~~

::

    rosrun strands_human_aware_velocity human_aware_cmd_vel [_parameter:=value]



Original page: https://github.com/strands-project/strands_hri/blob/hydro-devel/strands_human_aware_navigation/README.md
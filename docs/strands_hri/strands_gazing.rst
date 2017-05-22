Strands gazing package
======================

Since gazing is one important part of human-robot interaction this
package will provide general applications to perform gazing behaviours.

Gaze at pose
------------

This node takes a given ``geometry_msgs/PoseStamped`` and moves the head
to gaze at this position. This is implemented as an action server.

Parameters
~~~~~~~~~~

-  ``head_pose`` *Default: /head/commanded*\ state\_: The topic to which
   the joint state messages for the head position are published.
-  ``head_frame`` *Default: /head*\ base\_frame\_: The target coordinate
   frame.

Running
~~~~~~~

::

    rosrun strands_gazing gaze_at_pose [_parameter:=value]

To start the actual gazing you have to use the actionlib client
architecture, e.g. ``rosrun actionlib axclient.py /gaze_at_pose`` \*
goal \* ``int32 runtime_sec``: The time the gazing should be executed in
seconds. Set to 0 for infinit run time (has to be cancelled to stop).
*Cancelling a goal will trigger the head to move to the zero position.*
\* ``topic_name``: The name of the topic on which to listen for the
poses. Currently: ``/move_base/current_goal`` and
``/upper_body_detector/closest_bounding_box_centre`` but really
everything that poblishes a stamped pose can be used. \* result \*
``bool expired``: true if run time is up, false if cancelled. \*
feedback \* ``float32 remaining_time``: The remaining run time. \*
``geometry_msgs/Pose target``: The pose at which the robot currently
gazes.

Notes
~~~~~

Since some of the topics that publish a PoseStamped do this only once,
e.g. ``/move_base/current_goal``, the transformation runs a infinite
loop. This means that move\_base publishes the pose once and inside the
look the transform will run for the updated robot position with the
received pose from move\_base. As soon as a new pose is received the
transformloop will use this one to calculate the transform. This still
runs in real time but accounts for nodes that are lazy publishers.

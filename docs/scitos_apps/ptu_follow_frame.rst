ptu\_follow\_frame
==================

This package provides a ROS node that controls the PTU so as to keep the
``ptu_mount`` frame X axis pointing to the origin of a user supplied TF
frame.

It is activated and deactivated using two service calls:

-  ``/ptu_follow_frame/set_following : ptu_follow_frame/StartFollowing``
   call this with a string representation of the target frame, for
   example ``map`` to have the ptu frame follower track that frame.
-  ``/ptu_follow_frame/stop_following : std_srv/Empty`` call this to
   stop the ptu frame follower from tracking whatever frame it currently
   tracks.

During tracking, the PTU will be in velocity control mode and no other
node should try to control it.

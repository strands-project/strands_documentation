many segment :D
===============

For the semantic segmentation service:
``roslaunch semantic_segmentation semantic_segmentation_integrate.launch``

A dummy client to test it:
``rosrun semantic_segmentation dummy_client <waypoint_name>``

TODO:
=====

ASAP: \* Update service to take waypoint \* Query center from Rares \*
Fix flipping of normals \* Play around with rotations and flipping \*
Try neighborhood features! (Normals, psl, color,) \* Store labeled
pointclouds and make a latched topic for publishing them.

POST REV: \* Merge the two cmakelists files! \* Think about a cleaner
config file handling \* Pull back other data again?

DONE?: \* Fix up label set.

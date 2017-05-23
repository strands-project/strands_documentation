Human Trajectory
================

This is a ROS package that classifies human poses from
bayes\_people\_tracker\_logging in mongodb into human movements or
non-human movements. The classification is based on poses and velocity
of poses which are applied to KNN classifier. This package can only be
run offline retrieving human poses from perception\_people

Run this package by typing

::

    rosrun human_movement_identifier classifier.py [train_ratio] [accuracy (1/0)]

where ``[train_ratio]`` is the training data ratio between 0.0 and 1.0.
Setting 0.9 makes 0.1 of all data will be used as test data.
``[accuracy]`` is the option to choose between knowing the accuracy of
this classifier (1) or just wanting to test data from test data.


Original page: https://github.com/strands-project/trajectory_behaviours/blob/master/human_trajectory_classifier/README.md
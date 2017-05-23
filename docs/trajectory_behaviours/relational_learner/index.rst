Relational Learner
==================

A ROS package that uses qualitative spatio-temporal relations to learn
and classify human trajectories as statistically novel or not.

Prerequisites
-------------

-  roscore
-  mongodb\_store
-  strands\_perception\_people
-  soma\_trajectory
-  qsrlib

Getting started
---------------

1. Run mongodb datacentres:
   ``$ roslaunch mongodb_store mongodb_store.launch db_path:= <path>     $ roslaunch mongodb_store mongodb_store.launch db_path:=/home/strands/mongodb_store/bham_trajectory_store/``
   where ``path`` specifies the path to your mongodb\_store

Also run the mongodb robot pose logging tool:
``$ rosrun mongodb_log mongodb_log.py /robot_pose``

2. Make sure people perception is running to publish detected
   trajectories:
   ``$ roslaunch perception_people_launch people_tracker_robot.launch``

3. Also run the online-trajectory stiching tool:
   ``$ rosrun human_trajectory trajectory_publisher.py [publish_interval][online(1)/offline(0)]``
   see
   `here <https://github.com/strands-project/trajectory_behaviours/tree/master/human_trajectory_classifier>`__
   for more details.

Alternatively to step 2 and 3, you can run ``soma_trajectory`` and
obtain test trajectories from mongodb store:
``$ rosrun soma_trajectory trajectory_query_service.py``

4. Make sure the QSRLib Service is running:
   ``$ rosrun qsr_lib qsrlib_ros_server.py``

5. Run the Episodes Service:
   ``$ rosrun relational_learner episode_server.py``

6. Run the Novelty Service:

   ::

       $ rosrun relational_learner novelty_server.py

7. Run the Episodes node:
   ``$ rosrun relational_learner episodes_client.py``

8. Run Novelty node: ``$ rosrun relational_learner novelty_client.py``

Note:
-----

This package can be run offline by running ``soma_trajectory`` in step 2
and 3 instead of ``people_perception``. In this case, step 7 becomes:
``$ rosrun relational_learner episodes_client_OT.py``

which queries one region's trajectories from mongodb\_store instead of
subscribing to published trajectories.


Original page: https://github.com/strands-project/trajectory_behaviours/blob/master/relational_learner/README.md
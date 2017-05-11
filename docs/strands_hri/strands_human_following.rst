Package Description
===================

This package contains simple human following

The main function of this package is making the robot follow humans
based on the information from passive people detection.

The State Machine inside the package contains:

Start stage - Wandering stage - Following stage - Local-searching stage

Getting Start
=============

Before you can launch this package, you need:

::

    roscore
    strands robot bringup 
    strands robot camera
    strands ui
    strands navigation
    perception people tracker

To start this module, simply launch:

::

    roslaunch strands_human_following simple_follow.launch [wandering_mode, config_file]
    rosrun strands_human_following simple_follow_client.py

There are two parameters that can be changed: \* wandering\_mode [wait,
normal] with wait as default \* config\_file where the configuration of
this module is stored. It is stored in
/strands\_hri/strands\_human\_following/conf/default.yaml by default

Configurations
==============

To change the settings of this package, find:

::

    /strands_hri/strands_human_following/conf/default.yaml

Parameters you can change are listed below:

::

    wander_area            : (polygon)
    follow_area            : (polygon)
    max_t_frames(tolerence): (int)
    alpha                  : (double)
    distance(safe distance): (double)

Wander area is the area where the robot will wander around when there is
no person detected. Follow area is the area where the robot will follow
a person; The robot will not follow outside the follow area even when
there are persons detected. Both wander area and follow area are polygon
which are defined by points [x,y].

Max\_t\_frames is the maximum frames where the robot searches a person
after it loses the person. Alpha is the factor of how far the pan tilt
unit rotates when the robot follows a person. Distance is the distance
between the robot and a person when the robot follows the person.

Tasks and Routines
==================

There is an example called routine\_example.py of how to create a task
and add it to scheduler. First of all,

::

    roslaunch task_executor task-scheduler.launch

must be up and running. Create the task as follows:

::

    task = Task(start_node_id=[WayPoint], max_duration=[DurationOfTheTask], action='simple_follow')

    task_utils.add_int_argument(task, [DurationOfHumanFollowing])

Task\_utils is needed since SimpleFollow.action has one integer argument
to determine how long the human following runs.

Problems
========

Can not catch up with human's normal pace.

Can not follow when people walk towards or pass by the robot.

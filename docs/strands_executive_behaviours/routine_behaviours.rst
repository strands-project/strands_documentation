Routine Behaviours
==================

Overview
--------

This package provides tools to generate long-term routine behaviours for
mobile robots. The
`RobotRoutine <http://strands-project.github.io/strands_executive_behaviours/routine_behaviours/html/classroutine__behaviours_1_1robot__routine_1_1RobotRoutine.html>`__
class in this package provides facilities for extending the
`strands\_executive/task\_routine <https://github.com/strands-project/strands_executive/blob/hydro-release/README.md#creating-a-routine>`__
with useful runtime behaviours.

API documentation:
http://strands-project.github.io/strands_executive_behaviours/routine_behaviours/html

Idle Behaviours
~~~~~~~~~~~~~~~

When the robot is inactive for a configurable amount of time, with
sufficient battery charge, the methods
`RobotRoutine.on\_idle() <http://strands-project.github.io/strands_executive_behaviours/routine_behaviours/html/classroutine__behaviours_1_1robot__routine_1_1RobotRoutine.html#ab43e703d3745fab4ec8fab1053f91fe0>`__
is called. Overriding this method allows you to generate specific
behaviour when the robot is idle. For example
`PatrolRoutine.on\_idle() <http://strands-project.github.io/strands_executive_behaviours/routine_behaviours/html/classroutine__behaviours_1_1patrol__routine_1_1PatrolRoutine.html#ab93069ea912aa072520d33f6fdf670fa>`__
moves the robot to random node when idle.

Night Behaviours
~~~~~~~~~~~~~~~~

When the robot's routine for the day is complete, we assume that the
robot is then parked at a charging station. As the routine is complete,
tasks which are scheduled as part of the normal routine are not sent to
the robot. To provide tasks which are executed by the robot overnight,
you can use
`RobotRoutine.add\_night\_task <http://strands-project.github.io/strands_executive_behaviours/routine_behaviours/html/classroutine__behaviours_1_1robot__routine_1_1RobotRoutine.html#a0c405cb08cac81f6f3905f1897b4bb8a>`__.
This adds a task which will be sent for execution every night after the
routine finishes. These tasks cannot involve movement and therefore must
either have an empty ``start_node_id`` or be performed at the charging
station. A system can have multiple night tasks, but currently no
checking is done to ensure the night tasks fit within the time available
between the end of one routine day and the start of the next.


Original page: https://github.com/strands-project/strands_executive_behaviours/blob/hydro-devel/routine_behaviours/README.md
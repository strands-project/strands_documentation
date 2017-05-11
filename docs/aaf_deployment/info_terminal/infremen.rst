Overview
========

The **Infremen** package contains a waypoint proposer for the **Info
Terminal**. The tries to establish the probabilities of people presence
at the individual waypoints and times and use this information to
navigate to these waypoints when people are likely to be present.

Every midnight, it processes the information about the interactions it
achieved during the day and creates dynamic probabilistic models of
people presence at the individual waypoints. These models are then used
to create a *schedule* that determines at which waypoints and times the
robot offers its *Info Terminal* service.

Practical
=========

You can edit the schedule manually.

Parameters
----------

The **collectionName** determines what name will be used when saving and
retrieving interaction history from the *monngodb*. The
**scheduleDirectory** determines the place to store text files with the
schedules.

Dynamically reconfigurable parameters
-------------------------------------

The **explorationRatio** determines the balance between exploration
(trying to establish the probabilitic functions of people presence) and
exploitation (trying to meet people to actually interact). If the
battery level drops below the **minimalBatteryLevel**, the robot will go
and recharge itself. The robot will not leave the waypoint if there was
an interaction during the last **interationTimeout** seconds. The
**taskDuration** determines how long the robot waits for an interaction.
The **maxTaskNumber** sets how much *Info Terminal* tasks are maintained
at the same time. Setting **maxTaskNumber** causes the *Infremen* to
stop proposing tasks.

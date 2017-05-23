roslaunch\_axserver: Running roslaunch files via the actionlib interface
========================================================================

goal definition
---------------

This component allows to launch ROS launch files via an actionlib
server. A simple goal (of type ``launchServerGoal``) would look like
this:

::

    pkg: 'strands_morse'
    launch_file: 'uol_mht_nav2d.launch'
    monitored_topics: ['/map']

this would launch the launch file ``uol_mht_nav2d.launch`` in package
``strands_morse``.

monitoring the roslaunch process
--------------------------------

The action server implements a monitor thread that will provide feedback
on the actionlib feedback channel as a boolean (parameter ``ready`` in
the feedback), indicating if *all* the topics given via
``monitored_topics`` (in the example above just one: ``/map``) are
actually advertised. This allows to wait until all components have been
launched. If ``monitored_topics`` is empty, the feedback is always
``ready=True``.

state transitions
-----------------

The goal status will be set ACTIVE when it was possible to launch a
roslaunch process (and will be REJECTED if this was not possible). If
the roslaunch process terminates with an error (e.g. when the given
roslaunch file doesn't exist), the goal is set to ABORTED. If the
roslaunch process terminates successfully, then the goal is set to
SUCCESS (usually, we will never see this, as the roslaunch process will
likely be running until we actively preempt it).

using in Python
---------------

In order to use this in your code, include something like the following
in your python code:

::

    import rospy
    import roslaunch_axserver.msg
    import actionlib

    ...

        client = actionlib.SimpleActionClient('launchServer', roslaunch_axserver.msg.launchAction)

        # Waits until the action server has started up and started
        # listening for goals.
        client.wait_for_server()

        # Creates a goal to send to the action server.
        goal = roslaunch_axserver.msg.launchGoal(pkg='pkg', launch_file='filename', monitored_topics=[])

        # Sends the goal to the action server.
        client.send_goal(goal)

The server is reentrant, meaning that you can run several roslaunch
processes in parallel (*not* a ``SimpleActionServer``)


Original page: https://github.com/strands-project/strands_apps/blob/indigo-devel/roslaunch_axserver/README.md
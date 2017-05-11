Exercise 2
==========

In this exercise you will use our MDP/LTL planning framework to get the
robot to perform 3D mapping sweeps of a simple. This example connects
many of the different elements of our robot system, and may seem complex
at first. If something is unclear, or you want more information, please
just ask.

Background
==========

You must first run some basic elements from the STRANDS system. You
should ideally run each of these in a separate terminal where you have
sourced both the ROS and your local workspace ``setup.bash`` files, as
described in `tutorial\_prep.md <./tutorial_prep.md>`__.

MongoDB Store
-------------

(If you still have the database running from `Exercise
1 <./exercise_1.md>`__ you can skip this step)

First, check the ``db`` directory exists (which you should've created
following `tutorial\_prep.md <./tutorial_prep.md>`__). The following
should not list any files or report an error:

.. code:: bash

    ls `rospack find planning_tutorial`/db

If that is ok, then launch
`mongodb\_store <http://wiki.ros.org/mongodb_store>`__ using that
directory as its data path:

.. code:: bash

    roslaunch mongodb_store mongodb_store.launch db_path:=`rospack find planning_tutorial`/db

MORSE Simulation
----------------

In another terminal, launch our object simulation taken from the `ALOOF
Project <http://www.dis.uniroma1.it/~aloof/>`__.

.. code:: bash

    roslaunch strands_morse aloof_morse.launch 

If you press the 'h' key in MORSE you can see a list of available
keyboard commands.

2D and Topological Navigation
-----------------------------

We have predefined a simple topological map for you to use in this
tutorial. The first time (and only the first time!) you want to use
topological navigation in the ALOOF simulation, you must add this map to
the mongodb store. Do it with the following command:

.. code:: bash

    rosrun topological_utils load_yaml_map.py `rospack find strands_morse`/aloof/maps/aloof_top_map.yaml

You can check the result of this with the following command which should
print a description of the topological map ``aloof``.

::

    rosrun topological_utils list_maps 

If this was successful you can launch the 2D (amcl and move\_base) and
topological localisation and navigation for your simulated robot. Note
that in this configuration, the statistics for edge transitions in the
topological map will be learnt from experience (as opposed to manually
specified as in `Exercise 1 <./exercise_1.md>`__).

.. code:: bash

    roslaunch strands_morse aloof_navigation.launch

To see everything running, launch the ROS visualisation tool ``rviz``
with the provided config file:

.. code:: bash

    rviz -d `rospack find planning_tutorial`/plan_tut.rviz

You'll find that the robot is not localised at the correct place
compared to the simulation. Therefore use the ``2D Pose Estimate``
button and click (then hold and rotate to set angle) on the correct part
of the map.

If you click on a green arrow in a topological node, the robot should
start working its way there. Feel free to add whatever extra
visualisation parts you want to this (or ask us what the various bits
are if you're new to robotics).

MDP Planning
------------

Next launch the MDP-based task executive system in (yet another!) new
terminal:

.. code:: bash

    roslaunch mdp_plan_exec mdp_plan_exec_extended.launch

3D Mapping Nodes
----------------

Our 3D mapping framework makes use of an approach called *meta-rooms*
which builds 3D maps at waypoints in the environment. Before you run
this for the first time you need to create somewhere for the system to
store maps. Do this with the following command:

.. code:: bash

    mkdir ~/.semanticMap

If this was successful, you can launch the meta-room nodes with the
following command:

.. code:: bash

    roslaunch planning_tutorial meta_rooms.launch

Exercise 2a
===========

In `Exercise 1 <./exercise_1.md>`__ you exploited the fact that the
execution framework automatically creates an MDP for navigation across
the topological map. In this exercise we will extend this MDP with
additional actions which connect ROS `actionlib
servers <http://wiki.ros.org/actionlib>`__ to actions in the MDP.

In this part we will walk through an example where the outcome of the
invocation of an action server is tied to a non-deterministic outcome of
an action in an MDP. After showing you how to do this, the next step
will be for you to edit the file to change how the action is encoded in
the MDP.

All of the code for this part of the exercise is in
``planning_tutorial/script/sweep_at_waypoints.py`` so only the important
fragments will be included here.

The task we will undertake is to trigger the ``/do_sweep`` action server
with the argument ``medium`` (signifying the number of views to take in
the sweep) at a set of waypoints in the topological map. The key idea is
that we associate the action server with an MDP action which we add to
the navigation MDP. To make sure we only complete the action once, we
connect the successful completion of this action to a state variable in
our MDP specification, which can be used in pre- and post-conditions for
our action.

We start by creating a name for our action. As we care about the success
of an action at a waypoint, we need a different action for each
waypoint. This is captured in the naming of the action, which should be
different for each waypoint, i.e.

.. code:: python

        action_name = 'do_sweep_at_' + waypoint  

Next we create a the MDP state variable for tracking the success of the
action. This state variable will form part of our goal statement, e.g.
if we have the state variable ``executed_do_sweep_at_WayPoint1`` the
goal to eventually make this true would be
``(F executed_do_sweep_at_WayPoint1=1)``.

.. code:: python

        state_var_name = 'executed_' + action_name
        # Create the state var object, initialise to 0 (false)
        state_var = MdpStateVar(name = state_var_name, init_val = 0, min_range = 0, max_range = 1) 

Following this we need to encode the possible outcomes of the action and
the way they can change the state in the MDP. Although there is no
restriction on the number of outcomes an action can have (over one), we
will use two: succeeded or not succeeded. The ``/do_sweep`` action
reports its outcomes when it completes, so we will use this return
signal to tell the MDP which outcome occurred (allowing it to update its
internal state correctly). Each outcome has a probability of occurring
(which is used when creating a policy to solve the MDP), and a
probability distribution over how long it might take to reach the
outcome. In this example we make up these values, but in our full system
we can learn them from experience at execution time.

.. code:: python

        successful_outcome = MdpActionOutcome(
                    # the probability of this outcome occurring
                    probability = 0.99,
                    # the effects of this action on the MDP state, in this case setting the state variable to 1
                    post_conds = [StringIntPair(string_data = state_var_name, int_data = 1)],
                    # how long it will take to reach this outcome, and with what probability
                    duration_probs = [1.0],
                    durations = [240.0], 
                    # And the action server outcome which will tell us if this outcome occurred. In this case if the action server returns with SUCCEEDED 
                    status = [GoalStatus(status = GoalStatus.SUCCEEDED)])

Below is a similar encoding for the unsuccessful outcome, i.e. the cases
where the action server reports that it has aborted or was preempted.

.. code:: python

        unsuccessful_outcome = MdpActionOutcome(probability = (1 - successful_outcome.probability),
                    post_conds = [StringIntPair(string_data = state_var_name, int_data = 0)],
                    duration_probs = [1.0],
                    durations = [120.0],               
                    status = [GoalStatus(status = GoalStatus.ABORTED), GoalStatus(status = GoalStatus.PREEMPTED)])

The final step is to link the MDP action to the actionlib server. This
is done in the code below. The ``action_server`` argument is used to
configure the action server client, and the ``add_string_argument`` call
is used to embed the parameters for the call into the action itself (see
``strands_executive_msgs.mdp_action_utils`` for more options).

.. code:: python

        # Finally we tie all this together to an actionlib server
        action = MdpAction(name=action_name,
                # This is the actual action server topic to be used 
                action_server='/do_sweep', 
                # The action will only be attemped if the preconditions are satisfied. In this case we can't have succeeded in the action before 
                pre_conds=[StringIntPair(string_data=state_var_name, int_data=0)],
                # These are the possible outcomes we defined above
                outcomes=[successful_outcome, unsuccessful_outcome],
                # And this is where we can execute the action. 
                waypoints = [waypoint])
        add_string_argument(action, 'medium')

For the purposes of the tutorial you should understand the overall
approach we are taking for this, and be able to map this understanding
into the code. To see it working you can run:

.. code:: bash

    rosrun planning_tutorial sweep_at_waypoints.py

Feel free to edit the code as you wish and play around with the file.
You could add more waypoints to the list, or add additional LTL
navigation goals (as in `Exercise 1 <./exercise_1.md>`__) to the string
``mdp_spec.ltl_task`` to change the robot's behaviour (e.g. get it to do
a sweep without every visiting a given waypoint).

Exercise 2b
===========

To successfully complete the following you need to be competent with
both Python and ROS. If you're not comfortable with these, please pair
up with someone who is.

To test your understanding, create a copy of
``planning_tutorial sweep_at_waypoints.py`` and re-write it such that
instead of completing a sweep at every waypoint, the problem is to
simply complete a single sweep at any point at the map. However you
should be able to specify that the chance of the action succeeding is
different at different waypoints (with you inventing the numbers), and
this should result in the robot choosing the waypoint with the highest
chance of success for the sweep.

Exercise 2c
===========

What happens when you combine your answer to 2b with the ability to
change the probabilities of success on the edges of the topological map?
Talk to one of the lecturers for help with getting this running if you
want to try it.

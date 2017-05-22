Exercise 3 - UNFINISHED
=======================

In this exercise you will use our MDP/LTL planning framework to encode
an object search task in a simple environment. This example connects
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

Semantic Map
------------

Our object search framework makes use of a semantic map of the
environment to know where to look for objects. There is a predefined map
in this repository. Before you run the semantic mapping launch file for
the first time, load the predefined map into mongodb with the following
command.

.. code:: bash

    mkdir ~/.semanticMap
    mongorestore --port 62345 `rospack find planning_tutorial`/maps/soma_dump

If this was successful, you can launch the semantic map nodes with the
following command:

.. code:: bash

    roslaunch planning_tutorial aloof_semantic_map.launch

After you've done this you should see some blue and yellow regions
appear in RViz.

Exercise 2a
===========

In `Exercise 1 <./exercise_1.md>`__ you exploited the fact that the
execution framework automatically creates an MDP for navigation across
the topological map. In this exercise we will extend this MDP with
additional actions which connect ROS `actionlib
servers <http://wiki.ros.org/actionlib>`__ to actions in the MDP.

In order for the robot to search for objects, it first needs to execute
a *meta-room sweep* in each room where it may need to look. This allows
it to build a 3D map of each room for reasoning about supporting
surfaces and views.

We connect the

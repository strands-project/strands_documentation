Exercise 1
==========

In this first exercise you will use our MDP/LTL planning framework to
make the robot drive around the map, and also play with the edges of the
underlying map to see how different long-term robot experiences
influence its behaviour when creating navigation policies.

Background
==========

You must first run some basic elements from the STRANDS system. You
should ideally run each of these in a separate terminal where you have
sourced both the ROS and your local workspace ``setup.bash`` files, as
described in `tutorial\_prep.md <./tutorial_prep.md>`__.

MongoDB Store
-------------

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

In another terminal, launch our simplified simulation of the `Transport
Systems Catapult <http://ts.catapult.org.uk>`__ (TSC).

.. code:: bash

    roslaunch strands_morse tsc_morse.launch 

If you press the 'h' key in MORSE you can see a list of available
keyboard commands.

2D and Topological Navigation
-----------------------------

We have predefined a simple topological map for you to use in this
tutorial. The first time (and only the first time!) you want to use
topological navigation in the TSC simulation, you must add this map to
the mongodb store. Do it with the following command:

.. code:: bash

    rosrun topological_utils load_yaml_map.py `rospack find planning_tutorial`/maps/plan_tut_top_map.yaml

You can check the result of this with the following command which should
print a description of the topological map ``plan_tut``.

::

    rosrun topological_utils list_maps 

If this was successful you can launch the 2D (amcl and move\_base) and
topological localisation and navigation for your simulated robot.

.. code:: bash

    roslaunch planning_tutorial tsc_navigation.launch

To see everything running, launch the ROS visualisation tool ``rviz``
with the provided config file:

.. code:: bash

    rviz -d `rospack find planning_tutorial`/plan_tut.rviz

If you click on a green arrow in a topological node, the robot should
start working its way there. Feel free to add whatever extra
visualisation parts you want to this (or ask us what the various bits
are if you're new to robotics).

Edge Prediction and MDP Planning
--------------------------------

For this tutorial we're going to interfere with the expected duration
and success probabilities for navigating edges in the topological map.
Usually these are computed from data gathered as navigation happens, but
for now we're going to fix them. To launch a node which reports fixed
predictions for map edges, do the following in a new terminal (the
argument is the file which contains the values to be reported):

.. code:: bash

    rosrun topological_navigation manual_edge_predictions.py `rospack find planning_tutorial`/maps/plan_tut_edges.yaml

Once this is running you can launch the MDP-based task executive system
in (yet another!) new terminal:

.. code:: bash

    roslaunch mdp_plan_exec mdp_plan_exec_extended.launch

Exercise 1a
===========

With all this up and running, you're now ready to give the robot some
tasks. For now we're only going to worry about navigation tasks, i.e.
reaching a node in the topological graph. If you open up the file
``$WS_ROOT_DIR/src/planning_tutorial/scripts/ltl_nav.py`` you will see
some code which creates an MDP task to achieve an LTL goal. You can
execute this file as follows:

.. code:: bash

    rosrun planning_tutorial ltl_nav.py

As this runs you should see the robot move around, as is appropriate for
the task (i.e. following the optimal policy given the edge predictions).
Parts of the policy are visualised as large arrows in rviz under the
``MarkerArray`` topic ``topological_edges_policies`` (this is part of
the preconfigured rviz file you launched above).

The important part of this file is the goal specification, i.e.:

.. code:: python

    goal_formula = '(F "WayPoint2")'

In this case ``F`` means "eventually" and ``"WayPoint2"`` stands for the
robot being at ``WayPoint2``. Try editing this formula to try more
complex goals involving other waypoints, LTL operators or Boolean
connectives. For inspiration, take a look at the list below:

-  ``goal_formula = '(F "WayPoint2") & (F "WayPoint7") '`` Eventually
   reach ``WayPoint2`` and eventually reach ``WayPoint7``. Choose best
   ordering to do so.

-  ``goal_formula = '(F "WayPoint2") | (F "WayPoint7") '`` Eventually
   reach ``WayPoint2`` or eventually reach ``WayPoint7``. Choose best
   one to visit considering your current position.

-  ``goal_formula = '(F ("WayPoint2" & (F "WayPoint7"))) '`` Eventually
   reach ``WayPoint2`` and eventually reach ``WayPoint7``. Choose best
   one to visit considering your current position.

-  ``goal_formula = '((!"WayPoint7") U "WayPoint5") '`` Avoid
   ``WayPoint7`` until you reach ``WayPoint5``. Compare this policy with
   the one obtained for ``'(F "WayPoint5") '``.

-  ``goal_formula = '(F ("WayPoint1" & (X "WayPoint2"))) '`` Eventually
   reach ``WayPoint1`` and immediately after (``X``) go to
   ``WayPoint2``. This allows us to "tell" the robot to navigate through
   some edges, e.g., for environmental exploration.

These specifications can also be connected using boolean connectives,
e.g.,
``'((!"WayPoint7") U "WayPoint5") ' &  (F ("WayPoint1" & (X "WayPoint2")))``.

Exercise 1b
===========

So far the robot is using the default, static edge durations and
probabilities which we provided earlier. Now we'll play with these
probabilities to observe the changes in the robot's behaviour. If you
kill the ``manual_edge_predictions.py`` node (``CTRL-c`` in it's
terminal) then edit the yaml file
``$WS_ROOT_DIR/src/planning_tutorial/maps/plan_tut_edges.yaml`` you can
alter the expected duration (in seconds) and the success probability of
each edge in the map. After you've made your edits, restart the node as
before and check if the robot creates policies which respect the new
edge information you provided.

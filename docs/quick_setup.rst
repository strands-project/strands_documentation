STRANDS quick setup
====================

These instructions get you into a strands system quickly, without doing any
custom setup. For custom setup you should look at the more detailed instructions
`here <setup.html>`__.

ROS and package setup
---------------------

Installing ROS
~~~~~~~~~~~~~~

The first step is to follow the instructions found at
http://wiki.ros.org/indigo/Installation/Ubuntu. The full install of ROS
with the package ``ros-indigo-desktop-full`` should contain all the
base ROS packages that are required.

Installing STRANDS packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install the strands packages, you should follow the instructions at
https://github.com/strands-project-releases/strands-releases/wiki.

Database
--------

Many of our packages rely on the
`mongodb\_store <http://wiki.ros.org/mongodb_store>`__ database package.
You therefore need to start this prior to the rest of the system. The
first time you run it, you need to create a directory to hold the data.
This can be shared across multiple systems, or you can use one for each
system you build.

One time setup, with ``$DATA_DIR`` being where you're storing your
databases:

.. code:: bash

    mkdir $DATA_DIR/strands_sim_example

Launch the database

.. code:: bash

    roslaunch mongodb_store mongodb_store.launch db_path:=$DATA_DIR/strands_sim_example

Topological Map Creation
------------------------

The STRANDS navigation system relies on continuous navigation (using
movebase) and higher-level topological navigation. We have already
created a topological map for the Birmingham simulation environment. You
add this to the database as follows (assuming you have already launched
``mongodb_store`` as above).

.. code:: bash

    rosrun topological_utils insert_map.py $(rospack find strands_morse)/bham/maps/cs_lg_sim.tplg cs_lg cs_lg

If you wish to create your own topological map, follow `the topological
navigation
README <https://github.com/strands-project/strands_navigation/tree/indigo-devel/topological_navigation>`__/

Simulation
----------

The following launches a simulation of a `SCITOS
A5 <http://metralabs.com/index.php?option=com_content&view=article&id=67&Itemid=66>`__
in the `MORSE simulator <http://www.openrobots.org/morse/>`__. The map
is based on the lower ground floor of the `School of Computer Science,
University of Birmingham <http://www.cs.bham.ac.uk>`__.

.. code:: bash

    roslaunch strands_morse bham_cs_morse.launch

Visual Docking
--------------

The robot docks on its charging station using a visual docking process.
This needs to be calibrated the first time you use the system. When you
launch the simulation, the robot should already be on the docking
station. From this position (and assuming the ``mongodb_store`` database
is running) do the following in two terminals. Launch the charging
nodes:

.. code:: bash

    roslaunch scitos_docking charging.launch

Then calibrate the docking software

.. code:: bash

    rosrun scitos_docking visual_charging_client calibrate 100

After this you can kill the ``charging.launch`` file as it will be
launched again later as part of the full system.

UI
--

The STRANDS system relies on a number of UI components to communicate
with the world (e.g. asking for help with navigation actions). Therefore
once you have the database running, launch the UI nodes:

.. code:: bash

    roslaunch strands_bringup strands_ui.launch

If you want to see what the UI is showing (which will be nothing yet),
open a browser at http://localhost:8090.

Navigation
----------

With the simulation, UI and database running, you can launch the strands
navigation system. This runs continuous and topological localisation and
navigation.

.. code:: bash

    roslaunch strands_bringup strands_navigation.launch map:=$(rospack find strands_morse)/bham/maps/cs_lg.yaml no_go_map:=$(rospack find strands_morse)/bham/maps/cs_lg.yaml topological_map:=cs_lg

If you open

::

    rviz -d `rospack find strands_morse`/bham/cs_lg.rviz

you should see the robot docked at the charging station, the laser, and
the topological map.

You can test that this is working by sending the robot to a topological
node, e.g.

.. code:: bash

    rosrun topological_navigation nav_client.py `WayPoint3`

Tasks
-----

The STRANDS system allows you to write *tasks* which the robot executes
at nodes in the topological map. For a detailed description of how this
works, see the documentation for the `strands\_executive
framework <https://github.com/strands-project/strands_executive/blob/hydro-release/README.md>`__.

Start the executive framework with

.. code:: bash

    roslaunch task_executor task-scheduler.launch

The simplest task is to wait somewhere for some time. The following
example script will add the task for the robot to wait at ``WayPoint7``
for 20 seconds:

.. code:: bash

    rosrun task_executor example_add_client.py WayPoint7 20

If you add multiple tasks the scheduler will optimise their order of
execution taking into account time windows and travel time.

Routine Behaviours
------------------

To create repetitive long-term behaviour, you can use a *routine*
script. One example of this is a patrol routine which visits every
waypoint in the environment in regular windows. The execution of the
following will start this process and trigger actions when the robot is
idle.

.. code:: bash

    rosrun routine_behaviours patroller_routine_node.py

You can still add tasks during routine execution and the scheduler will
fit them in as appropriate.



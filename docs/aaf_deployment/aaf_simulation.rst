aaf\_sim
========

This package contains files that are necessary for running STRANDS
simulations on the University of Lincoln environments.

Setting up Autonomous Patrolling Simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Calibrate charging station parameters:

-  Launch strands\_datacentre: \`\`\` roslaunch mongodb\_store
   mongodb\_store.launch db\_path:=/opt/strands/mongodb\_store

   ::

          ```

-  Launch simulation: \`\`\` roslaunch strands\_morse
   aaf\_sim\_morse.launch

   ::

          ```

-  Launch scitos\_docking: \`\`\` roslaunch scitos\_docking
   charging.launch

   ::

          ```

-  Drive the robot to the charging station
-  Calibrate charging parameters running: \`\`\` rosrun scitos\_docking
   visual\_charging\_client calibrate 100

   ::

          ```

2. Insert waypoints on database:

-  Launch strands\_datacentre: \`\`\` roslaunch mongodb\_store
   mongodb\_store.launch db\_path:=/opt/strands/mongodb\_store

   ::

          ```

-  Insert waypoints in DB \`\`\` rosrun topological\_utils
   insert\_map.py $(rospack find aaf\_simulation)/maps/aaf\_sim.tmap
   aaf\_sim aaf\_sim

   ::

          ```

   NOTE: You can also create your own topological map following the
   instructions on:
   https://github.com/strands-project/strands\_navigation/tree/hydro-devel/topological\_navigation

Launching Autonomous Patrolling Simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If all previous steps are done launch simulation by running:

::

       ```
       rosrun aaf_simulation start.sh

       ```


Overview
~~~~~~~~

The docking service detects and guides the robot to its charging
station. The service is based on detection of the 'o' letters of the
'ROBOT STATION' tag in the robot camera image. Prior to use, the method
has to establish the docking station reference frame relative to the
robot position.

To install
^^^^^^^^^^

Dependecies are: \* libgsl0-dev \* libblas-dev

``sudo apt-get install libgsl0-dev libblas-dev``

To setup:
^^^^^^^^^

1. Print the station tag on a A4 paper. Do not let the printer to resize
   it.
2. Center the robot at the charging station.
3. Display the robot camera image and fix the tag on the wall
   approximattelly in the image center.
4. Tell the system to measure its position relatively to the charger by
   calling a the calibration routine via actionlib. This can be done
   using a GUI as follows:

.. code:: bash

    rosrun actionlib axclient.py /chargingServer

Then in the ``Goal`` textfield complete as follows:

::

    Command: calibrate
    Timeout: 1000

And then press the ``SEND GOAL`` button.

The robot should move its eyelids to indicate progress of the
calibration process.

To use:
^^^^^^^

-  Just point the robot approximatelly in the direction of the charging
   station and call the node via actionlib as above, substituting
   ``charge`` for calibrate.
-  To leave the charging station, use ``undock`` instead.
-  Set the ``lightEBC`` parameter to the name of an EBC port you have
   attached a light to, e.g. ``Port0_12V_Enabled``.


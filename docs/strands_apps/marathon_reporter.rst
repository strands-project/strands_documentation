Overview
--------

This package provides a script to report marathon run attempts to the
STRANDS Robot Marathon webserver. The script monitors the robot's
odometry to find out how far the the robot has moved. Starting the
script signals the beginning of a run, ending the script finishes the
run.

Pre-requisites
~~~~~~~~~~~~~~

-  The robot needs to have internet access at the beginning of the run.
   This is so that it can close any outstanding previous attempts and
   request a new run key from the server.
-  The robot must publish odometry data as ``nav_msgs/Odometry``
   messages on the ``/odom`` topic.
-  The monogodb\_store must be running.
-  Your marathon teamname/password must be set in ``~/.marathon_auth``

Setting up ``.marathon_auth``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The team name and password supplied to you must be placed in the file
``~/.marathon_auth`` in the format:

::

    team: "your_team_name"
    password: "your_pa33w0rd"


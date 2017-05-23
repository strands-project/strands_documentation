scitos\_dashboard
=================

This package provides an rqt\_robot\_dashboard for the Scitos robot. The
dashboard displays motor and battery status, and allows the motors to be
stopped or free-run enabled.

Installation
------------

This should not require any additional packages to be installed...

Running
-------

On your off-robot pc:

::

    export ROS_MASTER_URI=http://bob:11311   # or not-bob
    rosrun scitos_dashboard scitos_dashboard

This brings up a small dashboard window, which is an rqt docking pane:

.. figure:: https://raw.github.com/cburbridge/scitos_apps/master/scitos_dashboard/doc/dash.png
   :alt: ScreenShot

   ScreenShot
From left to right, the widgets are: \* Diagnostics: this provides
information about the hardware of the robot - see
http://www.ros.org/wiki/robot\_monitor?distro=groovy for info. \* ROS
Console: provides a view of all ros console (INFO, DEBUG, WARN etc)
messages, with optional filters - see
http://www.ros.org/wiki/rqt\_console \* Motor Status: Clicking this
allows you to select free run, or stop the motors. If it is green, then
the robot is ok to drive but can't be pushed; if it is yellow then it is
in free run and can be pushed; if it is red then the motor stop is
enabled and must be reset before it can drive. \* Battery Status: This
shows the battery state as percentage in a tooltip, and changes icon
when plugged in. \* Robot Mileage in metres


Original page: https://github.com/strands-project/scitos_apps/blob/hydro-devel/scitos_dashboard/README.md
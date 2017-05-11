scitos\_pc\_monitor
===================

This package provides a node that monitors the health of the embedded
scitos pc. Status updates are published as diagnostics messages on
/diagnostics. These messages are collated by a diagnostics aggregator,
which then allows them to be viewed on the scitos\_dashboard.

Running
-------

The monitor is started automatically when you use scitos\_bringup. To
start independently (assuming a roscore is existing somewhere, ie from
scitos bringup):

::

    rosrun scitos_pc_monitor pc_monitor.py

This then sends publishes on /diagnostics. To make use of the
information, launch the diagnostics aggregator:

::

    roslaunch scitos_bringup diagnostic_agg.launch

and view the message on the dashboard on your of-board pc:

::

    rosrun scitos_dashboard scitos_dashboard.py

See
https://github.com/strands-project/scitos\_apps/tree/master/scitos\_dashboard
for dashboard documentation.

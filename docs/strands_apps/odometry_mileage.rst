Odometry Mileometre
~~~~~~~~~~~~~~~~~~~

This very simple node subscribes to ``/odom`` and calculates the
travelled distance since start in metres. The result is publish on
``/odom_mileage``.

Start with ``rosrun odomoetry_mileage odometry_mileage``

If the parametere ``saved_mileage`` is present on the rosparam server
(e.g. via the datacentre), then the node will use the stored mileage to
intialise itself. The node will also check against the actual
``/mileage`` topic on startup and will choose the large of both
(parameter or published value). The ``mileage`` topic might be actually
higher then the ``odom_mileage`` topic after restarting the robot
because at that point the mileage is read directly from the EEPROM and
the odometry\_mileage node might not have been running all the time when
the system crashes.

While the node is running the mileage parameter is constantly set to the
current value and saved to the datacentre. The default save interval is
every 500 odometry messages, which is every ~10 seconds. This can be
change via the ``save_interval`` parametre.


Original page: https://github.com/strands-project/strands_apps/blob/indigo-devel/odometry_mileage/README.md
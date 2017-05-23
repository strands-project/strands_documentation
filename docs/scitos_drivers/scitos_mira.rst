scitos\_mira
============

Scitos G5 drivers that interface ROS to MIRA.

Installation
------------

See [https://github.com/strands-project/strands\_systems]

Using the robot
---------------

Various aspects of the robot are exposed as ROS services, published
topics, subscribed topics and dynamic\_reconfigure parameters. These are
divided into 5 "modules": \* Drive - for the control of the motors. \*
EBC - for controlling the power for extra devices (pan tilt and
cameras). \* Head - for controlling the HRI head. \* Display - for the
small status display on the base. \* Charger - for battery monitoring
and charging control.

Drive
~~~~~

Published topics
^^^^^^^^^^^^^^^^

-  ``/odom (nav_msgs::Odometry)`` The odometric position of the robot
   (Odometry.pose), and it's linear/angular velocity
   (Odometry.twist.linear.x, Odometry.twist.angular.z). This is also
   published as a TF between ``/odom`` and ``/base_footprint_link``.
-  ``/bumper (std_msgs::Bool)`` State of the robots bumper, published
   regularly not only when the state changes.
-  ``/mileage (std_msgs::Float32)`` The distance in metres that the
   robot has travelled since the beginning of time.
-  ``/charger_status (scitos_msgs::ChargerStatus)`` Detailed information
   about the current status of the charging circuit.
-  ``/motor_status (scitos_msgs::MotorStatus)`` The state of the motors,
   free-run mode, emergency button status, bumer status.

Subscribed topics
^^^^^^^^^^^^^^^^^

-  ``/cmd_vel (geometry_msgs::Twist)`` Any velocity published on this
   topic will be sent to the robot motor controller. Twist.linear.x
   corresponds to the desired linear velocity; Twist.angular.z
   corresponds to the angular velocity.

Services
^^^^^^^^

-  ``/reset_motorstop (scitos_msgs::ResetMotorStop)`` This service is an
   empty request and empty response. It turns off the motor stop, which
   is engaged when the robot bumps into something. It can only be turned
   off if the robot is not longer in collision.
-  ``/reset_odometry (scitos_msgs::ResetOdometry)`` This empty
   request/response service sets the robot odometry to zero.
-  ``/emergency_stop (scitos_msgs::EmergencyStop)`` This empty
   request/response service stops the robot. It is equivalent to the
   bumper being pressed - the motor stop is engaged, and can be reset
   with /reset\_motorstop.
-  ``/enable_motors (scitos_msgs::EnableMotors)`` This service takes a
   ``std_msgs::Bool enabled`` in the request, and gives an empty
   response. Disabling the motors is the same as placing the robot into
   "Free Run" mode from the status display.

Head
~~~~

Published topics
^^^^^^^^^^^^^^^^

-  ``/head/actual_state (sensor_msgs::JointState)`` The actual joint
   states of the head. This topic is published at 30Hz, although I'm not
   sure what the actual frequency the hardware provides is.

Subscribed topics
^^^^^^^^^^^^^^^^^

-  ``/head/commanded_state (sensor_msgs::JointState)`` To control the
   robot's head position. There are 6 axis that can be controlled by
   placing the joint name in JointState.name and the desired state in
   JointState.position. The axis are:
-  ``HeadPan`` - the pan joint of the head; 0 to 360 degrees, with a
   block point at 90 degrees.
-  ``HeadTilt`` - the tilt of the head;
-  ``EyePan`` - the pan of the eyes, without moving the head.
-  ``EyeTilt`` - the tilt of the eyes, without moving the head.
-  ``EyeLidLeft`` - the state of the left eye lid, 0..100, 100 fully
   closed.
-  ``EyeLidRight`` - the state of the right eye lid, 0..100, 100 fully
   closed.

EBC
~~~

Reconfigure parameters
^^^^^^^^^^^^^^^^^^^^^^

-  ``Port0_5V_Enabled (bool)`` Is 5V enabled at port 0
-  ``Port0_5V_MaxCurrent (float)`` Max current for port 0 5V
-  ``Port0_12V_Enabled (bool)`` Is 12V enabled at port 0
-  ``Port0_12V_MaxCurrent (float)`` Max current for port 0 12V
-  ``Port0_24V_Enabled (bool)`` Is 24V enabled at port 0
-  ``Port0_24V_MaxCurrent (float)`` Max current for port 0 24V
-  ``Port1_5V_Enabled (bool)`` Is 5V enabled at port 1
-  ``Port1_5V_MaxCurrent (float)`` Max current for port 1 5V
-  ``Port1_12V_Enabled (bool)`` Is 12V enabled at port 1
-  ``Port1_12V_MaxCurrent (float)`` Max current for port 1 12V
-  ``Port1_24V_Enabled (bool)`` Is 24V enabled at port 1
-  ``Port1_24V_MaxCurrent (float)`` Max current for port 1 24V

Charger
~~~~~~~

Published topics
^^^^^^^^^^^^^^^^

-  ``/battery_state (scitos_msgs::BatteryState``
-  ``/charger_status (scitos_msgs::ChargerStatus``

Reconfigure parameters
^^^^^^^^^^^^^^^^^^^^^^

There are some parameters, but they currently not implemented for fear
of messing up...

Display
~~~~~~~

Published topics
^^^^^^^^^^^^^^^^

-  ``/user_menu_selected (std_msgs::Int8)`` This topic is published when
   one of the user sub-menus (as set using the dynamic reconfigure
   parameters) is selected. The value 0..3 indicates which menu item was
   "clicked".

Reconfigure parameters
^^^^^^^^^^^^^^^^^^^^^^

-  ``EnableUserMenu (string)`` Is the user menu entry in the status
   display enabled
-  ``UserMenuName (string)`` The name of the user menu entry in the main
   menu of the status display
-  ``UserMenuEntryName1 (string)`` The name of the first sub menu entry
   in the user menu of the status display
-  ``UserMenuEntryName2 (string)`` The name of the second sub menu entry
   in the user menu of the status display
-  ``UserMenuEntryName3 (string)`` The name of the third sub menu entry
   in the user menu of the status display



Original page: https://github.com/strands-project/scitos_drivers/blob/indigo-devel/scitos_mira/README.md
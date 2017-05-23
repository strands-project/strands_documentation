Topics to log:
==============

Ros message printouts (above warning priority):
-----------------------------------------------

-  ``/rosout``

Robot status:
-------------

-  ``/tf`` - The tf description
-  ``/robot_pose`` - Also in tf but might as well
-  ``/cmd_vel`` - Velocity sent to motors
-  ``/goal`` - Might be the move base goal
-  ``/mileage`` - Distance traveled
-  ``/motor_status`` - Is motor stop on? Free run etc.

-  ``/head/actual_state`` - Positions of eyes
-  ``/head/cmd_light_state`` - Eye lights
-  ``/head/commanded_state`` - Eye position commands?

-  ``/barrier_status`` - Magnetic strip?
-  ``/battery_state`` - Is charging, battery percentage etc.
-  ``/bumper`` - Is bumper pressed?
-  ``/charger_status`` - Charging status
-  ``/rfid`` - Magnetic strip etc.

-  ``/diagnostics`` - Network status, joystick driver status, PTU status
   etc.

-  ``/SetPTUState/goal`` - PTU position command
-  ``/ResetPtu/goal`` - PTU reset command

-  ``/EBC/parameter_updates`` - cfg changes of ebc
-  ``/Charger/parameter_updates`` - cfg changes of charger

Topological nav:
----------------

-  ``/topological_navigation/Route`` - current route through nodes
-  ``/topological_navigation/Statistics`` - statistics on top nav
   (already logged but might as well)

-  ``/current_node`` - current node in topo nav
-  ``/current_edge`` - current edge in topo nav
-  ``/closest_node`` - closest node in topo nav

Monitored nav:
--------------

-  ``/do_backtrack/goal`` - Command to do the backtrack recovery

Communication:
--------------

-  ``/speak/goal`` - mary tts speak command
-  ``/mary_tts/speak`` - same?

-  ``/strands_emails/goal`` - send email command
-  ``/strands_image_tweets/goal`` - send image tweet command

-  ``/pygame_player_negotiation`` - highest audio priority + node?

Docking servers:
----------------

-  ``/chargingServer/goal``
-  ``/chargingServer/result``
-  ``/chargingServer/cancel``

-  ``/docking/goal``
-  ``/docking/result``
-  ``/docking/cancel``

-  ``/undocking/goal``
-  ``/undocking/result``
-  ``/undocking/cancel``

Move base:
----------

-  ``/map_updates``

-  ``/move_base/NavfnROS/plan`` - local plan?
-  ``/move_base/current_goal`` - current goal
-  ``/move_base/DWAPlannerROS/global_plan`` - global plan
-  ``/move_base/DWAPlannerROS/local_plan`` - local plan
-  ``/move_base/goal`` - current goal

Routine related:
----------------

-  ``/wait_node/goal`` - Action goal for wait action
-  ``/wait_node/result``
-  ``/wait_node/cancel``

Already logged (won't be logged by this):
=========================================

Task executor:
--------------

-  ``/execute_policy_mode/Statistics`` - Scheduling stats, times etc?
-  ``/task_executor/events`` - ?
-  ``/current_schedule`` - Current schedule

Monitored nav:
--------------

-  ``/monitored_navigation/monitored_nav_event`` - (Already logged by
   Bruno?)
-  ``/monitored_navigation/srv_pause_requested`` - ?
-  ``/monitored_navigation/stuck_on_carpet`` - Stuck on carpet state
-  ``/monitored_navigation/pause_requested`` - Nav pause



Original page: https://github.com/strands-project/aaf_deployment/wiki/Topics-to-log-during-deployments
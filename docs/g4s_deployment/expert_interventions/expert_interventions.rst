-  Date: 03/06/2015
-  Expert name: Bruno Lacerda
-  Comments: Big hardware (motors) failure required for a full robot
   restart.
-  Failures:

   -  11h00: Robot stopped moving, because the motors stopped working.
      He was always in free run This was a low level issue, as even
      using the onboard menu to put him in free run / motor stop, didn't
      do anything. Required full robot restart

-  Restarts:

   -  13h30: Restarted the routine, after getting everything running
      again.e

--------------

-  Date: 26/05/2015
-  Expert name: Chris Burbridge
-  Comments: Undocked at 9am and went about a full day, ran down battery
   to 29% at 16h25 and demanded dock. Navigation SM got screwed, motor
   stop was on but no help screen. Turned off motor-stop. Still no
   movement. Navigation SM was stuck, restarted navigation. Robot docked
   at 16h55

--------------

-  Date: 21/05/2015
-  Expert name: Burbridge
-  Comments: replication still active in the morning, battery not
   charging right.
-  Failures: replication of metric maps takes too long, still active in
   the morning. battery only reached 78% over night, no action taken.
-  Restarts: 9:25 restarted routine having removed metric map
   replication, changed day to 9h00-16h45, increased learning durations.

--------------

-  Date: 20/05/2015
-  Expert name: Bruno Lacerda
-  Comments: bobl's disk was full in the morning, so there was some
   issues with replication. Chris and Nick solved it by doing stuff. The
   battery went below 30% earlier today, so he finished theday around
   15h30.
-  Failures: 10h00: Found that
   ``roslaunch singleview_object_recognizer recognition_service.launch``
   crashed sometime before. This has happened before and has something
   to do with a
   ``[pcl::KdTreeFLANN::setInputCloud] Cannot create a KDTree with an empty input cloud!``
   error.
-  Param sets: 10h15: Set the recognition service launchfile to respawn
   the node, trying to work around 10h00 failure.
-  Restarts: 10h30: Restarted the recognition\_service with respawn,
   along with the search nodes, to make sure they connect to the
   service.

--------------

-  Date: 19/05/2015
-  Expert name: Rares Ambrus
-  Comments: Fixed bug that was causing metric mapping data to be also
   saved in the .ros folder. Cleaned up .ros folder.
-  Restarts: restarted metric mapping process:
   ``roslaunch semantic_map_launcher semantic_map.launch``

--------------

-  Date: 18/05/2015
-  Expert name: Lars Kunze
-  Comments: Happy Monday: Bob docked off and started its routine
   without problems. 11:00 the parameter change does not work well with
   the topological layout (bob is described as being 'drunk' or 'loopy'
   . I change it back for now.
-  Failures : 11:00 default website is gone.
-  Param sets: changed sim\_time from 2.1 to 0.8 (dynamic reconfigure);
   11:00 change it back to 2.1.
-  Restarts: restarted perception (crashed on thursday); 11:35 restart
   of main gui; 12:00 restarted object search as it could not reconnect
   to perception;

--------------

-  Date: 15/05/2015
-  Expert name: Ferdian Jovan
-  Comments: Bob starts his day properly. He once bumped into a chair
   with someone sitting on it. He once bumped into a wall when his lost
   his current position (shown in navigation tab). I created videos for
   the review. First video is pan\_tilt\_metric\_map (taken at 12:15),
   Second video is learn\_object (taken at 12:28), Third video is
   door\_check (taken at 13:30), Fourth video is object\_search with
   navigation (taken at 15:20). Bob always moves from WP 3 to WP 6 via
   WP 5. Even though that path is longer than if he goes straight from 3
   to 6. Bob docked around 16:05 after the battery fell below 33%.
-  Failures:

   -  14h30: Bob could not speak to ask for help even though he showed
      that in the screen.

-  Param sets: Change the velocity speed of WP 3 to WP 5 from 0.35 to
   0.2.
-  Restarts:

   -  14h40: Restarted strands ui because mary was broken and Bob could
      not speak.

--------------

-  Date: 14/05/2015
-  Expert name: Lenka Mudrova
-  Comments: Bob wasnt using proper nogomap, ie. it planned impossible
   paths. Solved by restarting navigation and added a proper parameter
-  Failures:
-  Param sets: -
-  Restarts:
-  -12:00 navigation restarted, no change
-  -14:00 navigation restarted, no change -16h00: Restarted navigation
   and added the paramter with\_no\_go\_map:=true, as no go map was not
   used properly

\*Tweaking: Waypoint 32 moved little bit and waypoint next to Tracey's
desk as Bob was getting stuck there all day.

--------------

-  Date: 13/05/2015
-  Expert name: Lenka Mudrova
-  Comments: Search tab showed error
   ``IOError: [Errno 28] No space left on device``, but it didnt appear
   again
-  Failures:
-  Param sets: -
-  Restarts:
-  

   -  no restarts, only run
      ``rosrun soma_roi_manager soma_roi.py g4s g4s``

-  

   -  start this too:
      ``roslaunch singleview_object_recognizer recognition_service.launch models_dir:=/home/strands/lars_ws/tmp/STRANDS_MODELS/models training_dir_sift:=/home/strands/lars_ws/tmp/STRANDS_MODELS/sift_train recognizer_structure_sift:=/home/strands/lars_ws/tmp/STRANDS_MODELS/recognition_structure``

\*Tweaking: Waypoint 32 moved little bit and waypoint next to Tracey's
desk as Bob was getting stuck there all day.

--------------

-  Date: 12/05/2015
-  Expert name: Bruno Lacerda
-  Comments: Nothing to declare.
-  Failures:

   -  15h00: Recovery behaviours for monitored navigation were not reset
      properly. This lead to the robot being unable to recover from a
      kick I gave him, to stop him and show Tracy how to put him in
      free-run. This was solved by changing params manually (see below)

-  Param sets:

   -  11h30: Reduced speed between wp40 and wp44 to 0.15, as he was
      still failing there
   -  15h30: Reset the monitored nav params by hand, to recover from
      15h00 failure. Robot resumed doing his stuff.
   -  15h45: Set relaxed nav off, as all learning was done.
   -  17h10: Set charge threshold to 33 to force charge, and show Tracy
      what to check for.

-  Restarts:

   -  15h45: Restarted object learning action to make sure mon nav
      recovery states are reset to defaults, and avoid 15h00 failure in
      the future.

--------------

-  Date: 11/05/2015
-  Expert name: Bruno Lacerda
-  Comments: Pretty good day, Bob spent the whole day doing his stuff,
   except the time I killed everything to update roscpp (to fix memory
   leaks). He doesn't really need supervision any more, move base still
   fails more than it should, but he tends to either recover on his own,
   or get helped quickly, so I spent most of the day reading papers.
-  Failures:
-  Restarts:

   -  11h30: Restarted card checking server to change the speech to
      something clearer
   -  14h30: Updated roscpp (to fix memory leak) and restarted the whole
      system. robot was down for around 45min.
   -  16h35: Restarted card checking server to start listening to the
      card topic

-  Param sets:

   -  10h30: Changed object learns wps, one of them was at a door
      (wp14). put it inside the room (wp15).
   -  12h00: Changed top speed between wp40 and wp44 to 0.25 (in mongo),
      as the robot was failing that edge too much.
   -  15h15: Used rviz to change position of wp32, as it was too close
      to the door and the robot was getting stuck there once in a while.
   -  16h00: Set number of lunch object searches to 6.
   -  16h35: Rotated wp 12 to stop facing the office wall

--------------

-  Date: 08/05/2015
-  Expert name: Chris Burbridge
-  Comments: A great undock and morning, scheduling tasks and doing
   things well. Disappointing crash at the end of the day.
-  Failures:
-  at 16:10 robot\_pose stopped being published at 16:10, resulting in
   the need to restart navigation, executor and routine. This co-incided
   with opening rviz on the robot screen, and files being copied over
   ssh to a remote machine. At the time the memory usage was near 100%.
   After restarting these components it dropped to 60%. Memory usage is
   now being logged to a file /home/strans/process\_log.txt to analyse
   after a while.
-  the card reader task succeeded in driving to a person at 15:53, but
   the person swiped there card and it kept asking to identify them
   every 5 or so seconds. Even though the card reader is not integrated
   into the action, this should only ask once. Until the card reader is
   integrated I have created another node greets people by name when
   they present there card. (This was a real hit with people, including
   Dave..)
-  logged pointclouds look to contain a lot of red points. Need to
   investigate the source of this, maybe the pulling out of mongo into a
   .pcd file.
-  Restarts:
-  12:25 Stopped routine, 12:29 Ran bruno's parametrised routine
-  12:35 Stopped routine because of typo bug, 12:36 ran master branch
-  12:38 Stopped routine, 12:39 pulled and ran Bruno's branch; increased
   object learnings to 10/10 via parameter
-  16:29 Stopped and restarted navigation, routine and executive
-  18:30 Restarted mongodb log script since tmux script had robot\_pose
   twice, so since wednesday no robot\_poses logged

--------------

-  Date: 07/05/2015
-  Expert name: Chris Burbridge
-  Comments: An excellent day, bob started well at 9.30am doing
   scheduled things. I demanded many learning tasks in addition.
-  Failures: Edge learning between the door and the charging station
   failed repeatedly due to not being able to rotate. This then caused
   backtracking which backtracked out the door, repeated.
-  Restarts: Object learning and metric mapping nodes restarted many
   times to fix bugs with logging. Replicator node restarted to add
   parameter for extra datacentre and dump path. Offline learning for
   trajectories restarted to incorporate Paul's PR to include time
   limited robot\_pose queries. Routine restarted to incorporate Nick's
   PR to fix edge traversal.
-  Forced navigations: To avoid repeating the edge traversal learning i
   had to manually persuade bob to traverse the edge.

--------------

-  Date: 05/05/2015
-  Expert name: Bruno Lacerda
-  Comments: Use this entry as a template. Copy it and add new
   interventions on the top of the file.

--------------



Original page: https://github.com/strands-project/g4s_deployment/blob/indigo-devel/expert_interventions/expert_interventions.md
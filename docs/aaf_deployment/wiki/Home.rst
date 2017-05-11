**This is a public Wiki, no confidential information to go in here!**

AAF Deployment 2016
===================

**Discussions of improvements in Google doc shared via mailing list
(can't link here, as it's public)**

-  Can run during night in Administration Wing, including the lobby
   (effectively y1 area)
-  see
   `issues <https://github.com/strands-project/aaf_deployment/milestones/aaf-predeployment-2016>`__

AAF Press Dates
---------------

-  05.04. 13:00 CET Short interview for local press (Die ganze Woche")
-  05.04. 15:00 CET Filming/short interview for RT (Russian Television
   abroad)
-  06.04. 13:00 Short interview and photo for local press
   ("Bezirksblatt")
-  14.04. 14:30 Interviews for Autrian radio

--------------

AAF Deployment 2015
===================

A number of pages on
`strands\_management <https://github.com/strands-project/strands_management>`__
(restricted access) describe the AAF scenario in greater detail: \*
`General Scenario
description <https://github.com/strands-project/strands_management/wiki/Y2-Integration---Care-Scenarios>`__
\* Bellbot (lead by Yiannis) \* Walking Group (lead by Christian D) \*
Info Terminal (lead by Michi) \* `Setup Network etc. at
AAF <https://github.com/strands-project/strands_management/wiki/Y2-Integration-Scenarios>`__
\* `General task and Deliverables for
yr2 <https://github.com/strands-project/strands_management/wiki/Y2-Tasks>`__
\* `Overview of STRANDS packaging and releasing
procedures <https://github.com/strands-project/strands_management/wiki/STRANDS-software-packaging,-deployment,-and-testing-(using-Jenkins)>`__

Tasks that can be scheduled
---------------------------

Besides the normal info\_task that is scheduled by ``infremen`` every 10
minutes to run for 5 minutes, we can schedule tasks in the `Google
Calendar <https://www.google.com/calendar/embed?title=Henry's%20schedule&showCalendars=0&height=600&wkst=2&hl=de&bgcolor=%23FFFFFF&src=henry.strands%40hanheide.net&color=%23B1365F&ctz=Europe%2FVienna>`__.
Here's a list of possible tasks, the "Where" field of an event must name
a valid waypoint.

-  ``info_task_server``: Run the info terminal at a given waypoint
-  ```charging_task`` <https://github.com/strands-project/aaf_deployment/blob/indigo-devel/aaf_bringup/launch/aaf_routine.launch#L20>`__:
   effectively waits at a given waypoint being non-interruptible. The
   duration is taken from the actual window and by default 10 minutes
   are subtracted for the execution time. The waypoint for charging on
   the docking station should be "ChargingPoint", but we could manually
   charge somewhere else.
-  ```maintenance_task`` <https://github.com/strands-project/aaf_deployment/blob/indigo-devel/aaf_bringup/launch/aaf_routine.launch#L25>`__:
   pretty much the same as ``charging_task``, but interruptible
-  ```bellbot`` <https://github.com/strands-project/aaf_deployment/blob/indigo-devel/aaf_bellbot/scripts/start_bellbot.py#L120>`__
   Start a bellbot task to guide a person to a destination. The Waypoint
   given is the one where the robot is to pick up the person (usually
   "Rezeption").
-  ```walking_group_slow`` <https://github.com/strands-project/aaf_deployment/blob/indigo-devel/aaf_walking_group/etc/walking_groups.yaml#L2>`__:
   Start the *slow* walking group. The Waypoint given here is pretty
   useless, as the tour is hard coded.
-  ```walking_group_fast`` <https://github.com/strands-project/aaf_deployment/blob/indigo-devel/aaf_walking_group/etc/walking_groups.yaml#L26>`__:
   Start the *fast* walking group. The Waypoint given here is pretty
   useless, as the tour is hard coded.
-  ```store_logs`` <https://github.com/strands-project/aaf_deployment/blob/indigo-devel/aaf_logging/scripts/store_logs_task.py>`__:
   runs the message\_store replication, configured
   `here <https://github.com/strands-project/aaf_deployment/blob/indigo-devel/aaf_logging/launch/logging.launch#L21>`__
-  ```/topological_prediction/build_temporal_model`` <https://github.com/strands-project/aaf_deployment/issues/198>`__
   should be run every day in the evening in a ~5 minute window.

General structure
-----------------

-  The deployment shall be based on released packages on indigo amd64
-  This
   `aaf\_deployment <https://github.com/strands-project/aaf_deployment>`__
   repository is meant solely for *AAF-specific packages*, anything that
   has a wider use outside the AAF deployment shall go in dedicated
   packages, e.g. in
   `strands\_apps <https://github.com/strands-project/strands_apps>`__.
-  Contributions are via pull requests only and rigorous code review
   will take place, in particular after the feature freeze milestone.

Milestones
----------

1. `AAF 2015 Feature
   Freeze <https://github.com/strands-project/aaf_deployment/milestones/aaf_2015_feature_freeze>`__
   **2/4/15**:

-  All features implemented for the different task
-  A "global" scheduling approach working
-  Basic GUIs in place with functionality
-  The system will be ran continuously at UoL and Vienna from this point
   onwards, with bug fixes being integrated as soon as they arrive.

2. `AAF 2015
   Pre-Deployment <https://github.com/strands-project/aaf_deployment/milestones/aaf_2015_pre_deployment>`__
   **13/4/15**:

-  Henry will perform 3 days at AAF, based on the released packages
-  The pre-deployment will comprise a staff training session, to empower
   AAF members of staff to operate the robot and fill confident about
   using it
-  The interfaces and tasks need to be completed by this milestone, as
   staff training will be based on these interfaces. Minor design tweaks
   allowed based on feedback from staff. No structural changes in
   program logic or code structure beyond this point. No new features to
   be added either.

3. `AAF 2015
   Deployment <https://github.com/strands-project/aaf_deployment/milestones/aaf_2015_deployment>`__
   **11/5/15**:

-  Start of the actual deployment for 30 days (including weekends)

Henry@AAF
---------

-  For the deployment, Henry will be remotely administrated by the
   STRANDS team (check
   https://github.com/strands-project/strands\_management/wiki/Y2-Integration-Scenarios
   for details to log in)
-  On site, two laptops are provided for staff interactions and robot
   monitoring, one in Tobias' and Denise's AAF office, and one at the
   reception desk
-  The control interface (web service) shall be running on this:

   -  scheduling bellbot tasks
   -  displaying the robots current screen
   -  seeing the robot on a map
   -  scheduling other tasks
   -  monitoring the robot's health (battery, disk space)

-  The laptop in the AAF office is also the control-PC, running mongodb
   replication and serving the websites for the control interfaces (see
   above)
-  The docking station will be in the reception for Henry to approach
   whenever needed autonomously
-  An additional charging opportunity is in the AAF office by cable, an
   non-interruptable "maintenance" task shall be implemented to call the
   robot into the office for maintenance and charging, where it will be
   explicitly released again for other jobs by clicking in the GUI
-  (Video-)Recording will be disabled in the therapy wing (AAF to
   indicate the topological nodes that should be excluded)
-  An additional web cam shall be place above the screen for recording
   interactions. This shall be continuously recording data (using
   data\_compression node) whenever permitted at low framerate.
-  Data will be uploaded during charging period to the control-PC

Setup Henry
~~~~~~~~~~~

-  Networking:
-  when WIFI network connection drops we shall try to reconnect
   automatically by pasting
   `nm-connect.sh <https://gist.githubusercontent.com/marc-hanheide/8b79676812f8710b90bb/raw/55a2246a65ae367874477344edb7401d085e7ec9/nm-reconnect.sh>`__
   into root's crontab (``sudo crontab -e``)
-  Voice:
   `script <https://github.com/strands-project/aaf_deployment/commit/a169858c4a426febf8cf7149a5411375262c57c4>`__
   added that sets Henry's voice

Deployment Feedback
-------------------


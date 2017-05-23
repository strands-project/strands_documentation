Instructions
============

Viewing Betty's Internals
-------------------------

If you want to see what Betty is current doing, or send her to do some
particular tasks, you can visit http://10.0.107.108/betty/ (the exact
address, including the trailing slash is important). Under the tasks tab
you can trigger immediate greeting tasks and charging tasks.

Setting Greeting Tasks via Google Calendar
------------------------------------------

You can schedule tasks for Betty using Google calendar. Currently this
only supports the greeting task, but we can extend this for other
functionalities if you want.

To add tasks to Betty's calendar you need write access to it. You can
get this by either logging in directly to https://calendar.google.com
with the following credentials:

username: betty@strands-project.eu password: issue\_bough\_conga

Or we can share the calendar with your Google account so you can edit it
from there.

To add a greeting task create an event that starts at the time you wish
the greeting to start, and then make it as long as you want Betty to
perform greeting for. E.g. a greeting task starting at 10:00 and ending
at 11:00 should cause her to start greeting at 10:00 and do this for one
hour (provided her battery doesn't run low).

The details of the task are important. The title of the event must be
/tsc\_greeter and the where field of the task (the location) must be the
name of one of the waypoints in Betty's map. The most important ones are
FrontDoor and GlassCorridor0 which are the two waypoints near the
reception created for running this task.

You can also add announcer tasks with the event title /tsc\_announcer.
The location should correspond to the locations that are visible in the
user interface for the announcer (at
http://10.0.107.108:4990/betty/announcer). If you want to announce at
multiple locations, you should enter the locations separated by commas,
for example ``location1, location2, location3``. The announcement to
make should be put into the description of the event.

Using web interfaces to make requests for delivery or announcer tasks
---------------------------------------------------------------------

At http://10.0.107.108:4990/betty/announcer, you can find a web
interface for requesting announcer tasks

At http://10.0.107.108:4991/betty/basket, you can find a web interface
for requesting delivery tasks

Direct Robot Control
--------------------

If you need to use the joystick to help Betty out, consult this image
for instructions on the buttons:
https://raw.githubusercontent.com/strands-project/scitos\_apps/master/scitos\_teleop/doc/joypad-cheat-sheet.jpg


Original page: https://github.com/strands-project/g4s_deployment/blob/indigo-devel/docs/end-user-instructions.md
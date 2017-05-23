Walking Group
=============

This AAF task is meant to accompany the walking group, driving infront
of the therapist and the patients, providing entertainment during rests.

Functionality
-------------

The interaction between the robot and therapist is based on the
so-called key card (TODO: Upload key-card) which has to be worn around
his/her neck. There can be several therpists, each wearing a key card,
but there has to be at least one. The key card has to be worn visably,
as the robot relies on it to identify the therapist.

-  The robot will be waiting for the group to start at the predefined
   starting location. During this phase it will provide entertainment,
   i.e. play music, play videos, or show images via a simple to use and
   clearly structured interface which is supposed to be used by the
   patients.
-  To start the group, the therapist shows the robot the key card in the
   correct orientation. This will trigger the so called guide interface.
   In the guide interface,
-  the therapist can toggle playing of music while the groups is walking
   along the corridors. This will drown out every other auditive
   feedback. If music is turned off, the robot will play jingles and
   nature sounds at predefined locations and events.
-  the next waypoint can be chosen, either by just pressing "Weiter"
   which lets the robot drive to the next waypoint in the tour, or by
   selecting them from a list of all possible waypoints.
-  the guide interface can be cancelled which results in showing the
   entertainment interface again.
-  the whole tour can be cancelled which results in the robot going
   away, doing a science.
-  During the actual walking, the robot is driving in front of the
   group, playing either music or jingles and nature sounds. After a
   predefined distance the robot stops, waiting for the therapist to be
   "close" (using the key card to meassure distance), and then shows a
   large "Weiter" button, which can be bressed by the patients to send
   the robot off and to elicit interaction.
-  When a resting area is reached, the robot waits for the guide to come
   "close" (using the key card to meassure distance), and then shows two
   buttons, i.e. "Witer" and "Rast", which either send the robot to the
   next waypoint or shows the entertainment interface.

This will continue until the final waypoint is reached. During the whole
tour, whenever the guide shows the key card in the specific orientation,
the robot will stop and show the guide interface. This way, the music
can be toggled, the waypoint chosen or the tour preempted at any point
in time.

Usage
-----

The whole behaviour is run via the `axlaunch
server <https://github.com/strands-project/strands_apps/tree/indigo-devel/roslaunch_axserver>`__
, starting the components, and `the abstract task
server <https://github.com/strands-project/strands_executive/blob/hydro-release/strands_executive_msgs/src/strands_executive_msgs/abstract_task_server.py>`__
to create scheduable tasks.

Configuration
~~~~~~~~~~~~~

The most basic and important configuration happens via a datacentre
entry storing the waypoints at which to rest and the distance at which
the robot should stop in regular intervals. An example file could look
like this:

::

    slow:
        stopping_distance: 3.0
        waypoints:
            1: "WayPoint34"
            2: "WayPoint14"
            3: "WayPoint26"
            4: "WayPoint15"
            5: "WayPoint46"
    fast:
        stopping_distance: 5.0
        waypoints:
            1: "WayPoint34"
            2: "WayPoint14"
            3: "WayPoint26"
            4: "WayPoint15"
            5: "WayPoint46"

``slow`` and ``fast`` are internally used identifiers. They don't have
to have specific names but have to be unique and consistent with the
``group`` entry described below. The ``stopping_distance`` is the
distance after which the robot will wait for the therapist to come
close, to show a button, which can be pressed by the patients to send it
off again. The ``waypoints`` entry specifies the waypoints at which the
group usually rests. Waypoints not specified in this list can never be
selected as resting areas during a tour; the index specifies the order
of points.

This file has to be inserted into the datacentre using a provided
script:

::

    $ rosrun aaf_walking_group insert_yaml.py --help
    usage: insert_yaml.py [-h] -i INPUT [--collection_name COLLECTION_NAME]
                          [--meta_name META_NAME]
                          dataset_name

    positional arguments:
      dataset_name          The name of the dataset. Saved in meta information
                            using 'meta_name'

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            Input yaml file
      --collection_name COLLECTION_NAME
                            The collection name. Default: aaf_walking_group
      --meta_name META_NAME
                            The name of the meta filed to store 'dataset_name' in.
                            Default: waypoint_set

shows it's functionalities. The defaults for ``meta_name`` and
``collection_name`` can be changed, but will then have to be specified
at start-up. Otherwise, the defaults in the launch file correspond with
the defaults in the script. The ``dataset_name`` name is a mendatory
argument which is used to identify the configuration you stored. With
``-i <my_file>`` you specify the input file. Once that has been inserted
we can move on to the second config file, loaded on start-up. An example
file could look like this:

::

    walking_group:
        walking_group_slow:
            group: 'slow'
            start_location: 'WayPoint34'
            max_duration: 3600
            parameters: 
                - 'music_set_group'
                - 'waypoint_set'
            values: 
                - 'my_set'
                - 'aaf_waypoints'
        walking_group_fast:
            group: 'fast'
            start_location: 'WayPoint34'
            max_duration: 3600
            parameters: 
                - 'music_set_group'
                - 'waypoint_set'
            values: 
                - 'my_set'
                - 'aaf_waypoints'

``walking_group_slow`` and ``walking_group_fast`` is used to create two
action servers with the corresponding name, therefore these names have
to be unique. The number of action servers is dynamic and can be changed
by adding another entry to this file. ``group`` is used to identify the
specific set of waypoints from the datacentre (see above); ``slow`` or
``fast`` in our case. ``start_location`` is the waypoint to which the
scheduler sends the robot at the beginning of the task and should be the
same as the first waypoint in the list above; ``WayPoint34`` in our
case. The ``max_duration`` is another argument for the schaduler which
tells it how long the group task lasts in the worst case. If this time
is reached it will assume that the task failed and preempt it. The
``parameters`` and ``values`` fields are used together to create the
start-up parameters for the internally used launch file:

-  ``waypoint_set`` *default="aaf*\ waypoints"\_: The ``dataset_name``
   used when inserting the yaml file using ``insert_yaml.py``
-  ``meta_name`` *default="waypoint*\ set"\_: The ``meta_name`` used
   when inserting the yaml file using ``insert_yaml.py``
-  ``collection_name`` *default="aaf*\ walking\_group"\_: The
   ``collection_name`` used when inserting the yaml file using
   ``insert_yaml.py``
-  ``waypoint_sounds_file`` *default="$(find
   aaf*\ walking\_group)/conf/waypoint\_sounds.yaml"\_: The waypoint
   sounds file, describing the waypoints at which to play sounds and
   which sounds to play; see below.
-  ``music_set_group`` *default="aaf*\ walking\_group\_music"\_: The
   media server music set to play during the walking phase and via the
   entertainment interface.
-  ``music_set_waypoints`` *default="aaf*\ waypoint\_sounds"\_: The
   media server music set containing the waypoint sounds.
-  ``music_set_jingles`` *default="aaf*\ jingles"\_: The media server
   music set containing the jingles used.
-  ``music_set_recovery``
   *default="aaf*\ walking\_group\_recovery\_sounds"\_: The media server
   music set containing the jingles used.
-  ``video_set`` *default="aaf*\ walking\_group\_videos"\_: The media
   server video set containing the videos shown during entertainment.
-  ``image_set`` *default="aaf*\ walking\_group\_pictures"\_: The media
   server image set containing the pictures shown during entertainment.

**Configuring the recovery behaviours**

Recovery behaviours are dynamically turend on and off during start-up
and after the end of the walking group to prevent some of them from
kicking in, making the robot drive backwards. Additionally, a custom
recovery behaviour, playing a sounds when in trouble, is added. To tell
the navigation which behaviour should be used during the group, we
create a so-called whitelist which could look like this:

::

    recover_states:
      sleep_and_retry: [true, .inf]
      walking_group_help: [true, .inf]

This enables, the ``sleep_and_retry`` and ``walking_group_help``
recovery states and sets the possible retries to ``inf``. Every
behaviour not in this list, will be disabled during the group and
reenabled afterwards.

**Configuring the media sets**

The video and image set can contain any form of images and videos and
just have to be passed by name during start-up. The ``music_set_group``
can contain any kind of music and just has to be passed by name during
start-up. The jingles and waypoint sets are a bit more special. The
jingles used have to have the following filenames:

-  ``jingle_stop.mp3``: Played when the robot stops and waits for
   someone to press the "Weiter" button.
-  ``jingle_patient_continue.mp3``: Sound played when someone presses
   the "Weiter" button
-  ``jingle_therapist_continue.mp3``: Sound played when the robot starts
   navigating after a therapist interaction.
-  ``jingle_waypoint_reached.mp3``: Sound played when a resting point is
   reached.

Currently these names are hard coded. For the waypoint sounds, we
provide a config file loaded from the ``waypoint_sounds_file``
parameter. An example file could look like this:

::

    waypoint_sounds: '{"Lift1": "great_tit.mp3", "WayPoint7": "crested_tit.mp3", "Cafeteria": "northern_tit.mp3", "WayPoint8": "marsh_tit.mp3"}'

The keys of the dictornary are topological waypoint names and the values
are the filenames of the music played when reaching that waypoint. In
this case we play a selection of bird sounds.

Running
~~~~~~~

Start the managing action server(s):

::

    roslaunch aaf_walking_group task_servers.launch

this launch file has one parameter: ``config_file`` which specifies the
location of the yaml file used to specify parameters needed to run the
behaviour. This file is the one described above setting the parameters
in the ``walking_group`` namespace.

Once the launch file is started it provides the respective number of
action servers which have an empty goals since everything is defined in
the config file. These can easily be scheduled using the google calendar
interface since they inherit from `the abstract task
server <https://github.com/strands-project/strands_executive/blob/hydro-release/strands_executive_msgs/src/strands_executive_msgs/abstract_task_server.py>`__.
An example would be, using all the above config files, we have two
action servers, one called ``walking_group_slow`` and the other
``walking_group_fast``. By creating a new event in the google calendar
of the robot called either ``walking_group_slow`` or
``walking_group_fast`` it will schedule the task and start the specific
action server. No additional configuration required. This makes it easy
to schedule these events, the only thing that has to be observed is that
the actual time window is larger than the ``max_duration`` set in the
launch file. Otherwise the duration can be overridden in the calendar by
using yaml style arguments in the event description.

Component Behaviour
~~~~~~~~~~~~~~~~~~~

The actually started action servers don't do anything until they receive
a goal. When a new goal is sent, they \* start the necessary components
using the `axlaunch
server <https://github.com/strands-project/strands_apps/tree/indigo-devel/roslaunch_axserver>`__
\* start the task immediately after the components are launched.

After the task is preempted or successful, the components are stopped to
not use any memory or CPU if the task is not running.

The servers communicate via a topic if an instance of the walking group
is already running or not. When trying to start a second instance, e.g.
slow is already running and you want to start fast, the goal will be
abborted.

Testing
~~~~~~~

To start the statemachine, run above launch file and configuration. Use,
e.g.

::

    rosrun actionlib axclient.py /walking_group_fast

To emulate the therapist being close, publish:

::

    rostopic pub /socialCardReader/QSR_generator std_msgs/String "data: 'near'"

to emulate the therpist showing the key card in the specified
orientation, publish:

::

    rostopic pub /socialCardReader/commands std_msgs/String "data: 'PAUSE_WALK'"



Original page: https://github.com/strands-project/aaf_deployment/blob/indigo-devel/info_terminal/README.md
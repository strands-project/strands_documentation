Launch package
==============

This convenience package contains launch files to start-up the whole
people tracker system.

General remarks
---------------

All the the packages rely heavily on the synchronisation of rgb and
depth images and the generated data of the other nodes. The
synchronization is realised using a queue which saves a predefined
number of messages on which the synchronisation is performed. *As a rule
of thumb: the faster your machine the shorter the queue to prevent
unnecessary use of memory.* You can set queue sizes using:

::

    roslaunch perception_people_launch file.launch gh_queue_size:=11 vo_queue_size:=22 ubd_queue_size:=33 pt_queue_size:=44

This will overwrite the default values. *gh = ground*\ hog, vo =
visual\_odemetry, ubd = upper\_body\_detector, pt =
mdl\_people\_tracker\_

The whole pipeline is desinged to unsuscribe from everything if there is
no subscriber to the published topics. This causes the nodes to not use
any CPU when there is no one listening on the published topics. This
might result in a 1-2 second dealy after subscribing to one of the
topics before the first data is published. Also, setting ``log`` to true
when starting the perception pipeline will cause it to always run and
log data.

Running on robot
----------------

These launch files will make use of the fixed ground plane which is just
rotated according to the PTU tilt and the robot odometry instead of the
visual odometry. Additionally, the necessary parameters are assumed to
be provided by the parameter server (see mongodb\_store confog\_manager
on default parameters) therefore the ``load_params_from_file`` parameter
is set to ``false`` and the nodes will querry the config parameters from
the parameter server. The standalone version on the other hand uses the
provided config files. If parameters are not present in the paremeter
server on the robot but you want to launch the ppl perception, run with
``load_params_from_file:=true``.

people\_tracker\_robot.launch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This version of the tracking does not rely on the ground\_hog feature
extraction and is therefore usable on PCs with no NVIDIA graphics card
(like the embedded robot PC). However, this has the drawback that the
system only relies on depth data to detect people which limits the
distance at which persons can be detected to approx. 5 meters. Where
possible the ground\_hog detection should be used to enhance tracking
results. It also uses the fixed ground plane assumption because it is
ment to be executed on the robots head xtion camera.

Parameters: \* ``load_params_from_file`` *default = true*: ``false``
tries to read parameters from datacentre, ``true`` reads parameters from
YAML file specified by ``param_file`` \* ``machine`` *default =
localhost*: Determines on which machine this node should run. \*
``user`` *default = ""*: The user used for the ssh connection if machine
is not localhost. \* ``gp_queue_size`` *default = 5*: The ground plane
sync queue size \* ``ubd_queue_size`` *default = 5*: The upper body
detector sync queue size \* ``pt_queue_size`` *default = 10*: The people
tracking sync queue size \* ``ptu_state`` *default = /ptu/state*: The
ptu state topic \* ``camera_namespace`` *default = /head*\ xtion\_: The
camera namespace. \* ``rgb_image`` *default =
/rgb/image*\ rect\_color\_: ``camera_namespace`` + ``rgb_image`` = rgb
image topic \* ``depth_image`` *default = /depth/image*\ rect\_:
``camera_namespace`` + ``depth_image`` = depth image topic \*
``mono_image`` *default = /rgb/image*\ mono\_: ``camera_namespace`` +
``mono_image`` = mono image topic \* ``camera_info_rgb`` *default =
/rgb/camera*\ info\_: ``camera_namespace`` + ``camera_info_rgb`` = rgb
camera info topic \* ``camera_info_depth`` *default =
/depth/camera*\ info\_: ``camera_namespace`` + ``camera_info_depth`` =
depth camera info topic \* ``ground_plane`` *default =
/ground*\ plane\_: The fixed ground plane \* ``upper_body_detections``
*default = /upper*\ body\_detector/detections\_: The detected upper body
\* ``upper_body_bb_centres`` *default =
/upper*\ body\_detector/bounding\_box\_centres\_: Publishing a pose
array of the centres of the bounding boxes \*
``upper_body_markers default = /upper_body_detector/marker_array_: A visualisation array for rviz *``\ upper\_body\_image\ ``_default = /upper_body_detector/image_: The detected upper body image *``\ visual\_odometry\ ``_default = /visual_odometry/motion_matrix_: The odometry. This takes the real odometry and only follows naming conventions for the ease of use. *``\ mdl\_people\_array\ ``_default = /mdl_people_tracker/people_array_: The detected and tracked people *``\ mdl\_people\_markers"
default="/mdl\_people\_tracker/marker\_array\_: A visualisation array
for rviz \*
``mdl_people_poses" default = /mdl_people_tracker/pose_array_: A PoseArray of the detected people *``\ tf\_target\_frame\ ``_default = /map: The coordinate system into which the localisations should be transformed *``\ bayes\_people\_positions\ ``_default = /people_tracker/positions_: The poses of the tracked people *``\ bayes\_people\_pose\ ``: _Default: /people_tracker/pose_: The topic under which the closest detected person is published as a geometry_msgs/PoseStamped``
\* ``bayes_people_pose_array``: *Default:
/people*\ tracker/pose\_array\_: The topic under which the detections
are published as a
geometry\_msgs/PoseArray\ ``*``\ bayes\_people\_poeple\ ``: _Default: /people_tracker/people_: The topic under which the results are published as people_msgs/People``
\* ``pd_marker`` *default = /people*\ tracker/marker\_array\_: A marker
arry to visualise found people in rviz \* ``log`` *default = false*: Log
people and robot locations together with tracking and detection results
to message\_store database into people\_perception collection. Disabled
by default because if it is enabled the perception is running
continuously. \* ``with_mdl_tracker`` *default = false*: Starts the mdl
people tracker in addition to the bayes tracker \* ``with_laser_filter``
*default = true*: Starts the laser filter to reduce false positives from
the leg detector \* ``with_tracker_filter_map`` *default = false*: Use a
special map to filter the tracker results instead of just the map used
for navigation. \* ``tracker_filter_map``: The map to use instead of the
navigation map to filter the tracker results. \*
``tracker_filter_positions`` *default =
/people*\ tracker\_filter/positions\_: The filtered tracker results. \*
``tracker_filter_pose`` *default = /people*\ tracker\_filter/pose\_: The
filtered pose for the closest person. \* ``tracker_filter_pose_array``
*default = /people*\ tracker\_filter/pose\_array\_: The filetered pose
array. \* ``tracker_filter_people`` *default =
/people*\ tracker\_filter/people\_: The filetered people message. \*
``tracker_filter_marker`` *default =
/people*\ tracker\_filter/marker\_array\_: The filetered marker array.

Running:

::

    roslaunch perception_people_launch people_tracker_robot.launch [parameter_name:=value]

people\_tracker\_standalone.launch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This version of the tracking does not rely on the ground\_hog feature
extraction and is therefore usable on PCs with no NVIDIA graphics card.
However, this has the drawback that the system only relies on depth data
to detect people which limits the distance at which persons can be
detected to approx. 5 meters. Where possible the ground\_hog detection
should be used to enhance tracking results.

It also uses the ``/camera`` namespace as a default and estimates the
groundplane because it is not supposed to be run on the robot but on an
external PC with a different set-up.

Parameters: \* ``load_params_from_file`` *default = true*: ``false``
tries to read parameters from datacentre, ``true`` reads parameters from
YAML file specified by ``param_file`` \* ``machine`` *default =
localhost*: Determines on which machine this node should run. \*
``user`` *default = ""*: The user used for the ssh connection if machine
is not localhost. \* ``gh_queue_size`` *default = 20*: The ground plane
sync queue size \* ``vo_queue_size`` *default = 5*: The visual odometry
sync queue size \* ``ubd_queue_size`` *default = 5*: The upper body
detector sync queue size \* ``pt_queue_size`` *default = 10*: The people
tracking sync queue size \* ``camera_namespace`` *default = /camera*:
The camera namespace. \* ``rgb_image`` *default =
/rgb/image*\ rect\_color\_: ``camera_namespace`` + ``rgb_image`` = rgb
image topic \* ``depth_image`` *default = /depth/image*\ rect\_:
``camera_namespace`` + ``depth_image`` = depth image topic \*
``mono_image`` *default = /rgb/image*\ mono\_: ``camera_namespace`` +
``mono_image`` = mono image topic \* ``camera_info_rgb`` *default =
/rgb/camera*\ info\_: ``camera_namespace`` + ``camera_info_rgb`` = rgb
camera info topic \* ``camera_info_depth`` *default =
/depth/camera*\ info\_: ``camera_namespace`` + ``camera_info_depth`` =
depth camera info topic \* ``ground_plane`` *default =
/ground*\ plane\_: The estimated ground plane \*
``upper_body_detections`` *default =
/upper*\ body\_detector/detections\_: The detected upper body \*
``upper_body_bb_centres`` *default =
/upper*\ body\_detector/bounding\_box\_centres\_: Publishing a pose
array of the centres of the bounding boxes \*
``upper_body_markers default = /upper_body_detector/marker_array_: A visualisation array for rviz *``\ upper\_body\_image\ ``_default = /upper_body_detector/image_: The detected upper body image *``\ visual\_odometry\ ``_default = /visual_odometry/motion_matrix_: The visual odometry *``\ pedestrain\_array\ ``_default = /mdl_people_tracker/people_array_: The detected and tracked people *``\ people\_markers"
default="/mdl\_people\_tracker/marker\_array\_: A visualisation array
for rviz \*
``people_poses" default = /mdl_people_tracker/pose_array_: A PoseArray of the detected people *``\ tf\_target\_frame\`
*default = ""*: The coordinate system into which the localisations
should be transformed. As this might not run on a robot and therefore no
tf is available this is an empty string.

Running:

::

    roslaunch perception_people_launch people_tracker_standalone.launch [parameter_name:=value]


Attic directory containing depricated launch files
--------------------------------------------------

these launch files are used to start the ppl perception using HOG featur
detection. This is currently deprecated and not supported. The code for
this can be found in the ``attic`` branch. This directory is not
installed and therefore just to preserve the files themselves. Following
are the instructions on how to use these files:

people\_tracker\_robot\_with\_HOG.launch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This version of the tracking does rely on the ground\_hog feature
extraction and is therefore only usable on PCs with an NVIDIA graphics
card. It also relys on the fixed ground plane assumption made for the
robot. To use this you have to run it remotely on a machine talking to
the rosmaster on the robot, e.g. a laptop inside the robot.

Parameters: \* ``load_params_from_file`` *default = true*: ``false``
tries to read parameters from datacentre, ``true`` reads parameters from
YAML file specified by ``param_file`` \* ``machine`` *default =
localhost*: Determines on which machine this node should run. \*
``user`` *default = ""*: The user used for the ssh connection if machine
is not localhost. \* ``gp_queue_size`` *default = 5*: The ground plane
sync queue size \* ``gh_queue_size`` *default = 20*: The ground plane
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
``upper_body_markers default = /upper_body_detector/marker_array_: A visualisation array for rviz *``\ upper\_body\_image\ ``_default = /upper_body_detector/image_: The detected upper body image *``\ visual\_odometry\ ``_default = /visual_odometry/motion_matrix_: The odometry. This takes the real odometry and only follows naming conventions for the ease of use. *``\ pedestrain\_array\ ``_default = /mdl_people_tracker/people_array_: The detected and tracked people *``\ people\_markers"
default="/mdl\_people\_tracker/marker\_array\_: A visualisation array
for rviz \*
``people_poses" default = /mdl_people_tracker/pose_array_: A PoseArray of the detected people *``\ tf\_target\_frame\ ``_default = /map: The coordinate system into which the localisations should be transformed *``\ pd\_positions\ ``_default = /people_tracker/positions_: The poses of the tracked people *``\ pd\_marker\ ``_default = /people_tracker/marker_array_: A marker arry to visualise found people in rviz *``\ log\`
*default = false*: Log people and robot locations together with tracking
and detection results to message\_store database into people\_perception
collection. Disabled by default because if it is enabled the perception
is running continuously.

Running:

::

    roslaunch perception_people_launch people_tracker_robot_with_HOG.launch [parameter_name:=value]

people\_tracker\_standalone\_with\_HOG.launch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This depends on the strands\_ground\_hog package which has to be built
with the libcudaHOG. See README file of 3rd\_party directory. It also
uses the ``/camera`` namespace as a default and estimates the
groundplane because it is not supposed to be run on the robot but on an
external PC with a different set-up.

Parameters: \* ``load_params_from_file`` *default = true*: ``false``
tries to read parameters from datacentre, ``true`` reads parameters from
YAML file specified by ``param_file`` \* ``machine`` *default =
localhost*: Determines on which machine this node should run. \*
``user`` *default = ""*: The user used for the ssh connection if machine
is not localhost. \* ``gh_queue_size`` *default = 10*: The ground hog
sync queue size \* ``gp_queue_size`` *default = 5*: The ground plane
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
``ground_hog_detections`` *default = /groundHOG/detections*: The ground
HOG detections \* ``upper_body_detections`` *default =
/upper*\ body\_detector/detections\_: The detected upper body \*
``upper_body_bb_centres`` *default =
/upper*\ body\_detector/bounding\_box\_centres\_: Publishing a pose
array of the centres of the bounding boxes \*
``upper_body_markers default = /upper_body_detector/marker_array_: A visualisation array for rviz *``\ ground\_hog\_image\ ``_default = /groundHOG/image_: The ground HOG image *``\ upper\_body\_image\ ``_default = /upper_body_detector/image_: The detected upper body image *``\ visual\_odometry\ ``_default = /visual_odometry/motion_matrix_: The visual odometry *``\ people\_markers"
default="/mdl\_people\_tracker/marker\_array\_: A visualisation array
for rviz \*
``people_poses" default = /mdl_people_tracker/pose_array_: A PoseArray of the detected people *``\ people\_markers"
default="/mdl\_people\_tracker/marker\_array\ ``: A visualisation array for rviz *``\ tf\_target\_frame\`
*default = ""*: The coordinate system into which the localisations
should be transformed. As this might not run on a robot and therefore no
tf is available this is an empty string.

Running:

::

    roslaunch perception_people_launch people_tracker_standalone_with_HOG.launch [parameter_name:=value]


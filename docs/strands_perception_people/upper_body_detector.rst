Upper Body Detector
-------------------

This package detects the upper bodies of persons using the depth image.

Run
~~~

Parameters: \* ``load_params_from_file`` *default = true*: ``false``
tries to read parameters from datacentre, ``true`` reads parameters from
YAML file specified by ``config_file`` \* ``config_file`` *default =
:math:`(find upper_body_detector)/config/upper_body_detector.yaml_: The config file containing all the essential parameters. Only used if `load_params_from_file == true`. * `template_file` _default = `\ (find
upper*\ body\_detector)/config/upper\_body\_template.yaml\_: The upper
body template file. Read from the database if
``load_params_from_file == true``. \* ``machine`` *default = localhost*:
Determines on which machine this node should run. \* ``user`` *default =
""*: The user used for the ssh connection if machine is not localhost.
\* ``queue_size`` *default = 20*: The synchronisation queue size \*
``config_file`` *default = ""*: The global config file. Can be found in
strands\_upper\_bodydetector/config \* ``template_file`` *default = ""*:
The template file. Can be found in config. \* ``camera_namespace``
*default = /head*\ xtion\_: The camera namespace. \* ``depth_image``
*default = /depth/image*\ rect\_: ``camera_namespace`` + ``depth_image``
= depth image topic \* ``rgb_image`` *default =
/rgb/image*\ rect\_color\_: ``camera_namespace`` + ``rgb_image`` = rgb
image topic \* ``camera_info_depth`` *default = /depth/camera*\ info\_:
``camera_namespace`` + ``camera_info_depth`` = depth camera info topic
\* ``ground_plane`` *default = /ground*\ plane\_: The estimated/fixed
ground plane \* ``upper_body_detections`` *default =
/upper*\ body\_detector/detections\_: The deteced upper bodies \*
``upper_body_bb_centres`` *default =
/upper*\ body\_detector/bounding\_box\_centres\_: Publishing a pose
array of the centres of the bounding boxes \* ``upper_body_image``
*default = /upper*\ body\_detector/image\_: The resulting image showing
the detections as a boundingbox \* \`upper\_body\_markers default =
/upper\_body\_detector/marker\_array\_: A visualisation array for rviz

rosrun:

::

    rosrun upper_body_detector upper_body_detector [_parameter_name:=value]

roslaunch:

::

    roslaunch upper_body_detector upper_body_detector.launch [parameter_name:=value]



Original page: https://github.com/strands-project/strands_perception_people/blob/indigo-devel/upper_body_detector/README.md
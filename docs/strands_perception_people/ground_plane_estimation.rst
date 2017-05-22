Ground Plane
------------

This package estimates the ground plane using depth images.

It can also be used with a fixed ground plane which is just rotated
according to the ptu tilt angle. In this case the optimal ground plane
is assumed and represented by the normal vector [0,-1,0] and the
distance of 1.7 (Distance of the origin of the camera coordinated system
to the plane in meters). These values can be changed in the
config/fixed\_gp.yaml file. As you can see this assumes to be used with
the head\_xtion and is therefore exclusive to the robot but it also
prevents failurs due to wrongly estimated planes in cases where the
camera can't see the ground. All this was necessary because the camera
on the head of the robot is rather high and therefore has a high risk of
not seeing the actual ground plane. At the current state of development
it is advised to use the fixed plane set-up when running it on the
robot.

Run
~~~

Parameters for estimation: \* ``load_params_from_file`` *default =
true*: ``false`` tries to read parameters from datacentre, ``true``
reads parameters from YAML file specified by ``param_file`` \*
``param_file`` *default = $(find
ground*\ plane\_estimation)/config/estimated\_gp.yaml\_: The config file
containing all the essential parameters. Only used if
``load_params_from_file == true``. \* ``machine`` *default = localhost*:
Determines on which machine this node should run. \* ``user`` *default =
""*: The user used for the ssh connection if machine is not localhost.
\* ``queue_size`` *default = 5*: The synchronisation queue size \*
``config_file`` *default = ""*: The global config file. Can be found in
ground\_plane\_estimation/config \* ``camera_namespace`` *default =
/head*\ xtion\_: The camera namespace. \* ``depth_image`` *default =
/depth/image*\ rect\_: ``camera_namespace`` + ``depth_image`` = depth
image topic \* ``camera_info_rgb`` *default = /rgb/camera*\ info\_:
``camera_namespace`` + ``camera_info_rgb`` = rgb camera info topic \*
``ground_plane`` *default = /ground*\ plane\_: The estimated ground
plane

Parameters for the fixed ground plane: \* ``load_params_from_file``
*default = true*: ``false`` tries to read parameters from datacentre,
``true`` reads parameters from YAML file specified by ``param_file`` \*
``param_file`` *default = $(find
ground*\ plane\_estimation)/config/fixed\_gp.yaml\_: The config file
containing all the essential parameters. Only used if
``load_params_from_file == true``. \* ``machine`` *default = localhost*:
Determines on which machine this node should run. \* ``user`` *default =
""*: The user used for the ssh connection if machine is not localhost.
\* ``ptu_state`` *default = /ptu/state*: The current angles of the ptu
\* ``ground_plane`` *default = /ground*\ plane\_: The rotated ground
plane

rosrun:

::

    rosrun ground_plane_estimation ground_plane_estimated [_parameter_name:=value]

or

::

    rosrun ground_plane_estimation ground_plane_fixed [_parameter_name:=value]

roslaunch:

::

    roslaunch ground_plane_estimation ground_plane_estimated.launch [parameter_name:=value]

or

::

    roslaunch ground_plane_estimation ground_plane_fixed.launch [parameter_name:=value]


strands\_morse
==============

A MORSE-based simulation for the STRANDS project

Prerequisites
-------------

For running the simulation you would need:

-  `MORSE <http://www.openrobots.org/morse/doc/latest/user/installation.html>`__
-  `Blender <http://www.blender.org/download/get-blender/>`__
-  `ROS <http://www.ros.org/wiki/ROS/Installation>`__

We recommend to install the morse-blender-bundle from our debian server:

-  Set-up instructions: `Using the STRANDS
   repository <https://github.com/strands-project-releases/strands-releases/wiki#using-the-strands-repository>`__
-  Install the bundle:
   ``sudo apt-get install morse-blender-2.65-py-3.3``
-  Source the environment:
   ``source /opt/morse-blender-2.65-py-3.3/.bashrc`` *You might want to
   add this to your ~/.bashrc*
-  Check if morse has installed correctly: ``morse check``

Please refer to the respective installation guides to install them on
your system.

The current software has been tested under the following configuration:

-  MORSE (strands-project/morse)
-  Blender 2.63a
-  ROS Groovy
-  Python 3.2.3 (3.3.0)
-  Ubuntu 12.04 LTS

Please note: Using a depth camera requires Python 3.3.0 and a
corresponding Blender version (>2.65).

Getting Started
---------------

Start some terminals and run the commands below:

1. Fire up roscore:

   ::

       $ roscore

2. Run the MORSE simulation:

   ::

       $ roslaunch strands_morse bham_cs_morse.launch

3. (optional) Launch the 2D navigation:

   ::

       $ roslaunch strands_morse bham_cs_nav2d.launch

4. (optional) To visualize the environment model in RVIZ run

   ::

       $ rosrun rviz rviz

       $ roslaunch strands_morse bham_cs_rviz.launch

and add a new display of type ``RobotModel`` in RVIZ. Set the
robot\_description to ``/env/env_description`` and TF prefix to ``env``.
(requires
`strands\_utils <https://github.com/strands-project/strands_utils>`__)

The commands above use the lower ground floor of the Computer Science
building by default. For simulating a different level of the building
please run:

::

        $ roslaunch strands_morse bham_cs_morse.launch env:=cs_1

Other available environments are: cs\_lg, cs\_ug, cs\_1, cs\_2, cs (for
the whole building)

Similarly, you have to run the navigation and visualization with an
extra argument as follows:

::

        $ roslaunch strands_morse bham_cs_nav2d.launch env:=cs_1               

        $ roslaunch strands_morse bham_cs_rviz.launch env:=cs_1

--------------

To start run the MORSE simulation of the TUM kitchen with a ScitosA5:

::

       $ roslaunch strands_morse tum_kitchen_morse.launch

Alternatively:

::

       $ roslaunch strands_morse tum_kitchen_morse.launch env:=tum_kitchen_WITHOUT_CAMERAS

--------------

The Scitos robot model is equipped with a video, depth and semantic
camera by default.

If you wish to start the robot without any camera provide
``Scitosa5.WITHOUT_CAMERAS`` in the robot's constructor (see example
below). Starting the robot without any camera is useful to run MORSE in
fast\_mode.

If you only want to disable the depth camera, provide
``Scitosa5.WITHOUT_DEPTHCAM`` in the constructor. This might be useful
if you run MORSE on MacOSX, because users have reported problems when
using a depth camera.

Example usage in the MORSE builder script:

-  with cameras:

   ::

       robot = Scitosa5()
       # Alterntively
       # robot = Scitosa5(Scitosa5.WITH_CAMERAS)

-  without cameras

   ::

       robot = Scitosa5(Scitosa5.WITHOUT_CAMERAS)

-  without depth camera

   ::

       robot = Scitosa5(Scitosa5.WITHOUT_DEPTHCAMS)

-  with OpenNI stack generating point clouds and images, be sure to
   launch ``roslaunch strands_morse generate_camera_topics.launch`` and

   ::

       robot = Scitosa5(Scitosa5.WITH_OPENNI)




Original page: https://github.com/strands-project/strands_morse/blob/indigo-devel/README.md
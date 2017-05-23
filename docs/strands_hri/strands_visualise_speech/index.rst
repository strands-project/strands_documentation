Visualise speech package
------------------------

This package provides a control node for the head lights of the robot to
compensate for the fact that it does not have a mouth for speaker
identification. At the current stage the node uses pulseaudio to read
the output levels of the soundcard and translates this to control
commands for the head lights. The louder the more lights are
illuminated.

Installation
~~~~~~~~~~~~

-  make sure that the submodules are there before running
   ``catkin_make``
-  ``cd strands_hri``
-  ``git submodule init``
-  ``git submodule update``

Usage
~~~~~

*Cannot be run remotely. Needs to access the robots hardware.*

This node is a action server and needs a goal to start doing anything.
The only parameter of the goal is the runtime of the system: \* seconds:
run time in seconds. 0 for infinite (until preempted)

Run with: ``rosrun strands_visualise_speech sound_to_light.py`` or
better: have a look at the strands\_hri\_utils package to run together
with the convenience action server provided in there.

*Troubleshooting*: \* The audio grabber assumes that your sound sink is
called
``alsa_output.usb-Burr-Brown_from_TI_USB_Audio_CODEC-00-CODEC.analog-stereo``
if it is not, the node won't do anything. You can check if the name is
correct by looking at the output. The node will list all available sinks
when started. Re-run the node with the parameter
``_sink_name:=<your sink>``. If the output states:
``setting up peak recording using <your sink name>`` it is configured
correctly. \* If the programme states ``Connection failed``, make sure
that no other user is logged in, hogging the sound resource.

*Problems*: \* The light control is very slow and therefore the lights
are a bit delayed. \* The publish rate had to be artificially reduced to
4hz because it would otherwise interfer with all the hardware control
commands.


Original page: https://github.com/strands-project/strands_hri/blob/hydro-devel/strands_visualise_speech/README.md
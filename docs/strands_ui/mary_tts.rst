A simple interface for the `MARY TTS system <http://mary.dfki.de/>`__.
Offers a service ``/ros_mary`` and an actionlib interface ``/speak``
that accepts a simple text argument and plays the audio using
PulseAudio.

-  launch it: ``roslaunch mary_tts ros_mary.launch``
-  make the robot speak:
   ``rosservice call /ros_mary 'Welcome to the school of computer science. Please follow me!'``
-  in order to use the actionlib cleint you can run
   ``rosrun actionlib axclient.py /speak``
-  switching voices:
   ``rosservice call /ros_mary/set_voice "dfki-obadiah-hsmm"``
-  switching languages: ``rosservice call /ros_mary/set_locale "en_US"``

Available languages and voices: \* it \* None \* te \* None \* en\_US \*
cmu-slt-hsmm (female) \* dfki-obadiah-hsmm (male) \* dfki-prudence-hsmm
(female) \* dfki-poppy-hsmm (female) \* dfki-spike-hsmm (male) \* tr \*
None \* ru \* None \* de \* bits1-hsmm (female) \* bits3-hsmm (male) \*
dfki-pavoque-neutral-hsmm (male) \* sv \* None

Installing new voices: Use
``strands_ui/mary_tts/marytts-5.0/bin/marytts-component-installer.sh``

Trouble shooting
----------------

If you experience errors like this:

::

    Traceback (most recent call last):
      File "/opt/ros/hydro/lib/mary_tts/marybridge.py", line 363, in <module>
        player.play(the_sound)
      File "/opt/ros/hydro/lib/mary_tts/marybridge.py", line 284, in play
        pa.strerror(ctypes.byref(error))))
    Exception: Could not create pulse audio stream: 30873552!
    [WARN] [WallTime: 1416493711.323501] mary speach action failed; maybe took too long (more than 10 seconds), maybe pulse is broke.

It means that mary was started when it could not determine which pulse
resource to use. This could have multiple reasons: \* mary was started
remotely without logging in as the same user on the PC or robot. Only
one user can access pulse on a PC. Who that user is decided by who is
currently logged in. If no one is logged in then pulse is not running,
therefore you have to log in to the PC before starting mary remotely. \*
mary was started as a different user than the one that is logged in. If
``user1`` is logged in and ``user2`` logs in remotely starting mary,
mary won't work because pulse is held by ``user1``. \* If you are using
``tmux``, as done by most of the STRANDS systems, not only the two
points above apply but if you start ``tmux`` via ssh with activated X
forwarding, mary will try to access the pulse resource on the remote
machine. try to always start the tmux session on the robot or PC that is
supposed to run mary as the user that is supposed to run mary and is
currently logged in. If you want to start it remotely, make sure not to
use X forwarding.

If MARY server is only binding to IP6, you can force it to bind to IP4
(from http://superuser.com/a/453329):

::

    export _JAVA_OPTIONS="-Djava.net.preferIPv4Stack=true"


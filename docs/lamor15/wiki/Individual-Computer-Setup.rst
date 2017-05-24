The school organisers prepared the robots to be available to the
individual groups with all software and hardware readily installed. Each
participant, in order to be able to work in the team, should be
following the installation instructions detailed below for their own PC:

1. Install Ubuntu Linux 14.04LTS 64bit on your computer. Please make
   sure that you have exactly this version installed: 14.04 for 64bit.
   Download the image from here: http://www.ubuntu.com/download/desktop.
   Note, that you can perfectly install Ubuntu 14.04 alongside an
   existing operating system (even on a MacBook).
2. Follow the instructions at
   https://github.com/strands-project-releases/strands-releases/wiki#using-the-strands-repository
   to install both ROS and the STRANDS software packages. We assume a
   basic understanding of Unix-like operating systems and shell usage
   here. If you need help using the command line, this might be a good
   start: https://help.ubuntu.com/community/UsingTheTerminal. The
   relevant installation steps are copied below for your convenience:
3. Enable the ROS repositories: Accomplish steps 1.1-1.3 in
   http://wiki.ros.org/indigo/Installation/Ubuntu#Installation. No need
   to do the following steps after 1.3.
4. Enable the STRANDS repositories:

   1. Add the STRANDS public key to verify packages:
      ``curl -s http://lcas.lincoln.ac.uk/repos/public.key | sudo apt-key add -``
   2. Add the STRANDS repository:
      ``sudo apt-add-repository http://lcas.lincoln.ac.uk/repos/release``

5. update your index: ``sudo apt-get update``
6. install required packages:
   ``sudo apt-get install ros-indigo-desktop-full ros-indigo-strands-desktop``
7. Try out the “MORSE” simulator (run all the following in your
   terminal):
8. configure ROS: ``source /opt/ros/indigo/setup.bash``
9. launch the simulator:
   ``roslaunch strands_morse uol_mht_morse.launch`` You should see the
   Morse simulator popping up with our robot platform being configured.
   If your graphics card cannot handle the simulation properly, please
   try the “fast mode”, using this command instead:
   ``roslaunch strands_morse uol_mht_morse.launch env:=uol_mht_nocam_fast``

If your laptop uses an NVidia graphics card it might be worth looking
at: https://wiki.ubuntu.com/Bumblebee to use it to its full potential.
You should be all set now!


Original page: https://github.com/strands-project/lamor15/wiki/Individual-Computer-Setup
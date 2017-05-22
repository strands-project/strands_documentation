Simple install script for MORSE and ROS for STRANDS
---------------------------------------------------

The easiest way to install MORSE is to use the install script
`here <https://gist.github.com/cburbridge/5782900#file-setup-sh>`__.
This gets all of the necessary packages, and installs Python 3.3,
Blender, and MORSE in a user directory. It also installs ROS Groovy in
/opt.

1. Download the script
   `setup.sh <https://gist.github.com/cburbridge/5782900#file-setup-sh>`__
2. Create a directory in home under which packages will be installed.
   The directory will later contain the sub-directories bin/ include/
   lib/ opt/ share/ src/ tmp/, following the usual filesystem structure.
3. Open a terminal, cd to the newly created directory and execute the
   install script. During install, your password will be requested to
   install ROS in /opt using the official packages. After all the
   components are installed, your directory will have a .bashrc file
   inside it. Sourcing this file sets the PATH etc in the shell session.
   The install script sets up automatic sourcing of this file at the end
   of your ~/.bashrc file.
4. Open a new terminal and run

   morse check

This should tell you that your environment is setup correctly. :-)

5. get yourself a github account (https://github.com) and send your
   account name to marc@hanheide.net

The manual way
--------------

...

Issues and solutions
--------------------

-  ``Cannot find a MORSE environment or simulation scene matching <strands_sim>!``
-  add the path to ``strands_sim`` in ``~/.morse/config``. This is done
   by going into the strands\_sim directory,
-  To easily achieve this do:

   -  run ``morse create test``: this will create the setupfile you need
      by creating a dummy morse project.
   -  You can then remove the newly created created dummy project by
      ``rm -rf test/``
   -  Now its time to edit the config file that was created to work with
      your path to the strands morse project, do this by:
      ``gedit ~/.morse/config``
   -  change the path and name to fit your installation in
      ``.morse/config``. For me this file looks like this:
      ``[sites]     strands_sim = /home/johane/strands/strands_morse/strands_sim``

-  Run bham morse sim with ros:
-  Create a directory like: ``strands/sim/src`` and cd to that
-  clone the git repository to this location
   ``git clone git://github.com/strands-project/strands_morse.git`` and
   ``cd strands_morse``
-  create a src dir and move everything into it:
   ``mkdir src && mv * src``
-  go to strands/sim/src and run ``catkin_init_workspace``
-  go to strands/sim and run ``catkin_make``
-  source the ros environment: ``source devel/setup.bash``
-  run it: ``rosrun strands_sim simulator.sh``


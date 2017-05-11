BHAM CS Building Simulation with Moving Lift
============================================

Setup
-----

The following additional setup is required in addition to the STRANDS
standard Morse install.

PySide
~~~~~~

PySide is needed for the control manager GUI. It must be installed from
source for the STRANDS install of Python 3.3:

1) Install system depends

::

    sudo apt-get install build-essential git cmake libqt4-dev libphonon-dev libxml2-dev libxslt1-dev qtmobility-dev

2) Install Python3.3 setuptools:

::

    cd /opt/strands/tmp  # OR THE PLACE YOU CHOSE
    wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
    python3.3 ez_setup.py

3) Build & Install PySide (this takes a while)

::


    wget https://pypi.python.org/packages/source/P/PySide/PySide-1.2.1.tar.gz
    tar -xvzf PySide-1.2.1.tar.gz
    cd PySide-1.2.1
    python3.3 setup.py install --qmake=/usr/bin/qmake-qt4

Using the Lift
--------------

1) Start Morse with all floors of the CS building:

::

    roslaunch strands_morse bham_cs_morse.launch env:=cs

2) Start the 'Lift Controller' - a small program that maintains a queue
   of lift calls and commands through ROS, and passes them on to Morse.

::

    rosrun strands_morse lift_controller.py

3) Launch the control interface

::

    rosrun strands_morse bham_control_gui.py

The control GUI allows you to \* Hide / Show different floors of the
building - Top row of buttons \* Call the lift to a floor (ie. press the
button outside the lift) - Second row of buttons \* Command the lift to
a floor (ie. press a button inside the lift) - Bottom row of buttons.

How the Lift works
------------------

The lift acts as a "robot" within the environment, with
``morse.core.actuator.Actuator``\ s to control the doors and the lift
platform. These actuators provide services to open and close doors, and
to move the lift platform between floors, exposed as Morse RPC functions
using the basic morse socketstream 'middleware'.

The 'Lift Controller' uses the morse middleware through the pymorse
library to command the lift between floors. It receives floor requests
through ROS topics, subscribing to:

::

    /lift_sim/[command|call]floor : std_messages/Bool

where floor is [B\|G\|1\|2]. For example, ``/lift_sim/callG``.

The topics correspond to a user pressing the "call" button on the
outside of the lift on floor, or the "command" button on the inside of
the lift to got to "floor".

The controller maintains a simple queue and moves the lift in the order
requested, and waits a minimum of 8 seconds before closing the door
between floor visits.

Installing
==========

Tonight I installed and ran MORSE (up to the first tutorial at least)
under OSX. This was done using Homebrew. The steps I took were as
follows

1. Download Blender from the `Blender download
   page <http://www.blender.org/download/get-blender/>`__, and copy the
   apps to /Applications. I used Blender 2.67a 64 bit.

2. As that Blender uses Python 3.3.0 you need to install the exact
   matching version for your system. I did this using
   `Homebrew <http://brew.sh>`__. You have to go through some extra
   steps as the current version of Python is 3.3.1. The hash for the
   checkout command comes from ``brew versions python3``.

.. code:: bash

    $ cd /usr/local
    $ git checkout 864e9f1 /usr/local/Library/Formula/python3.rb
    $ brew install python3

Then make sure pkg-config can find this install

.. code:: bash

    $ export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/Cellar/python3/3.3.0/Frameworks/Python.framework/Versions/3.3/lib/pkgconfig

I also had to remove my Python 2.7 packages from my environment as cmake
failed:

.. code:: bash

    unset PYTHONPATH

3. I installed MORSE using the `manual installation
   instructions <http://www.openrobots.org/morse/doc/stable/user/installation.html#manual-installation>`__.
   However, I needed a bit of a hack to get this working. First, the
   compiled Python modules wouldn't link against the Python libs, so I
   edit line 261 of ``config/FindPythonLibs.cmake`` to be the following

   ::

       TARGET_LINK_LIBRARIES(${_NAME} python3.3m)

   There's probably a more elegant way of fixing this, but I didn't look
   for it. I then ran ``ccmake`` as follows

   ::

       $ mkdir build && cd build
       $ ccmake -DPYTHON_INCLUDE_DIR=/usr/local/Cellar/python3/3.3.0/Frameworks/Python.framework/Versions/3.3/include/python3.3m -DPYTHON_LIBRARY=/usr/local/Cellar/python3/3.3.0/Frameworks/Python.framework -DBUILD_ROS_SUPPORT=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/morse -DPYTHON_EXECUTABLE=/usr/local/bin/python3.3  -DCMAKE_MODULE_LINKER_FLAGS=`pkg-config --libs python3` ..
       $ sudo make install

4. To allow MORSE to find Blender I set ``MORSE_BLENDER`` as follows:

   .. code:: bash

       $ export MORSE_BLENDER=/Applications/blender.app/Contents/MacOS/blender

5. At this point ``morse check`` should succeed (despite some minor
   Blender complaints), and you can run the `basic
   tutorial <http://www.openrobots.org/morse/doc/stable/user/beginner_tutorials/tutorial.html>`__:

   .. code:: bash

       $ morse run /opt/share/morse/examples/tutorials/tutorial-1-sockets.py 

   and in another terminal

   .. code:: bash

       $ telnet localhost 4000

   followed by

   ::

       id1 atrv.motion set_speed [2, -1]

   This should make your robot go in a circle in the simulation.

ROS Integration
===============

Although the above worked for me, I couldn't run the CS sim with ROS
integration. This seemed to be because Python 3 couldn't load some of
the installed Python 2.7 packages (I installed ROS from source following
instructions
`here <http://www.ros.org/wiki/groovy/Installation/OSX/Homebrew/Source>`__).
To fix my issues I had to do the following

.. code:: bash

    $ pip3 install PyYAML rospkg catkin_pkg

I have then been running with the following PYTHONPATH (the first seems
necessary as the ROS install doesn't do things quite right).

.. code:: bash

    $ export PYTHONPATH=/opt/ros/groovy/lib/python2.7/site-packages:/usr/local/lib/python2.7/site-packages

I also had to change ``strands_sim/morse_config.py`` so that the first
line launches python3 from the location Homebrew installed it, i.e.

::

    #!/usr/local/bin/python3

I suspect there's a more elegant way of doing this.

Current Issues
==============

The rendering of Blender/MORSE seems a bit odd on my 15" rMBP as I only
see the simulation in a quarter of the window. This problem goes away
when running on an external display though. Logged here:
https://github.com/laas/morse/issues/383

Problems
========

If you see an error like the following

::

    Traceback (most recent call last):
      File "/opt/bin/morse", line 825, in <module>
        args.func(args)
      File "/opt/bin/morse", line 645, in do_check
        check_setup()
      File "/opt/bin/morse", line 275, in check_setup
        blender_prefix = os.path.join(os.path.normpath(prefix), os.path.normpath("bin/blender"))
    NameError: global name 'prefix' is not defined

it means that MORSE can't find Blender. Set ``MORSE_BLENDER`` as above.

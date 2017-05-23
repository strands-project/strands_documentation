STRANDS User Interfaces
=======================

User interfaces for the robots, displayed using a web browser.

Installation
============

You can add the STRANDS UI source to your catkin workspace (if it's not
there already) using ``wstool``:

.. code:: bash

    wstool merge https://raw.github.com/hawesie/strands_ui/master/strands_ui_rosinstall.yaml
    wstool update strands_ui twitter_bootstrap

``rosdep`` should give you most requirements as usual (e.g.
``rosdep install --from-paths src --ignore-src --rosdistro groovy -y -r``),
but we don't yet have a rosdep for `web.py <http://webpy.org>`__ which
is required by ``strands_webserver``. This can be installed using, e.g.,

.. code:: bash

    sudo apt-get install python-webpy

or

::

    sudo pip install web.py

You can then run ``catkin_make`` as usual.

strands\_webserver
==================

The ``strands_webserver`` is a node which both acts as a webserver and a
ROS node which can receive input from other nodes. This allows these
other nodes to control what the webserver displays and receive feedback
from user interaction with the pages.

Running
-------

To run the server, first run rosbrige if you don't have it running
already.

::

    roslaunch rosbridge_server rosbridge_websocket.launch

Then run the server

.. code:: bash

    rosrun strands_webserver strands_webserver 

This will launch the webserver on localhost port 8090, so browse to
http://localhost:8090 and you should see something like

.. code:: text

    Ready; display = 1

Displaying content
------------------

The webserver manages individual *displays* separately, one for each
request to its URL. These can be published to individual by specifying
their number, or you can just send 0 to publish to all of them.

Interaction with ``strands_webserver`` typically happens by publishing
instructions to it for display. These can either be URLs or bits of html
which will be injected into its main page. The URLs are loaded in a full
size iframe. The bits of html are injected as the ``innerHTML`` of the
``content`` node in the main page
(``strands_webserver/data/main.html``).

The example below shows how to publish a simple html page to the
webserver, both a normal URL (given that it is happy to appear in an
iframe) then a page defined locally.

.. code:: python

    #! /usr/bin/env python

    import sys
    import os
    import roslib
    import rospy

    import strands_webserver.client_utils

    if __name__ == '__main__':
        rospy.init_node("strands_webserver_demo")
        # The display to publish on, defaulting to all displays
        display_no = rospy.get_param("~display", 0) 

        # display a start-up page
        strands_webserver.client_utils.display_url(display_no, 'http://strands-project.eu')

        # sleep for 2 seconds
        rospy.sleep(5.)

        # tell the webserver where it should look for web files to serve
        http_root = os.path.join(roslib.packages.get_pkg_dir("strands_webserver"), "data")
        strands_webserver.client_utils.set_http_root(http_root)

        # start with a basic page pretending things are going normally
        strands_webserver.client_utils.display_relative_page(display_no, 'example-page.html')

To display arbitrary HTML within the the ``content`` node in the main
page (``strands_webserver/data/main.html``) you can use calls like the
following

.. code:: python

    strands_webserver.client_utils.display_content(display_no, '<p>Hello world</p>') 

Note that any ``script`` nodes will not be evaluated in this injected
html.

Using the Webloader action server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The webloader action server offers 4 ways of manipultating webpages
shown by the webserver (all of this of course only works if you
exclusivly use the webloader server to display pages): \* Loading
relative or contant generated pages \* Reloading the current page \*
Going back to the previous page \* Showing a temporary page for a
specific number of seconds

Usage still requires your main programm to set

::

        http_root = os.path.join(roslib.packages.get_pkg_dir("my_package"), "directory")

Currently all these pages are sent to all displays. Possible future
extensions could therefore include a history for each display.

Every of the above mentioned actions has their own action file.
Reloading and going back are just empty actions. Loading a page reuires
to specify ``goal.relative=BOOL`` to toggle between relative and content
generated pages and ``goal.page=STRING`` is either the name of the
relative page or the content for the generated page. For the temporary
page you also have to specify ``goal.timeout=INT`` after which the
previous page will be shown again.

This action server was developed to manage the user interface for the
NHM deployment where people could trigger to tweet an image. This was
displayed on a temporary page and afterwards the display was reset to
the previous page. This had the advantage of showing arbitrary pages
without care about what should be displayed afterwards.

Auto-generated button pages
---------------------------

The ``strands_webserver`` package also provides functionality for
automatically generating pages with buttons which can call services.
Such a call might look like this

.. code:: python

        notice = 'Help me, I am <em>stuck</em>'
        buttons = [('No', 'trigger_pleading'), ('Sure', 'party_time')]
        service_prefix = '/caller_services'
        content = strands_webserver.page_utils.generate_alert_button_page(notice, buttons, service_prefix)  
        strands_webserver.client_utils.display_content(display_no, content) 

In this ``notice`` is the used to generate a large banner notice and
``buttons`` maps between a button label (e.g. No) and the service call
which will be triggered when the button is pressed, e.g.
(``'/caller_services/trigger_pleading'``). This service is of type
``std_srvs/Empty``. Instead of ``generate_alert_button_page`` you can
use ``generate_button_page`` which accepts arbitrary html instead of a
banner notice.

The full example is as follows (also available as
``strands_webserver/scripts/strands_webserver_demo.py``).

.. code:: python

    #! /usr/bin/env python

    import sys
    import os
    import roslib
    import rospy

    import strands_webserver.page_utils
    import strands_webserver.client_utils
    import std_srvs.srv 


    def trigger_pleading(req):
          print 'please, please help'


    def party_time(req):
          print 'woo, off I go baby'


    if __name__ == '__main__':
        rospy.init_node("strands_webserver_demo")
        # The display to publish on, defaulting to all displays
        display_no = rospy.get_param("~display", 0) 

        # display a start-up page
        strands_webserver.client_utils.display_url(display_no, 'http://strands-project.eu')

        # sleep for 5 seconds
        rospy.sleep(5.)

        # tell the webserver where it should look for web files to serve
        http_root = os.path.join(roslib.packages.get_pkg_dir("strands_webserver"), "data")
        strands_webserver.client_utils.set_http_root(http_root)

        # start with a basic page pretending things are going normally
        strands_webserver.client_utils.display_relative_page(display_no, 'example-page.html')

        # sleep for 5 seconds
        rospy.sleep(5.)

        # now ask for help
        name = 'Help me, I am <em>stuck</em>'
        buttons = [('No', 'trigger_pleading'), ('Sure', 'party_time')]
        service_prefix = '/caller_services'
        content = strands_webserver.page_utils.generate_alert_button_page(name, buttons, service_prefix)    
        strands_webserver.client_utils.display_content(display_no, content) 
        rospy.Service('/caller_services/trigger_pleading', std_srvs.srv.Empty, trigger_pleading) 
        rospy.Service('/caller_services/party_time', std_srvs.srv.Empty, party_time) 
        rospy.spin()

Includes
--------

Need to describe where the webserver fetches javascript and css from,
and the standard includes available.

marathon\_touch\_gui
====================

This package uses the ``strands_webserver`` to create an interface for
the patroller during the marathon event. It's not very pretty, but it's
a start. There is a main page (map, pause button) which is displayed
using ``strands_webserver.client_utils.display_relative_page`` and two
pages for recovery methods which are generated using
``strands_webserver.page_utils.generate_alert_button_page``. These are
wrapped up in ``marathon_touch_gui.client`` for ease of use. They can be
called as follows:

.. code:: python

        # Setup -- must be done before other marathon_touch_gui calls
        marathon_touch_gui.client.init_marathon_gui()

        # Show the main page of the GUI
        marathon_touch_gui.client.display_main_page(displayNo)

        rospy.sleep(2)
        
        # All callback services should be under this prefix
        service_prefix = '/patroller'

        # Do something like this on bumper collision

        # when the human gives the 'ok' then /patroller/bumper_recovered is called
        # note that this service must be provided by some other node
        on_completion = 'bumper_recovered'
        marathon_touch_gui.client.bumper_stuck(displayNo, service_prefix, on_completion)

        rospy.sleep(2)

        # Do something like this on move_base failure

        # when the human gives the 'ok' then /patroller/robot_moved is called
        # note that this service must be provided by some other node
        on_completion = 'robot_moved'
        marathon_touch_gui.client.nav_fail(displayNo, service_prefix, on_completion)

        rospy.sleep(2)

        # Return to main page
        marathon_touch_gui.client.display_main_page(displayNo)

The full example is in ``marathon_touch_gui/scripts/demo.py``

Running
-------

To run the marathon GUI, first launch ``strands_webserver`` plus
rosbridge and the necessary additional publishers (with HOST\_IP set to
an external ip for your machine if you want this to be externally
accessible, else leave blank for 127.0.0.1):

.. code:: bash

    HOST_IP=10.0.11.158 roslaunch marathon_touch_gui marathon_gui_dependencies.launch

This will launch the webserver on localhost port 8090, so browse to
http://localhost:8090.

Then you can call the ``marathon_touch_gui`` functions. To test you can
cycle through them with

.. code:: bash

    rosrun marathon_touch_gui demo.py 

Modal Dialog
------------

By publishing a ``strands_webserver/ModalDlg`` message on the
``/strands_webserver/modal_dialog`` topic a modal dialog can be
triggered hovering above any window display. This is useful for system
notifications. The ``strands_webserver/ModalDlg`` is defined as follows:

::

    string title
    string content
    bool show

The modal dialog can be closed by the user using a little close item in
the top right corner, it can remotely be hidden, by setting ``show`` to
false. Here is an example to display the dialog box:

::

    rostopic pub /strands_webserver/modal_dialog strands_webserver/ModalDlg "title: 'Nice Title'
    content: '<b>test</b> <a href="https://github.com/strands-project/aaf_deployment">AAF</a>'
    show: true"

To hide it again, simply publish

::

    rostopic pub /strands_webserver/modal_dialog strands_webserver/ModalDlg "title: ''
    content: ''
    show: false"

Both, title and content can contain valid HTML.


Original page: https://github.com/strands-project/strands_ui/blob/hydro-devel/README.md
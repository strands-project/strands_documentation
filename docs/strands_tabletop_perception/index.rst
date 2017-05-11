STRANDS Tabletop Perception
===========================

Tabletop perception for STRANDS. The tabletop perception is realised as
a ROS action server. Given the information about a table in the
environment, i.e. its pose and its shape specified as a polygon, the
robot plans multiple views to perceive the tabletop, segments the data
from the depth camera at each of the planned views, and classifies the
extracted segments for a given set of object classes. The individual
components of the system are described below.

The information about the tables is stored in the ros datacentre
(MongoDB). This information can either be added through the autonomous
table detection or a manual process using a marker (cf. to the
descriptions below).

Finding/Storing Tables
----------------------

Tables are stored in the datacentre as strands\_perception\_msgs/Table
messages, using the MessageStore system.

Manually inserting tables into the datacentre:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few possible ways this can be done:

**OPTION A**) Use RoboMongo or any MongoDB client to create a new Table
message inside the message\_store collection inside the message\_store
database. Create a document that looks like:

::

     {
        "_id" : ObjectId("533c147c9f9d51517be039af"),
        "header" : {
            "stamp" : {
                "secs" : 0,
                "nsecs" : 0
            },
            "frame_id" : "/map",
            "seq" : 0
        },
        "pose" : {
            "pose" : {
                "position" : {
                    "y" : -5.604931354522705,
                    "x" : 5.736222267150879,
                    "z" : 1.433120727539062
                },
                "orientation" : {
                    "y" : 0.6713822484016418,
                    "x" : 0.7393708229064941,
                    "z" : 0.04276063665747643,
                    "w" : 0.02735294029116631
                }
            },
            "covariance" : [ 
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0
            ]
        },
        "table_id" : "lg_table_8",
        "tabletop" : {
            "points" : [ 
                {
                    "y" : 0,
                    "x" : 0,
                    "z" : 0
                }, 
                {
                    "y" : 1,
                    "x" : 0,
                    "z" : 0
                }, 
                {
                    "y" : 1,
                    "x" : 1,
                    "z" : 0
                }, 
                {
                    "y" : 0.2000000029802322,
                    "x" : 1,
                    "z" : 0
                }, 
                {
                    "y" : 0,
                    "x" : 0,
                    "z" : 0
                }
            ]
        },
        "_meta" : {
            "stored_type" : "strands_perception_msgs/Table",
            "stored_class" : "strands_perception_msgs.msg._Table.Table"
        }
    }

**OPTION B**) Create a Table message in your program and use the message
store proxy classes to insert it:

.. code:: python

    from strands_perception_msgs.msg import Table
    from geometry_msgs.msg import PoseWithCovariance, Polygon

    from mongodb_store.message_store import MessageStoreProxy

    my_table = Table()
    my_table.table_id = "MagicTable1"
    my_table.header.frame_id = "/map"  # The parent frame that the table is in

    table_pose = PoseWithCovariance()  # The transformation to the table frame
    # Fill in the table position...
    my_table.pose = table_pose

    polygon = Polygon()                # The table top surrounding polygon in the table frame
    # Fill in the points in the polygon....
    my_table.tabletop = polygon

    _msg_store = MessageStoreProxy()
    # Store the table
    _msg_store.insert(my_table)
            

Semi-automatic table insertion:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``manual_table_storer`` package provides a script to create tables
at locations given by a calibration board/chessboard. This avoids the
need to work out where the table is in space, but does still require the
manual measurements of the table plane polygon.

To do so:

1) Checkout and compile the chessboard detection code into your catkin
   workspace:

``bash roscd cd ../src git clone https://github.com/cburbridge/chessboards cd .. catkin_make``

2) Measure your chosen table's top, choosing an origin point. +z will
   point down, so +y will be clockwise to +x. Write down the
   co-ordinates of the table top:

.. figure:: https://github.com/strands-project/strands_tabletop_perception/raw/hydro-devel/images/tables.png
   :alt: table

   table

3) Add your new table top to the top of store.py file:

.. code:: python

    TABLES["LGType4"]=[(0,0,0),
                       (0.4,0,0),
                       (0.4,0.6,0),
                       (-1.0,.6,0),
                       (-1,-1.0,0),
                       (-0.4,-1,0),
                       (-0.4,-0.6,0)]

4) Launch the table store program with the table type and the new name
   for the table:

::

    rosrun manual_table_storer store.py LGType my_magic_table

5) Print out an A3 calibration pattern, found in
   ``chessboards/chessboards/boards/A3 cal.pdf``. Stick it to some card.

6) Place the calibration pattern on to the table, with the centre of the
   board at your origin and the x & y axis aligned with your axis. See
   image above.

7) Make sure your robot is well localised in the 2D map then run the
   chessboard detector:

::

    roslaunch chessboard_pose detect_a3_8_5.launch 

When the image shows the chessboard highlighted in rainbow colours, it
has been found. At that point, the storer node will store and exit.

Autonomous table detection (KTH, Nils)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See
`README <https://github.com/strands-project/strands_tabletop_perception/blob/hydro-devel/table_detection/README.md>`__.

Table Visualisation and Tweeking
--------------------------------

Once tables are inside the datacentre, they can be manually moved about
using the ``visualise_tables`` package.

To visualise the tables, without the option to move them (safer):

::

    rosrun visualise_tables visualise.py

To visualise the tables with interactive markers enabled to move the
table:

::

    rosrun visualise_tables visualise.py edit

In RViz, add an InteractiveMarkers display and set the Update Topic to
``/table_markers/update``. If enabled, dragging the table about updates
the datacentre.

View planning for tabletop perception (BHAM, Lars)
--------------------------------------------------

1. Make sure that you have the table information available in the ros
   datacentre

2. Make sure that you have a octomap server running with a local 3D map:

   ::

       roslaunch perceive_tabletop_action octomap.launch

3. Launch the view planning components and action server:

   ::

       roslaunch perceive_tabletop_action perceive_tabletop.launch

3D Object recognition (TUW, Aitor, Thomas, Michael)
---------------------------------------------------

Run the 'perceive tabletop' action
----------------------------------

Run the tabletop action client with a table id (known by the ros
datacentre):

::

    rosrun perceive_tabletop_action PerceiveTabletopActionClient.py test_lg_1

Visualisation of the viewplanning in RVIZ:

.. figure:: https://github.com/strands-project/strands_tabletop_perception/raw/hydro-devel/images/viewplanning_rviz.png
   :alt: table

   table
Appendix: table and object data management using MongoDB (BHAM, Chris)
----------------------------------------------------------------------

On route.

Topological Map
===============

A topological map in the strands system is published over the
'/topological\_map' topic its ros message is type defined the following
`way <https://github.com/strands-project/strands_navigation/blob/indigo-devel/strands_navigation_msgs/msg/TopologicalMap.msg>`__:

::

    string name          # topological map name generally should be the same as in the pointset field
    string map           # 2D Metric map name (not used currently)
    string pointset      # The name of the group of nodes that compose the topological map, typically the same as name
    string last_updated  # Last time the map was modified
    strands_navigation_msgs/TopologicalNode[] nodes  # The group of nodes that composes the topological map

Topological Nodes
-----------------

The nodes are the locations to which the robot should navigate on its
working environment these location are related to coordinates in the
robot map frame, the nodes are defined as a ros message in the following
[way]
(https://github.com/strands-project/strands\_navigation/blob/indigo-devel/strands\_navigation\_msgs/msg/TopologicalNode.msg)

::

    string name                 # Node name
    string map                  # 2D Metric map name (not used currently)
    string pointset             # The name of the group of nodes that compose the topological map
    geometry_msgs/Pose pose     # Node X,Y,Z,W coordinates in the map frame
    float64 yaw_goal_tolerance  # The tolerance in radians for the waypoint position
    float64 xy_goal_tolerance   # The tolerance in meters for the waypoint position
    Vertex[] verts              # X,Y coordinates for the vertices of the influence zone relative to the node pose
    Edge[] edges                # The group of outward oriented edges connecting this node to others
    string localise_by_topic    # The configuration for localisation by topic 

Edges
-----

The edges are the definitions for the connections between nodes,
typically this connections are included in the node message, which means
that the edges defined for each node are the ones on which the node they
are defined at is the point of origin, they are also defined as a ros
message type in the following
`way <https://github.com/strands-project/strands_navigation/blob/indigo-devel/strands_navigation_msgs/msg/Edge.msg>`__

::

    string edge_id                        # An identifier for the edge
    string node                           # Name of destination node
    string action                         # Name of navigation action, e.g. move_base
    float64 top_vel                       # Maximum speed in [m/s]
    string map_2d                         # Name of the 2D map 
    float64 inflation_radius              # Obstacle inflation radius on this edge, 0 for default
    string recovery_behaviours_config     # Not currently used, typically a json string

YAML format
===========

the topological map can also be defined in yaml format, this is used to
export and manually modify maps a map on this format would look like
this:

.. code:: YAML

    - meta:
        map: mb_arena
        node: Start
        pointset: mb_test2
      node:
        edges:
        - action: move_base
          edge_id: Start_End
          inflation_radius: 0.0
          map_2d: mb_arena
          node: End
          recovery_behaviours_config: ''
          top_vel: 0.55
        localise_by_topic: ''
        map: mb_arena
        name: Start
        pointset: mb_test2
        pose:
          orientation:
            w: 0.92388
            x: 0
            y: 0
            z: 0.38268
          position:
            x: -1.5
            y: 2.6
            z: 0.0
        verts:
        - x: 0.689999997616
          y: 0.287000000477
        - x: 0.287000000477
          y: 0.689999997616
        - x: -0.287000000477
          y: 0.689999997616
        - x: -0.689999997616
          y: 0.287000000477
        - x: -0.689999997616
          y: -0.287000000477
        - x: -0.287000000477
          y: -0.689999997616
        - x: 0.287000000477
          y: -0.689999997616
        - x: 0.689999997616
          y: -0.287000000477
        xy_goal_tolerance: 0.3
        yaw_goal_tolerance: 0.1
    - meta:
        map: mb_arena
        node: End
        pointset: mb_test2
      node:
        edges:
        - action: move_base
          edge_id: End_Start
          inflation_radius: 0.0
          map_2d: mb_arena
          node: Start
          recovery_behaviours_config: ''
          top_vel: 0.55
        localise_by_topic: ''
        map: mb_arena
        name: End
        pointset: mb_test2
        pose:
          orientation:
            w: 0.70711
            x: 0.0
            y: 0.0
            z: -0.70711
          position:
            x: -1.5
            y: -0.5
            z: 0.0
        verts:
        - x: 0.689999997616
          y: 0.287000000477
        - x: 0.287000000477
          y: 0.689999997616
        - x: -0.287000000477
          y: 0.689999997616
        - x: -0.689999997616
          y: 0.287000000477
        - x: -0.689999997616
          y: -0.287000000477
        - x: -0.287000000477
          y: -0.689999997616
        - x: 0.287000000477
          y: -0.689999997616
        - x: 0.689999997616
          y: -0.287000000477
        xy_goal_tolerance: 0.3
        yaw_goal_tolerance: 0.1

All the fields correspond to the definitions presented before, please
note that each node has a "meta" field.

Node Meta information
~~~~~~~~~~~~~~~~~~~~~

Each node is stored in the datacentre with additional meta information,
in the YAML version of a topological map this meta information *MUST* be
included with at lest the three fields shown in the map, however any
other meta information can be added as long as it is included in a valid
YAML format for example:

.. code:: YAML

    - meta:
        map: mb_arena
        node: End
        pointset: mb_test2
        example: 'this is an example field'



Original page: https://github.com/strands-project/strands_navigation/wiki/Topological-Map-Definition
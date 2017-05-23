This package visualizes all points of the point clouds in directory
*my\_input\_dir* that have a corresponding file with saved point indices
(file prefix: *object\_indices\_*).

::

    _my_input_dir
    |
    +-- _apple
    |   +-- 000.pcd
    |   +-- 001.pcd
    +-- _banana
    |   +-- 000.pcd
    |   +-- 001.pcd
    |   +-- 002.pcd
    +-- _mug
    |   +-- 000.pcd
    |   +-- 001.pcd
    +-- _mouse
    |   +-- 000.pcd
    |   +-- 001.pcd
    |   +-- 002.pcd
    |   +-- 003.pcd
     ```

    For instance:

    To show all point clouds of all classes, run:

rosrun visualize\_pcd\_indices visualize\_pcd\_indices\_node
*dir:=my*\ input\_dir

::


    to show all point clouds of a particular class (e.g. banana), run:

rosrun visualize\_pcd\_indices visualize\_pcd\_indices\_node
*dir:=my*\ input\_dir/banana \`\`\`

One possibility to compute the indices of the point cloud above a table
plane is to use the catkin package *pcd\_filter*
(https://github.com/strands-project/strands\_tabletop\_perception/tree/hydro-devel/pcd\_filter).


Original page: https://github.com/strands-project/strands_tabletop_perception/blob/hydro-devel/visualize_pcd_indices/README.md
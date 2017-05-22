This package filters points from a point cloud and can be used for
processing training data for the object classifier. It saves the indices
of the point cloud that are on the heighest table plane parallel to the
largest plane (this will mostly be the floor) and within a distance
*chop\_z\_max* from the camera. It saves these point indices as *.pcd
file in the same folder as the input files adding a filename prefix
*\ object\_indices\_\*. This file is later used for the object
classifier to train the objects.

To gather input data, put your training objects individually on an empty
plane (e.g. floor) and grab the point clouds with a pcd grabber. Put
them into a directory structure like:

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

    Finally, filter the pcd files in *my\_input\_dir* by running:

rosrun pcd\_filter pcd\_filter\_node *input*\ dir:=~/my\_input\_dir
*input*\ dir:=/home/thomas/Projects/v4r/trunk/bin/records/
*chop*\ z\_max:=1.1 *visualize:=true *\ force\_refilter:=true \`\`\` ,
where \*\_visualize\* can be set to visualize the filtered point clouds
and **force*\ refilter* to do a new filtering process for already
filtered .pcd files (i.e. pcd files where corresponding
*object\_indices\_* already exist).

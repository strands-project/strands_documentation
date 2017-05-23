It is based on the *object\_classifier* ros package (read instructions
there on how to train it).

You can launch the multi-view service, single-view service and
segmentation module as follows:

roslaunch mv\_object\_classifier
mv\_classifier\_from\_files\_demo.launch
models\_dir:=/media/DATA/Cat200\_ModelDatabase\_\ *small/
training*\ dir:=/media/DATA/Cat200\_ModelDatabase\_\ *small*\ trained/
chop\_z:=1 mv\_visualize\_output:=true

and then:

rosrun mv\_object\_classifier mv\_object\_classifier\_demo\_from\_file
\_folder:=${DATA}

where data should point to the data/mv\_seq1/ folder within this package
or any folder containing PCD files that will be used as input for the
multi-view classifier.


Original page: https://github.com/strands-project/strands_tabletop_perception/blob/hydro-devel/mv_object_classifier/README.md
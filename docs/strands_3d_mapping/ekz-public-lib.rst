------------- WARNING - SURF features disabled in this version
----------------

Section 1: License Section 2: Dependencies Section 3: BUILD Section 4:
SOURCE CODE Section 5: EXAMPLES Section 6: TODOLIST

-------------------------Section 1:
License------------------------------------

License: BSD

-------------------------Section 2:
Dependencies-------------------------------

Dependencies required: 1: Install ros hydro from:
http://wiki.ros.org/hydro/Installation/ 2: Install ros-pcl with: apt-get
install ros-hydro-perception-pcl 3: Install ros-opencv2: apt-get install
ros-hydro-opencv2

Optional(recommended): 4: Install ros openni: apt-get install
ros-hydro-openni-launch -------------------------Section 3:
BUILD-------------------------------------- Place in catkin src folder.
Use catkin\_make from catkin folder.

-------------------------Section 4: SOURCE
CODE-------------------------------- found in installation directory +
/src/ This section summarizes the contents of the src directory. For
each folder a summary of the contents are provided with a short list
important files that the user is likely to interact with.

+----+
| Fi |
| le |
| :  |
| ek |
| z. |
| h  |
| In |
| fo |
| :  |
| To |
| in |
| cl |
| ud |
| e  |
| li |
| br |
| ar |
| y  |
| ju |
| st |
| in |
| cl |
| ud |
| e  |
| ek |
| z. |
| h. |
| In |
| cl |
| ud |
| es |
| of |
| ot |
| he |
| r  |
| fi |
| le |
| s  |
| fo |
| r  |
| th |
| e  |
| li |
| br |
| ar |
| y. |
+----+

Folder:core Info: Contains core classes for the library. Important
Files:

Calibration.h //Calibration class, controls focal length etc

FrameInput.h //Contains the input of one frame. Got functions like
getXYZ(int w, int h), getPointCloud() etc.

RGBDFrame.h //Representation of a frame. Contains extracted information
for the frame such as segmentation and keypoints etc.

Transformation.h //Represents a transformation between two frames.

+----+
| Fo |
| ld |
| er |
| :F |
| ea |
| tu |
| re |
| De |
| sc |
| ri |
| pt |
| or |
| In |
| fo |
| :  |
| Co |
| nt |
| ai |
| ns |
| di |
| ff |
| er |
| en |
| t  |
| ty |
| pe |
| s  |
| of |
| fe |
| at |
| ur |
| e  |
| de |
| sc |
| ri |
| pt |
| or |
| s  |
| us |
| ed |
| by |
| th |
| e  |
| li |
| br |
| ar |
| y. |
| Im |
| po |
| rt |
| an |
| t  |
| fi |
| le |
| s: |
| Fe |
| at |
| ur |
| eD |
| es |
| cr |
| ip |
| to |
| r. |
| h  |
| // |
| Ba |
| se |
| cl |
| as |
| s  |
| fo |
| r  |
| Fe |
| at |
| ur |
| e  |
| de |
| sc |
| ri |
| pt |
| or |
| s, |
| co |
| nt |
| ai |
| ns |
| fu |
| nc |
| ti |
| on |
| s  |
| su |
| ch |
| as |
| di |
| st |
| an |
| ce |
| (F |
| ea |
| tu |
| re |
| De |
| sc |
| ri |
| pt |
| or |
| \* |
| ot |
| he |
| r\ |
| _d |
| es |
| cr |
| ip |
| to |
| r) |
| .  |
+----+

Folder:FeatureExtractor Info: Contains different types of feature
extractors to be chosen from by the library. Important files:
FeatureExtractor.h //Core class for feature extractors OrbExtractor.h
//Class used to extract Orb keypoints SurfExtractor.h //Class used to
extract Surf keypoints

+----+
| Fo |
| ld |
| er |
| :F |
| ra |
| me |
| Ma |
| tc |
| he |
| r  |
| In |
| fo |
| :  |
| Co |
| nt |
| ai |
| ns |
| re |
| gi |
| st |
| ra |
| ti |
| on |
| al |
| go |
| ri |
| th |
| ms |
| th |
| at |
| ta |
| ke |
| s  |
| tw |
| o  |
| fr |
| am |
| es |
| as |
| in |
| pu |
| ts |
| (n |
| o  |
| in |
| it |
| ia |
| l  |
| gu |
| es |
| s  |
| gi |
| ve |
| n) |
| .  |
| Im |
| po |
| rt |
| an |
| t  |
| fi |
| le |
| s: |
| Fr |
| am |
| eM |
| at |
| ch |
| er |
| .h |
| // |
| Co |
| re |
| cl |
| as |
| s  |
| fo |
| r  |
| Fr |
| am |
| e  |
| ma |
| tc |
| he |
| rs |
| AI |
| CK |
| .h |
| // |
| AI |
| CK |
| ba |
| se |
| im |
| pl |
| em |
| en |
| ta |
| ti |
| on |
| wi |
| th |
| ou |
| t  |
| he |
| ur |
| is |
| ti |
| c  |
| ma |
| tc |
| hi |
| ng |
| al |
| go |
| ri |
| th |
| m. |
| bo |
| wA |
| IC |
| K. |
| h  |
| // |
| AI |
| CK |
| im |
| pl |
| em |
| en |
| ta |
| ti |
| on |
| wi |
| th |
| he |
| ur |
| is |
| ti |
| c  |
| ma |
| tc |
| hi |
| ng |
| al |
| go |
| ri |
| th |
| m. |
| Fa |
| st |
| er |
| th |
| an |
| AI |
| CK |
| .h |
| .  |
+----+

Folder:Map Info: Contains Map3D classes. Important files: Map3D.h
//Basic map class. Contains many usefull functions to reduce the
complexity for the user. Registers frames added sequentially.

+----+
| Fo |
| ld |
| er |
| :  |
| my |
| ge |
| om |
| et |
| ry |
| In |
| fo |
| :  |
| Co |
| nt |
| ai |
| ns |
| ge |
| om |
| et |
| ry |
| cl |
| as |
| se |
| s  |
| su |
| ch |
| as |
| pl |
| an |
| es |
| an |
| d  |
| po |
| in |
| ts |
| .  |
| Al |
| so |
| co |
| nt |
| ai |
| ns |
| Ke |
| yp |
| oi |
| nt |
| s  |
| ba |
| se |
| cl |
| as |
| s. |
+----+

Folder:RGBDSegmentation Info: Contains RGBD segmentation algorithms to
be used on the RGBDFrames. Currently unused.

+----+
| Fo |
| ld |
| er |
| :T |
| ra |
| ns |
| fo |
| rm |
| at |
| io |
| nF |
| il |
| te |
| r  |
| In |
| fo |
| :C |
| on |
| ta |
| in |
| s  |
| re |
| gi |
| st |
| ra |
| ti |
| on |
| al |
| go |
| ri |
| th |
| ms |
| th |
| at |
| ta |
| ke |
| s  |
| tw |
| o  |
| fr |
| am |
| es |
| as |
| in |
| pu |
| ts |
| wi |
| th |
| an |
| in |
| it |
| ia |
| l  |
| tr |
| an |
| sf |
| or |
| ma |
| ti |
| on |
| an |
| d  |
| im |
| pr |
| ov |
| es |
| th |
| e  |
| so |
| lu |
| ti |
| on |
| .  |
| Cu |
| rr |
| en |
| tl |
| y  |
| un |
| us |
| ed |
| .  |
+----+

Folder:apps Info:Contains example code of how to use the library. See
Section 5 for details.

-------------------------Section 5:
EXAMPLES----------------------------------- found in installation
directory + /src/apps/ Unzip testdata.7z to gain access to some test
data to run the examples with.

====================image\_recorder.cpp==================== Summary:
Records data and stores it in .pcd files from a the rostopic
/camera/depth\_registered/points Input: path where to store recorded
data Output: png image pairs with RGBD data captured from a the rostopic
/camera/depth\_registered/points USAGE: Run roscore Run roslaunch
openni\_launch openni.launch Run image\_recorder program with an
argument telling the recorder where to store the data

====================pcd\_recorder.cpp==================== Summary:
Records data and stores it in .png files from a the rostopic
/camera/depth\_registered/points Input: path where to store recorded
data Output: captured pairs(depth and RGB) of .png files USAGE: Run
roscore Run roslaunch openni\_launch openni.launch Run pcd\_recorder
program with an argument telling the recorder where to store the data

====================example\_register\_pcd\_map.cpp====================
Summary: Minimalistic example for registering data provided in .pcd
files sequentially using a Map3D object. Input: a set of paths to pcd
files Output: .pcd file of aligned data USAGE: Run
example\_register\_pcd\_map program with a set of paths to pcd files to
be registed

====================example\_register\_images\_map.cpp====================
Summary: Minimalistic example for registering data provided in .png
files sequentially using a Map3D object. Input: a path to a folder where
png files with the correct names are located Output: .pcd file of
aligned data USAGE: Run example\_register\_images\_map program with an
argument telling the program where to find the data

====================example\_register\_pcd\_standalone.cpp====================
Summary: Example for registering data provided in .pcd files
sequentially. Input: a set of paths to pcd files Output: .pcd file of
aligned data USAGE: Run example\_register\_pcd\_map program with a set
of paths to pcd files to be registed

====================example\_register\_images\_standalone.cpp====================
Summary: Example for registering data provided in .png files
sequentially. Input: a path to a folder where png files with the correct
names are located Output: .pcd file of aligned data USAGE: Run
example\_register\_images\_map program with an argument telling the
program where to find the data

====================example\_register\_images\_fast\_map.cpp====================
Summary: Example for registering data provided in .png files
sequentially using a Map3D object using ORB features and AICK with bag
of words. Input: a path to a folder where png files with the correct
names are located a path+fileprefix to a folder where a pre trained bag
of words model is located Output: .pcd file of aligned data USAGE: Run
example\_register\_images\_fast\_map program with an argument telling
the program where to find the data

====================example\_bow\_images.cpp====================
Summary: Example for training a bag of words model for data provided in
.png files using a Map3Dbow. Input: a path to a folder where png files
with the correct names are located, a path/name for output, number of
files to read and a number to controll how what part of the frames given
will be used. Output: .pcd file of aligned data USAGE: Run
example\_bow\_images program with a path to a folder where png files
with the correct names are located, a path/name for output, number of
files to read and a number to controll how what part of the frames given
will be used.

-------------------------Section 1: TODOLIST -------------------------
Use trees to speed up word association during frame generation. Provide
more maptypes. Give option to provide initial guess for poses in map.


Original page: https://github.com/strands-project/strands_3d_mapping/blob/hydro-devel/ekz-public-lib/README.txt
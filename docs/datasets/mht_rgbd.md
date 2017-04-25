<!DOCTYPE html>

MHT Building RGB-D and laser dataset
------------------------------------

The MHT building dataset was collected for purposes of testing RGB-D mapping of changing environments. The dataset consists of 2D (laser scanner) and 3D (Asus Xtion) data collected by a SCITOS-G5 mobile robot. We provide the gathered data in form of rosbags.

* * * * *

### Dataset purpose

The intended use was to create a dataset to benchmark spatio-temporal representations of changing environments. The robot was patrolling a small office (see the video below) every 5 minutes. Each patrol started and ended at a charging station. During each patrol, the robot continuously collected its laser scans and odometric data. Moreover, it stopped at three different locations, took snapshots using its RGB-D sensor and attempted to detect people presence.

\

  ------------------------------------------------------------------------------------------------------------------------------------------------------
  <iframe width="640" height="360" src="https://www.youtube.com/embed/_tXOevb51rc?feature=player_detailpage" frameborder="1" allowfullscreen></iframe>
  MHT office night collections with 3D sweeps
  ------------------------------------------------------------------------------------------------------------------------------------------------------

* * * * *

### Dataset structure

The provided archives contain rosbags, which are zipped into separate files according to the day of the data collection and data type. Each rosbag with a 3D prefix contains a depth/color image, camera information, robot position, tf data, laser scan and person detection gathered by the robot at a location and time that is encoded in the rosbag name, which contains day, month, year, hour, minute and location id. For example, *3D\_23-08-13-15-20\_place\_2.bag* contains data gathered at location 2 on August 23 2013 at 15:20 o'clock. Each rosbag with a 2D prefix contains AMCL position estimates, robot odometry, tf data and laser scans. Day, month, year, hour and minute are part of the bag file name.

* * * * *

### Download

<table border="0" align="center">
<tr>
<td>
<table border="1" align="center" cellspacing="5">
<tr>
<td colspan="2" align="center">
**August 2013**

</td>
</tr>
<tr>
<td align="center">
[2D data Aug](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/2D_2013-08.zip)

</td>
<td align="center">
[3D data Aug](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-08.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-08-24](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/2D_2013-08-24.zip)

</td>
<td>
[3D\_2013-08-24](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-08-24.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-08-25](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/2D_2013-08-25.zip)

</td>
<td>
[3D\_2013-08-25](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-08-25.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-08-26](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/2D_2013-08-26.zip)

</td>
<td>
[3D\_2013-08-26](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-08-26.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-08-27](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/2D_2013-08-27.zip)

</td>
<td>
[3D\_2013-08-27](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-08-27.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-08-28](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/2D_2013-08-28.zip)

</td>
<td>
[3D\_2013-08-28](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-08-28.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-08-29](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/2D_2013-08-29.zip)

</td>
<td>
[3D\_2013-08-29](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-08-29.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-08-30](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/2D_2013-08-30.zip)

</td>
<td>
[3D\_2013-08-30](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-08-30.zip)

</td>
</tr>
</table>
</td>
<td width="30">
</td>
<td>
<table border="1" align="center" cellspacing="5">
<tr>
<td colspan="2" align="center">
**September 2013**

</td>
</tr>
<tr>
<td align="center">
[2D data Sep](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09.zip)

</td>
<td align="center">
[3D data Sep](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-09-01](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-01.zip)

</td>
<td>
[3D\_2013-09-01](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-01.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-09-02](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-01.zip)

</td>
<td>
[3D\_2013-09-02](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-02.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-09-03](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-01.zip)

</td>
<td>
[3D\_2013-09-03](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-03.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-09-04](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-01.zip)

</td>
<td>
[3D\_2013-09-04](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-04.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-09-05](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-01.zip)

</td>
<td>
[3D\_2013-09-05](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-05.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-09-06](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-01.zip)

</td>
<td>
[3D\_2013-09-06](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-06.zip)

</td>
</tr>
<tr>
<td align="right">
[2D\_2013-09-07](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-01.zip)

</td>
<td>
[3D\_2013-09-07](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/3D_2013-09-07.zip)

</td>
</tr>
</table>
</td>
<tr>
</table>

* * * * *

### Conditions of use

If you use the dataset for your research, please cite our [paper](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/paper.pdf) that describes the data collection in detail. We attached a [bibtex](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/MHT/paper.bib) record for your convenience.

* * * * *

This dataset is part of the larger [LCAS-STRANDS long-term dataset collection](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/index.html).

</p>


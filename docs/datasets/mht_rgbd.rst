MHT Building RGB-D and laser dataset
------------------------------------

The MHT building dataset was collected for purposes of testing RGB-D mapping of changing environments. The dataset consists of 2D (laser scanner) and 3D (Asus Xtion) data collected by a SCITOS-G5 mobile robot. We provide the gathered data in form of rosbags.

--------------

Dataset purpose
~~~~~~~~~~~~~~~

The intended use was to create a dataset to benchmark spatio-temporal representations of changing environments. The robot was patrolling a small office (see the video below) every 5 minutes. Each patrol started and ended at a charging station. During each patrol, the robot continuously collected its laser scans and odometric data. Moreover, it stopped at three different locations, took snapshots using its RGB-D sensor and attempted to detect people presence.

| 

+-----------------------------------------------+
+-----------------------------------------------+
| MHT office night collections with 3D sweeps   |
+-----------------------------------------------+

--------------

Dataset structure
~~~~~~~~~~~~~~~~~

The provided archives contain rosbags, which are zipped into separate files according to the day of the data collection and data type. Each rosbag with a 3D prefix contains a depth/color image, camera information, robot position, tf data, laser scan and person detection gathered by the robot at a location and time that is encoded in the rosbag name, which contains day, month, year, hour, minute and location id. For example, *3D\_23-08-13-15-20\_place\_2.bag* contains data gathered at location 2 on August 23 2013 at 15:20 o'clock. Each rosbag with a 2D prefix contains AMCL position estimates, robot odometry, tf data and laser scans. Day, month, year, hour and minute are part of the bag file name.

--------------

Download
~~~~~~~~

.. raw:: html

   <table border="0" align="center">

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <table border="1" align="center" cellspacing="5">

.. raw:: html

   <tr>

.. raw:: html

   <td colspan="2" align="center">

**August 2013**

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="center">

`2D data Aug <MHT/2D_2013-08.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td align="center">

`3D data Aug <MHT/3D_2013-08.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-08-24 <MHT/2D_2013-08-24.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-08-24 <MHT/3D_2013-08-24.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-08-25 <MHT/2D_2013-08-25.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-08-25 <MHT/3D_2013-08-25.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-08-26 <MHT/2D_2013-08-26.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-08-26 <MHT/3D_2013-08-26.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-08-27 <MHT/2D_2013-08-27.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-08-27 <MHT/3D_2013-08-27.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-08-28 <MHT/2D_2013-08-28.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-08-28 <MHT/3D_2013-08-28.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-08-29 <MHT/2D_2013-08-29.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-08-29 <MHT/3D_2013-08-29.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-08-30 <MHT/2D_2013-08-30.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-08-30 <MHT/3D_2013-08-30.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

.. raw:: html

   </td>

.. raw:: html

   <td width="30">

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <table border="1" align="center" cellspacing="5">

.. raw:: html

   <tr>

.. raw:: html

   <td colspan="2" align="center">

**September 2013**

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="center">

`2D data Sep <MHT/3D_2013-09.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td align="center">

`3D data Sep <MHT/3D_2013-09.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-09-01 <MHT/3D_2013-09-01.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-09-01 <MHT/3D_2013-09-01.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-09-02 <MHT/3D_2013-09-01.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-09-02 <MHT/3D_2013-09-02.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-09-03 <MHT/3D_2013-09-01.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-09-03 <MHT/3D_2013-09-03.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-09-04 <MHT/3D_2013-09-01.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-09-04 <MHT/3D_2013-09-04.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-09-05 <MHT/3D_2013-09-01.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-09-05 <MHT/3D_2013-09-05.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-09-06 <MHT/3D_2013-09-01.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-09-06 <MHT/3D_2013-09-06.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="right">

`2D\_2013-09-07 <MHT/3D_2013-09-01.zip>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

`3D\_2013-09-07 <MHT/3D_2013-09-07.zip>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

.. raw:: html

   </td>

.. raw:: html

   <tr>

.. raw:: html

   </table>

--------------

Conditions of use
~~~~~~~~~~~~~~~~~

If you use the dataset for your research, please cite our `paper <MHT/paper.pdf>`__ that describes the data collection in detail. We attached a `bibtex <MHT/paper.bib>`__ record for your convenience.

--------------

This dataset is part of the larger `LCAS-STRANDS long-term dataset collection <index.html>`__.

.. raw:: html

   </p>


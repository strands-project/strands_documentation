MHT building lecturer office
----------------------------

This dataset contains depth images captured by a stationary Asus Xtion sensor located in a small lecturer office in the University of Lincoln. The sensor captures a depth image every 5 seconds since April 2014 and the depth data are compressed and uploaded automatically every day. The data is recorded simply as a stream of 320x240x16b images. To convert them to ROS-compatible *image\_raw* format, you will need to use the *convert\_raw* utility, which is part of the `froctomap <https://github.com/gestom/fremen/tree/master/froctomap>`__ package.

| 
| 
| 

+--------------------------------+-------------------------------+
| |image2|                       | |image3|                      |
+--------------------------------+-------------------------------+
| Typical afternoon depth map.   | Typical midnight depth map.   |
+--------------------------------+-------------------------------+

| 
| 

--------------

Dataset structure and download
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The depth images, organised in chunks of one-day length are `here <GREG/>`__. Each zip archive contains a *xx.3D* file with the depth image taked every 5 seconds and a *xx.1D* file that contains timestamps and distance of central pixel of the depth image taken at 30Hz. The date and time, encoded in the file name, denote the moment when the data collection started. Note that since a frame is captured every 5 seconds, the first frame of *2016-02-25\_23:59:56.3D* file is actually taken at midnight Feb 26 2016. The dataset collection terminated on May 2016, when the room started to be occupied by another researcher.

To obtain ROS-compatible depth data stream, unzip the downloaded file, and use the *convert\_raw* utility, which is part of the `froctomap <http://github.com/gestom/fremen/tree/master/froctomap>`__ package. Calling *rosrun froctomap convert\_raw xxx.3D* will publish the depth images on the */camera/depth/image\_raw* topic with the timestamp from the data collection time. To modify the timestamp to the current time, simply do the changes aroung line 97 of `convert\_raw.cpp <https://github.com/gestom/fremen/blob/master/froctomap/src/convert_raw.cpp>`__.

--------------

Conditions of use
~~~~~~~~~~~~~~~~~

If you use the dataset for your research, please cite our `paper <GREG/paper.pdf>`__ that describes it. We attached a `bibtex <GREG/paper.bib>`__ record for your convenience.

--------------

This dataset is part of the larger `LCAS-STRANDS long-term dataset collection <index.html>`__.

.. |image0| image:: images/small_office/greg.png
.. |image1| image:: images/small_office/none.png
.. |image2| image:: images/small_office/greg.png
.. |image3| image:: images/small_office/none.png


Original page: https://lcas.lincoln.ac.uk/owncloud/shared/datasets/greg-office.html
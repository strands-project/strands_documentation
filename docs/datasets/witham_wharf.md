<!DOCTYPE html>

Witham Wharf RGB-D dataset
--------------------------

The Witham Wharf was collected for purposes of testing RGB-D localization in changing environments. The dataset consists of one training set and three testing sets that cover changes of eight locations in an open-plan office for one year. We provide the gathered data in form of rosbags and color images.

* * * * *

### Dataset purpose

The intended use was to create a dataset to benchmark visual and RGB-D localization in changing environments. See and hear the 2 minute video below. If you are interrested only in how the dataset was collected, simply skip the first minute of the video or click [here](https://www.youtube.com/watch?feature=player_detailpage&v=aTr9KD4XMGc#t=74).

\

  ------------------------------------------------------------------------------------------------------------------------------------------------------
  <iframe width="640" height="360" src="https://www.youtube.com/embed/aTr9KD4XMGc?feature=player_detailpage" frameborder="1" allowfullscreen></iframe>
  LCAS Witham Wharf dataset collection process (time 1:13-1:32)
  ------------------------------------------------------------------------------------------------------------------------------------------------------

* * * * *

### Dataset structure

#### Rosbags

The provided archives contain rosbags, which are zipped into separate files according to the day of the data collection. Each rosbag contains a depth/color image, camera information, robot position, tf data and laser scan captured by the robot at a location and time that is encoded in the rosbag name, which contains day, month, year, hour, minute and location id. For example, *3D\_16-11-13-15-20\_place\_3.bag* contains data gathered at location 3 on Nov 16 2013 at 15:20 o'clock.

#### Color images

Color images of the dataset are arranged into eight folders according to the location they were captured at. Images were captured on a regular basis every 10 minutes and their filename corresponds to the time they were captured at. For example *00000.bmp* was captured at midnight the first day, *00012.bmp* at 2:10 am on the first day and *00145.bmp* at 0:10am of the second day of the data collection. Please note that sometimes the robot got stuck and failed to capture an image at a given location. For our method, we needed to substitute these missing images by taking the last previously captured image.

* * * * *

### Download

  ------------------------ --------- ------------------ ---------------------------------------------- ----------------------------------------------
  Name                     Length    Dates              Images                                         Rosbags
  November 2013 training   7 days    10-16/Nov/2013     [Nov 2013 training](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_RGB/training_Nov.zip)   [Nov 2013 training](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_Raw/training_Nov.zip)
  November 2013 testing    1 day     17/Nov/2013        [Nov 2013 testing](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_RGB/testing_Nov.zip)     [Nov 2013 testing](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_Raw/testing_Nov.zip)
  February 2014 testing    1 day     02/Feb/2014        [Feb 2014 testing](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_RGB/testing_Feb.zip)     [Feb 2014 testing](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_Raw/testing_Feb.zip)
  December 2014 testing    1 day     14/Dec/2014        [Dec 2014 testing](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_RGB/testing_Dec.zip)     [Dec 2014 testing](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_Raw/testing_Dec.zip)
  Complete dataset         10 days   all of the above   [Complete dataset](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_RGB/tranimage.zip)       [Complete dataset](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_Raw/tranbags.zip)
  ------------------------ --------- ------------------ ---------------------------------------------- ----------------------------------------------

* * * * *

### Additional information

If you need to transform the point clouds to a global coordinate frame, you can use the [ww\_transforms](http://github.com/gestom/ww_transforms) package, which provides a map of the environment and additional transforms that complement the *tf* information that is contained in the rosbags. The robot also performed 360°&times90° 3D [sweeps](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_Sweeps) on an hourly basis at three different locations of the Witham Wharf.

* * * * *

### Conditions of use

If you use the dataset for your research, please cite our [paper](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_RGB/paper.pdf) that describes the data collection in detail. We attached a [bibtex](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/WW_RGB/paper.bib) record for your convenience.

* * * * *

This dataset is part of the larger [LCAS-STRANDS long-term dataset collection](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/index.html).

</p>


KTH Track Dataset
-----------------

![](./STRANDS%20public%20datasets_files/bob.jpg)

UoB Scitos G5 robot - Bob

The track data were collected autonomously by a Scitos G5 robot with an RGB-D camera on a pan-tilt and a mounted laser scanner on the base of the robot, navigating through University of Birmingham library for approximately ten hours. The data contain 6251 human tracks. Each track is regarded as a sequence of human positions sticthed together based on the chronology of the positions. This track is obtained by detecting and tracking a person passing in front of the robot. All collected tracks overlayed over UoB library map can be seen in the figure below. The chronology of each track is shown by the transition of the colour from blue to green. The data are a part of the [Strands](http://strands.acin.tuwien.ac.at/index.html) EU FP7 project.

![](./STRANDS%20public%20datasets_files/library_tracks.png)

Human tracks overlayed on the 2D map

\

### Dataset structure

Data contain 6251 human tracks. Each track is stored in a cell *C~n~* and each cell is composed of *4 x N* matrix.

First and second rows correspond to *(x, y)* coordinates in meters for each captured position.

Third and fourth rows correspond to the second and nanosecond of the epoch/unix timestamp information of each position. The timestamp has the format *ssssssssss.nnnnnnnnn* where *s* is the second and *n* is the nanosecond of the timestamp.

The unix timestamp and corresponding date of a column j in a cell Cn is calculated using the formula:

-   `  TSn(j) = Cn(3,j) + Cn(4,j)*1e-09`
-   `  timestamp = str2num(num2str(TSn(j), '%.10g')) `
-   `  date = datestr(timestamp/86400 + datenum(1970,1,1))`

### Download

This dataset is available for download as a .mat [file](https://strands.pdc.kth.se/public/TrackData/dataTrajectoryNoIDCell6251.mat) (\~8.5 MB).

* * * * *

### Condition of use

If you use the dataset for your research, please cite our [paper](https://strands.pdc.kth.se/public/TrackData/dondrup_ICRA15_WS.pdf) that describes it:

       
        Real-Time Multisensor People Tracking for Human-Robot Spatial Interaction 
        Dondrup, Christian and Bellotto, Nicola and Jovan, Ferdian and Hanheide, Marc
        Robotics and Automation (ICRA), 2015 IEEE International Conference on
        
        

We attached a [bibtex](https://strands.pdc.kth.se/public/TrackData/dondrup_ICRA15_WS.bib) record for your convenience.

For further questions regarding the dataset, you can contact Ferdian Jovan (fxj345[at]cs.bham.ac.uk).

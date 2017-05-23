This page provides the training data for both ***real*** and
***simulated*** scenes and also describes the format of the data sets.

-  Simulated data:
-  `BHAM office
   desks <https://github.com/strands-project/strands_qsr/blob/master/data/simulation/bham_office_desk_500.json>`__

-  Real-world data:
-  KTH office desks

Data format
-----------

The training data is described in JSON
(http://en.wikipedia.org/wiki/JSON), a human-readable text format to
transmit data objects consisting of *key:value* pairs.

Mandatory data structures
~~~~~~~~~~~~~~~~~~~~~~~~~

The file contains a list of scenes whereby each scene is represented by
at least the following data structures:

-  ``scene_id``, a unique identifier for the scene
-  ``objects``, list of object IDs for objects that are present in the
   scence. The IDs are used as a key to retrieve the information about
   an object from all other data structures. The ID is *not* consistent
   across different scenes.
-  ``type``, a dictionary for *ID:type* pairs denotes the type of an
   object.
-  ``position``, a dictionary for *ID:position* pairs. The position is
   given in the coordinate frame of the table, whereby the bottom-left
   corner of the table resembles the origin.
-  ``orientation``, a dictionary for *ID:orientation* pairs. The
   orientation is represented as a quaternion in the reference frame of
   the table.
-  ``bbox``, a dictionary for *ID:bbox* pairs. The bounding box (bbox)
   is given by eight points *(x,y,z)* in the reference frame of the
   table.

Optional data structures
~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the above mentioned data structures, a scene description
might contain more information. This additional information depends on
the origin of the data.

For the ***real-world*** data, a scene description also includes the
following data:

-  ``front-face``, a dictionary for *ID:front-face* pairs. The
   front-face is a subset of the bounding box, denoting the intrinsic
   front face of an object.
-  ``tableID``, a unique ID for the table. This ID is identical across
   scenes.
-  ``tableType``, a type description of the table. Examples include:
   *StudentDesk*,\ *ProfessorDesk*, and *StaffDesk*.
-  ``date``, the date and time when the data collection took place. The
   format is as follows: ``YYYY:MM:DD HH:MM``. This timestamp is
   identical for all scenes collected in a single data collection run.

For the ***simulated*** data, a scene description also includes the
following data:

-  ``tablePose``, the position and orientation of the table in the world
   frame.
-  ``cameraPose``, the position and orientation of the camera view in
   the world frame.

Example
-------

The following example includes the mandatory data structures for one
scene.

::

    [
      {
        "scene_id": "scene1", 
        "type": {
          "monitor": "Monitor", 
          "cup": "Cup", 
          "keyboard": "Keyboard", 
          "pencil": "Pencil", 
          "telephone": "Telephone", 
          "pc": "PC"
        }, 
        "orientation": {
          "monitor": [
            0.9989563872446908, 
            0.0, 
            0.0, 
            0.04567424200832827
          ], 
          "cup": [
            0.6135444651092773, 
            0.0, 
            0.0, 
            0.7896601733237981
          ], 
          "keyboard": [
            0.9960360851196927, 
            0.0, 
            0.0, 
            0.08895008229021645
          ], 
          "pencil": [
            -0.6901722579088913, 
            0.0, 
            0.0, 
            0.7236451163470551
          ], 
          "telephone": [
            0.9998801896319474, 
            0.0, 
            0.0, 
            0.015479224191834938
          ], 
          "pc": [
            0.9996278322010864, 
            0.0, 
            0.0, 
            0.02727997597060249
          ]
        }, 
        "position": {
          "monitor": [
            0.2808067798614502, 
            0.8186612129211426, 
            0.2287198305130005
          ], 
          "cup": [
            0.29055213928222656, 
            1.423274040222168, 
            0.0857805609703064
          ], 
          "keyboard": [
            0.6437058448791504, 
            0.8054618835449219, 
            0.02877497673034668
          ], 
          "pencil": [
            0.8851318359375, 
            0.7548675537109375, 
            0.0085601806640625
          ], 
          "telephone": [
            0.6974833011627197, 
            0.4091925621032715, 
            0.0903427004814148
          ], 
          "pc": [
            0.3361496925354004, 
            0.384305477142334, 
            0.24617063999176025
          ]
        }, 
        "bbox": {
          "monitor": [
            [
              0.17071890830993652, 
              0.5517492294311523, 
              0.004999995231628418
            ], 
            [
              0.17071890830993652, 
              0.5517492294311523, 
              0.45243966579437256
            ], 
            [
              0.12404227256774902, 
              1.0611200332641602, 
              0.45243966579437256
            ], 
            [
              0.12404227256774902, 
              1.0611200332641602, 
              0.004999995231628418
            ], 
            [
              0.43757128715515137, 
              0.576202392578125, 
              0.004999995231628418
            ], 
            [
              0.43757128715515137, 
              0.576202392578125, 
              0.45243966579437256
            ], 
            [
              0.39089465141296387, 
              1.0855731964111328, 
              0.45243966579437256
            ], 
            [
              0.39089465141296387, 
              1.0855731964111328, 
              0.004999995231628418
            ]
          ], 
          "cup": [
            [
              0.3886749744415283, 
              1.3467788696289062, 
              0.004999995231628418
            ], 
            [
              0.3886749744415283, 
              1.3467788696289062, 
              0.16656112670898438
            ], 
            [
              0.24104976654052734, 
              1.309129238128662, 
              0.16656112670898438
            ], 
            [
              0.24104976654052734, 
              1.309129238128662, 
              0.004999995231628418
            ], 
            [
              0.3400545120239258, 
              1.5374188423156738, 
              0.004999995231628418
            ], 
            [
              0.3400545120239258, 
              1.5374188423156738, 
              0.16656112670898438
            ], 
            [
              0.1924293041229248, 
              1.4997692108154297, 
              0.16656112670898438
            ], 
            [
              0.1924293041229248, 
              1.4997692108154297, 
              0.004999995231628418
            ]
          ], 
          "keyboard": [
            [
              0.5719075202941895, 
              0.5088963508605957, 
              0.004999995231628418
            ], 
            [
              0.5719075202941895, 
              0.5088963508605957, 
              0.05254995822906494
            ], 
            [
              0.4729793071746826, 
              1.0583620071411133, 
              0.05254995822906494
            ], 
            [
              0.4729793071746826, 
              1.0583620071411133, 
              0.004999995231628418
            ], 
            [
              0.8144323825836182, 
              0.5525617599487305, 
              0.004999995231628418
            ], 
            [
              0.8144323825836182, 
              0.5525617599487305, 
              0.05254995822906494
            ], 
            [
              0.7155041694641113, 
              1.102027416229248, 
              0.05254995822906494
            ], 
            [
              0.7155041694641113, 
              1.102027416229248, 
              0.004999995231628418
            ]
          ], 
          "pencil": [
            [
              0.8866786956787109, 
              0.8634657859802246, 
              0.004999995231628418
            ], 
            [
              0.8866786956787109, 
              0.8634657859802246, 
              0.012120306491851807
            ], 
            [
              0.8938477039337158, 
              0.863126277923584, 
              0.012120306491851807
            ], 
            [
              0.8938477039337158, 
              0.863126277923584, 
              0.004999995231628418
            ], 
            [
              0.877265453338623, 
              0.6647830009460449, 
              0.004999995231628418
            ], 
            [
              0.877265453338623, 
              0.6647830009460449, 
              0.012120306491851807
            ], 
            [
              0.8844344615936279, 
              0.6644434928894043, 
              0.012120306491851807
            ], 
            [
              0.8844344615936279, 
              0.6644434928894043, 
              0.004999995231628418
            ]
          ], 
          "telephone": [
            [
              0.630591869354248, 
              0.35100269317626953, 
              -0.012934625148773193
            ], 
            [
              0.630591869354248, 
              0.35100269317626953, 
              0.15775072574615479
            ], 
            [
              0.6271209716796875, 
              0.4630756378173828, 
              0.15775072574615479
            ], 
            [
              0.6271209716796875, 
              0.4630756378173828, 
              -0.012934625148773193
            ], 
            [
              0.7880260944366455, 
              0.3558783531188965, 
              -0.012934625148773193
            ], 
            [
              0.7880260944366455, 
              0.3558783531188965, 
              0.15775072574615479
            ], 
            [
              0.784555196762085, 
              0.46795129776000977, 
              0.15775072574615479
            ], 
            [
              0.784555196762085, 
              0.46795129776000977, 
              -0.012934625148773193
            ]
          ], 
          "pc": [
            [
              0.11110544204711914, 
              0.2659010887145996, 
              0.004999935626983643
            ], 
            [
              0.11110544204711914, 
              0.2659010887145996, 
              0.4873412847518921
            ], 
            [
              0.0995481014251709, 
              0.4774947166442871, 
              0.4873412847518921
            ], 
            [
              0.0995481014251709, 
              0.4774947166442871, 
              0.004999935626983643
            ], 
            [
              0.5727512836456299, 
              0.29111623764038086, 
              0.004999935626983643
            ], 
            [
              0.5727512836456299, 
              0.29111623764038086, 
              0.4873412847518921
            ], 
            [
              0.5611939430236816, 
              0.5027098655700684, 
              0.4873412847518921
            ], 
            [
              0.5611939430236816, 
              0.5027098655700684, 
              0.004999935626983643
            ]
          ]
        }, 
        "objects": [
          "monitor", 
          "pc", 
          "keyboard", 
          "pencil", 
          "telephone", 
          "cup"
        ]
      }
    ]



Original page: https://github.com/strands-project/strands_qsr/wiki/Data-sets
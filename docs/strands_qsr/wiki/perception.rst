Simulating perception
---------------------

To simulate the perception for each scene in a scenes file, use the
'generate\_perception.py' script inside the strands\_qsr\_evaluation
package. This will generate a **perceptions** file that contains
artificial confidence values for the class of every object inside every
scene.

Usage
~~~~~

::

    rosrun strands_qsr_evalution generate_perception.py [options]

    Options:
      -h, --help            show this help message and exit
      -o FILE, --out=FILE   write scene perceptions to FILE
      -s FILE, --scenes=FILE
                            load the scenes from FILE
      -p P_TYPE, --perception=P_TYPE
                            generate perceptions of type P_TYPE
      -t OBJ_CLASS, --object_type=OBJ_CLASS
                            conside objects of type OBJ_CLASS
      -a, --all_objects     conside all objects in scenes (replaces -t)
      -O, --overwrite       overwrite output file if already exists.

for example

::

    rosrun strands_qsr_evalution generate_perception.py -o perceptions.json -s data/simulation/bham_office_desk_500.json -p gt_60 -t Mouse -t Keyboard -t Mug -t Monitor -t Headphone -t Pencil -t Keys -t Lamp -t Laptop 

Perception models
~~~~~~~~~~~~~~~~~

The perception model to use to generate the artificial object class
confidences can be specified using the ``-p`` option. Available models:
\* ``random`` - every possible class is given equal confidence \*
``gt_N`` where ``N`` is 1..100 - ground truth from 1 to 100%, the
correct object label is given confidence N while the others are equally
distributed 100-N. \* a 'library' model

Library models are specified at the bottom of
``strands_qsr_evaluation/src/perception.py`` as global variables. These
are matrices that give p(perception\_label \| true\_label). To define a
new perception model, create a new variable at the bottome of the file
using the existing model as a guide. The Gnumeric spreadsheet in the
package can be used as a guide.

Perceptions file data format
----------------------------

JSON reprentation of a dictionary, key = scene\_id, value is another
dictionary where key is the object id in the scene and value is another
dictionary of entries 'type' -> list of possible types for the object,
'confidence' - list of confidences associated to the type.

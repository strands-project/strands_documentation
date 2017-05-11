The evaluation client calls the ROS service 'group\_classification' for
each scene in a supplied JSON scenes file(\ `see
here <https://github.com/strands-project/strands_qsr/wiki/Data-sets>`__).
The perception for each scene is read from a **perceptions** file
(`Simulated
Perception <https://github.com/strands-project/strands_qsr/wiki/perception>`__).

The output of the classification is stored to a flat text file for later
processing.

Evaluation client usage
~~~~~~~~~~~~~~~~~~~~~~~

::

    Usage: rosrun strands_qsr_evalution evaluation_client.py [options]

    Options:
      -h, --help            show this help message and exit
      -p FILE, --perception_filename=FILE
                            read perceptions from FILE
      -s FILE, --scenes=FILE
                            load the scenes from FILE
      -o FILE, --output=FILE
                            store results in FILE
      -O, --overwrite       overwrite output file if already exists.
    chris@heatwave:~/documents/strands/strands_qsr.wiki$ 

for example

::

    rosrun strands_qsr_evalution evaluation_client.py -s data/simulation/bham_office_desk_500.json -p simulated_perceptions.json -o run1_results.txt

All object classes that exist in the specified simulated perceptions
file will be considered - ie. to test on a subset of the object classes
in a given scenes file, create a simulated perception file with only the
desired object types.

Output format
~~~~~~~~~~~~~

The results file looks like this:

::

    --
    scene1
    Pencil  Monitor Cup Telephone   PC  Keyboard    
    Pencil  Laptop  Cup Mouse   PC  Keyboard    
    Pencil  Cup Cup Mouse   PC  Keyboard    
    --
    scene2
    Pencil  Monitor Monitor Telephone   Bottle  Keyboard    Pencil  
    Pencil  Monitor Monitor Telephone   Bottle  Cup Stapler 
    Pencil  Monitor Monitor Telephone   Bottle  Cup Stapler 
    --
    ...

each labelled scene is specified by 5 lines: 1. A separator '--' 1. The
scene id as read from the scenes file 1. A tab separated list of ground
truth labels 1. A tab separated list of perception labels 1. A tab
separated list of relation+perception labels

So, if perception is 100% then lines 3 & 4 will be the same.

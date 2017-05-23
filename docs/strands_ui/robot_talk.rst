Robot talk
==========

A simple interface for managing short *text phrases* a robot might use
in a conversation via text and/or text-to-speech output. The text
phrases are grouped wrt topics and have associated weights. This allows
a user to sample a random text phrase for a given topic according to the
weights. All information are stored in MongoDB. The commandline tool
``rtalk.py`` can be used for managing the contents of the MongoDB
collection. The RobotTalkProxy provides a Python API for interacting
with the collection.

Commandline interface ``rtalk.py``
----------------------------------

Please run the following command for help:

::

    $ rosrun robot_talk rtalk.py -h
    usage: rtalk.py [-h]
                    {add,remove,update,list,search,play,play_random,topics} ...

    positional arguments:
      {add,remove,update,list,search,play,play_random,topics}
                            sub-command -h|--help
        add                 add -h|--help
        remove              remove -h|--help
        update              update -h|--help
        list                list -h|--help
        search              search -h|--help
        play                play -h|--help
        play_random         play_random -h|--help
        topics              topics -h|--help

    optional arguments:
      -h, --help            show this help message and exit

RobotTalkProxy (Python API)
---------------------------

Please confer to the file ``run_example.py`` for an example for using
the API.

::

    $ rosrun robot_talk run_example.py 

    Adding entry: ID: 1 - Topic: Greeting - Text: Hi! - Weight 1.0
    Adding entry: ID: 2 - Topic: Greeting - Text: Hello! - Weight 2.0
    Adding entry: ID: 3 - Topic: Greeting - Text: Hey! - Weight 0.5

    Listing entries for topic: Greeting
    ====  ========  ======  ========
      ID  Topic     Text      Weight
    ====  ========  ======  ========
       1  Greeting  Hi!          1
       2  Greeting  Hello!       2
       3  Greeting  Hey!         0.5
    ====  ========  ======  ========
    Total number: 3

    EXAMPLE 1: Get random text for a given topic. Here 'Greeting'
    Chosen ID:  1 - Probability: 0.285714285714
    Text: Hi!

    Chosen ID:  2 - Probability: 0.571428571429
    Text: Hello!

    Chosen ID:  1 - Probability: 0.285714285714
    Text: Hi!

    Chosen ID:  3 - Probability: 0.142857142857
    Text: Hey!

    Chosen ID:  1 - Probability: 0.285714285714
    Text: Hi!

    Chosen ID:  2 - Probability: 0.571428571429
    Text: Hello!

    Chosen ID:  1 - Probability: 0.285714285714
    Text: Hi!

    Chosen ID:  1 - Probability: 0.285714285714
    Text: Hi!

    Chosen ID:  2 - Probability: 0.571428571429
    Text: Hello!

    Chosen ID:  2 - Probability: 0.571428571429
    Text: Hello!

    EXAMPLE 2: Playing random text (via marytts) for a given topic
    Chosen ID:  2 - Probability: 0.571428571429
    Now playing: Hello!

    Removing entry ID: 1
    Removal successful.
    Removing entry ID: 2
    Removal successful.
    Removing entry ID: 3
    Removal successful.



Original page: https://github.com/strands-project/strands_ui/blob/hydro-devel/robot_talk/README.md
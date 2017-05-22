strands\_tweets
===============

Utility package containing a node that can be used to manage twitter
accounts from ROS

Installation
------------

Install Twython via pip

::

        $ pip install twython

or, with easy\_install

::

        $ easy_install twython

Starting Out
------------

-  Go to ``https://dev.twitter.com/apps`` and register an application
-  If the application is registered, hit the ``Test OAuth``. Skip the
   two following steps.
-  Go to the settings tab and chage permitions to
   ``Read, Write and Access direct messages``
-  Go back to the Details tab and at the botton hit the
   ``Create Access Token Button``
-  Go to OAuth tool tab and get the Consumer key, Consumer secret,
   Access token and Access token secret and save them on
   ``/opt/strands/strands_catkin_ws/src/strands_deployment/strands_parameters/defaults/twitter_params.yaml``
   with the format as follows: \`\`\` twitter: appKey: '' appSecret: ''
   oauthToken: '' oauthTokenSecret: ''

   \`\`\`
-  Launch the mongodb\_store:
   ``roslaunch mongodb_store mongodb_store.launch``
-  Save the parameters on your locals collection:

``rosservice call /config_manager/save_param /twitter/appKey``

``rosservice call /config_manager/save_param /twitter/appSecret``

``rosservice call /config_manager/save_param /twitter/oauthToken``

``rosservice call /config_manager/save_param /twitter/oauthTokenSecret``
\* Now you are ready to go!

Tweeting
--------

Text Only
~~~~~~~~~

Run the Strands\_tweets node ``rosrun strands_tweets tweet.py``

You can send a tweet by calling the ``/strands_tweets/Tweet`` service
like this:

``rosservice call /strands_tweets/Tweet 'Whatever you want to say' false``

You can also send a tweet using the ``tweet_test`` client like this:

``rosrun strands_tweets tweet_test.py 'Whatever you want to say'``

You can tweet using actions too try running:

``rosrun actionlib axclient.py /strands_tweets``

Fill the text field with the text of your tweet and press SEND GOAL

Tweeting Images
~~~~~~~~~~~~~~~

You can tweet Images using an script especially provided for it:

``rosrun strands_tweets tweet_image_test.py 'text for the tweet less than a 140 characters' /path/to/an/image.png``

Using strands\_tweets in your code
----------------------------------

Goal definition
~~~~~~~~~~~~~~~

strands\_tweets is an action server with the following goal

::

    #goal definition
    string text
    bool force
    bool with_photo
    sensor_msgs/Image photo
    ---
    #result definition
    bool success
    ---
    #feedback
    string tweet

-  text: is a field that contains the text to be tweeted

-  force: is a boolean to tell the action server to tweet the text even
   if is longer than a 140 characters, on that texted it will send as
   many tweets as needed to send the whole string. Note: this doesn't
   work when tweeting images

-  with\_photo: is a boolean to tell the action server that the tweet
   contains an image

-  photo: is the image to be tweeted with the text when 'with\_photo' is
   set to true

Using the action server (python)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Import the necessary modules

   ::

       import actionlib
       import strands_tweets.msg

   if using images you'll need to import this too:

::

    from sensor_msgs.msg import Image

-  Create action server client

   ::

       client = actionlib.SimpleActionClient('strands_tweets', strands_tweets.msg.SendTweetAction)
       client.wait_for_server()

   strands\_tweets is the action server name

-  Create goal definition (text only)

   ::

       tweetgoal = strands_tweets.msg.SendTweetGoal()
       tweetgoal.text = text
       tweetgoal.force = false
       tweetgoal.with_photo = False

-  Create goal definition (with image)

   ::

       tweetgoal = strands_tweets.msg.SendTweetGoal()
       tweetgoal.text = text
       tweetgoal.with_photo = True
       tweetgoal.photo = image_from_ros_msg

   Note: the image HAS to be a 'sensor\_msgs.msg.Image' ROS message

-  Send goal

   ::

       client.send_goal(tweetgoal)
       # Waits for the server to finish performing the action.
       client.wait_for_result()
       # Prints out the result of executing the action
       ps = client.get_result()
       print ps

-  Where can I see an example of this?

You can check the test nodes for this code in :

https://raw.githubusercontent.com/strands-project/strands\_social/hydro-devel/strands\_tweets/scripts/tweet\_image\_test.py

and

https://raw.githubusercontent.com/strands-project/strands\_social/hydro-devel/strands\_tweets/scripts/tweet\_test.py

Using the action server (C++)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are no examples of this in C++ but you can use it following the
steps on this Readme using the action lib API for C++ should do,
following this tutorial should help
http://wiki.ros.org/actionlib\_tutorials/Tutorials/SimpleActionClient

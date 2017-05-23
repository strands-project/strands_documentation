watchdog\_node
==============

This package provides a 'watchdog' node that monitors for specified
conditions, and takes a specified action if any condition becomes true.

Usage
-----

``rosrun watchdog_node watchdog_node _config:=/path/to/config.yaml``

where ``config.yaml`` is the configuration specifying a list of
watchdogs in terms of 'monitors' and 'actions':

::

    - name: check_battery
      description: Monitors the battery level.
      restart_timeout: 30
      monitors:
          - monitor_type: TopicFieldCondition
            topic: /battery_state/lifePercent
            condition: "{value} < 97"
      actions:
          - action_type: SendEmail
            to_addresses:  [cburbridge@gmail.com]
            from_address: cburbridge@gmail.com
            message: "Warning: robot battery is critically low."
            server: mail-relay.cs.bham.ac.uk
            port: 25
    - name: check_scitos_node
      description: Checks the /odom topic, kills scitos node if not published for 20s.
      restart_timeout: 30
      monitors:
          - monitor_type: TopicAlive
            topic: /odom
            max_duration: 20
      actions:
          - action_type: KillNode
            node_name: /scitos_mira

Each watchdog must have the following fields:

-  ``name``: any name chosen by the user
-  ``description``: some hopefully useful description string
-  ``restart_timeout``: how many seconds to wait after this watchdog has
   fired before restarting the watchdog. If value is -1 then the
   watchdog will stop running after it has been fired.
-  ``monitors``: a list of monitors that make up the watchdog. If any
   one of the monitors fires then the watchdog will fire and stop,
   restarting after ``restart_timeout``.
-  ``actions``: a list of actions to take when this watchdog fires.

Monitors
--------

The following monitors are available:

::

    - type:  TopicPublished
      description:  This monitor triggers the actions if a message is published on a given topic
      configuration fields:
        -  topic  :  The topic to listen to

    - type:  TopicAlive
      description:  This monitor triggers the actions if there are no messages on the given topic for a given period
      configuration fields:
        -  topic  :  The topic to monitor
        -  max_duration  :  The maximum number of seconds to accept not receiving a message

    - type:  TopicFieldCondition
      description:  This monitor checks a field in a given topic and triggers the actions when a condition is met.
      configuration fields:
        -  topic  :  The topic & field to watch, eg /topic/field
        -  condition  :  A python expression containing {value} as a place holder for the value of the topic field. For example '{value} < 30'

Actions
-------

The following actions are available:

::

    - type:  KillNode
      description:  Sends a specified node a kill signal.
      configuration fields:
        -  node_name  :  The rosgraph name of the node to kill.

    - type:  SendEmail
      description:  Sends an email using simple unsecure SMTP.
      configuration fields:
        -  to_addresses  :  A list of email addresses to send to.
        -  from_address  :  The email address to be sent from.
        -  message  :  The message body of the email.
        -  server  :  The SMTP server.
        -  port  :  The port the SMTP server uses.

Developing new actions/monitors
-------------------------------

Monitors
~~~~~~~~

Monitors are classes that derive from the base classes
``watchdog_node.MonitorType``. They must provide ``name``,
``description`` and ``config_keys`` fields at the class level and
implement a ``start()`` and ``stop()`` method. ``start()`` will be
called when the monitor is started or restarted following the firing of
the watchdog. ``stop()`` will be called when the watchdog fires or is
shutdown.

In order to signal that the watchdog should fire, the class should call
'self.set\_invalid()\`.

TopicPublished provides a straightforward example.

Note that all modules defining monitors need to be imported in
``monitors/__init__.py``

Actions
~~~~~~~

Actions are classes that derive from the base class
``watchdog_node.ActionType``. Similar to monitors they must provide
``name``, ``description`` and ``config_keys`` fields at the class level.
They must also provide a ``execute(self)`` method that will be called
when the watchdog fires.

``KillNode`` provides a straightforward example.

Note that all modules defining actions need to be imported in
``actions/__init__.py``


Original page: https://github.com/strands-project/strands_apps/blob/indigo-devel/watchdog_node/README.md
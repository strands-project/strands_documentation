Network configuration
=====================

Bob (hostname ``bob``) has the following network interfaces: - ``eth0``
connects to the internal bob network ``[192.168.0.*]``, statically
assigned IP ``192.168.0.100`` - ``eth1`` is unused, but can be connected
to the robotics lab wired network for maintenance. Dynamic IP. -
``wlan0`` is connected to what ever wireless network is in use, usually
``ccarobot``.

The additional onboard PC (hostname ``bobl``) has a single wired network
connection ``eth0`` to the internal bob network. Network manager is
removed and setup is in ``/etc/network/interfaces``.

Internal "bob network"
----------------------

The bob network ``[192.168.0.*]`` is supplied with an outside connection
by NAT through ``bob``. ``bob`` is the main machine on this network
providing routing to other networks and DNS services. ``bobl`` is able
to access any machine accessible from ``bob`` over the ``wlan0``
interface by default. However, to access ``bobl`` from a machine that
has access to ``bob`` (``woody`` for example) you need to fist add
``bob`` as a route in the machines table:

::

    sudo route add -net 192.168.0.0/24 dev eth0 gw bob

Hostnames and IP addresses
--------------------------

To enable ROS communication between your machine and bob network hosts,
add an entry in ``/etc/hosts`` on ``bob`` and then update the internal
network dns server:

::

    sudo /etc/init.d/dnsmasq restart

Then both ``bobl`` and ``bob`` will be able to find your IP, editing
``/etc/hosts`` on ``bobl`` is not required. You might also want to add
``bob`` as an addition DNS server on your machine so that you do not
have to maintain your own hosts file.

Time
----

The time on ``bob`` and ``bobl`` are synchronised using ``chrony``.
``bob`` is the master, and can be used by offboard machines to
synchonise with:

::

    sudo ntpdate bob

ROS communication
-----------------

``bobl`` looks to ``bob`` for the ros core. On any off board machine,
set the ROS\_MASTER\_URI to bob and make sure you add your hostname as
above. In order to have full access to topics published by ``bobl`` you
must first set the route as above.

Ping of life
------------

Fixed machines sometimes loose communication with ``bob`` due to some
unknown problem with the ``ccarobot`` network routers. This has always
been fixable by pinging the lost machine from Bob, which then allows the
machine to ping/ssh/etc Bob. As a work-around and to avoid regular
manual pinging, the script ``/usr/bin/ping-hosts`` can be used to ping
all hosts in Bob's hosts file. This is also ran automatically every 2
minutes, logging to ``/var/log/ping-hosts``.

::

    strands@bob:~$ cat /var/log/ping-hosts
    ----------------------------------------------------------------------
    Wed, 14 Jan 2015 11:14:01 +0000
    localhost                    live
    bob                          live
    bobl                         live
    bobr                         down
    cca-1128                     live
    heatwave                     live
    woody                        live

Configuration files
-------------------

-  The NAT is setup on ``bob`` in the file ``/etc/robotnet.sh``, which
   is invoked by ``/etc/rc.local``. robotnet script:
   https://gist.github.com/cburbridge/3ee13fb45a4f05ea7e1e
-  The DNS services are provided using ``dnsmasq``, configured in
   ``/etc/dnsmasq.conf``:
   https://gist.github.com/cburbridge/56c1a4d94bfb48c1be46. The user of
   dns-maq by network manager needs to be removed by commenting out in
   ``/etc/NetworkManager/NetworkManager.conf``.
-  The network on ``bob`` is configured in Network Manager.
-  The network connection on ``bobl`` is configured in
   ``/etc/network/interfaces``:
   https://gist.github.com/cburbridge/2b7bc5e104ac95848501
-  The chrony configuration is in ``/etc/chrony/chrony.conf``. ``bobl``
   gets from ``bob``, ``bob`` from ``timehost.cs.bham.ac.uk`` when
   available. Bob configuration:
   https://gist.github.com/cburbridge/27502dc2ad7f74f0b48e; Bob-L
   configuration:
   https://gist.github.com/cburbridge/12eccdeb3dc2bdb63eb2
-  ``ping-hosts`` script:
   https://gist.github.com/cburbridge/b185c60efc5efbc83bc5


Setting up an Ubuntu machine to connect to the robot's VPN
==========================================================

*IPs might be different for your robot. Please ask someone from the
STRANDS team.*

Connecting via Network-Manager
------------------------------

In order to connect a random PC to the robot, it first needs to be able
to connect to the robot via TCP port 1723. The onboard PC (with local IP
``192.168.0.100`` and remote IP as assigned by the WiFi DHCP server, the
remote IP is referred to as **``WLAN_IP``** from now on) acts as a
gateway.

1. Make sure the Network-Manager PPTP plugin is installed:
   ``sudo apt-get install network-manager-pptp-gnome``
2. Create a new VPN connection in Network-Manager using PPTP protocol
3. Set **``WLAN_IP``** as the gateway address (ask a member of the
   STRANDS team to get it)
4. set username and password (ask a member of the STRANDS team to get
   it)
5. In the *"VPN"* tab, choose *"Advanced"*, and select *"Use
   Point-to-Point encryption (MPPE)"*
6. In the *"IPv4 Settings"* tab, choose *"Address Only"*
7. Click on *"Routes"* in the *"IPv4 Settings"* tab, and select *"Use
   this connection only for resources on its own network"*
8. Still in *"Routes"* add a static route with

-  Address: ``192.168.0.0``
-  Netmask: ``24``
-  Gateway: ``0.0.0.0``

1. save and connect to the new VPN network,... Tadaaa, you should be
   connected. (Note: This connection is only used to connect to the
   robot, all other network traffic on your computer still goes via the
   default route, *not* the robot!)

configure ``/etc/hosts``
------------------------

in order to have it all working nicely for ROS to find all machines, you
need to add the robot's IP addresses in ``/etc/hosts`` on your own
machine like this: The following is an example taken from Linda. Please
ask a member of the team for the correct IP range

::

    192.168.0.100 linda
    192.168.0.101 left-cortex
    192.168.0.102 right-cortex

    192.168.0.230   vpn-00
    192.168.0.231   vpn-01
    192.168.0.232   vpn-02
    192.168.0.233   vpn-03
    192.168.0.234   vpn-04
    192.168.0.235   vpn-05
    192.168.0.236   vpn-06
    192.168.0.237   vpn-07
    192.168.0.238   vpn-08
    192.168.0.239   vpn-09
    192.168.0.240   vpn-10
    192.168.0.241   vpn-11
    192.168.0.242   vpn-12
    192.168.0.243   vpn-13
    192.168.0.244   vpn-14
    192.168.0.245   vpn-15
    192.168.0.246   vpn-16
    192.168.0.247   vpn-17
    192.168.0.248   vpn-18
    192.168.0.249   vpn-19
    192.168.0.250   vpn-20
    192.168.0.251   vpn-21
    192.168.0.252   vpn-22

Enjoy
-----

You should be all set now. Just run

1. ``export ROS_MASTER_URI=http://<robot_name>:11311/`` and
2. ``export ROS_HOSTNAME=vpn-XX`` to your assign name, with ``XX``
   matching your assign IP (see above)

You should be able to e.g. run ``rosrun rviz rviz`` displaying *all*
data streams.

convenience scripts
~~~~~~~~~~~~~~~~~~~

At UOL we use a little script to set our desktop PCs to use the robot
ROS infrastructure, called
`robot-overlord.sh <https://gist.github.com/marc-hanheide/ff29427dc8ba0aa34d9c>`__.
Simply download it and run ``source robot-overlord.sh``. *This works for
Linda. Please adjust robot name appropriately if you work on one of the
other robots.*


Original page: https://github.com/strands-project/lamor15/wiki/Robot-VPN-to-connect-from-Desktop-PCs-and-Laptops
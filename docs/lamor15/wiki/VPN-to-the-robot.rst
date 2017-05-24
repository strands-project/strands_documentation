In order to connect other machines to the robot's ROS infrastructure and
to talk to all the hosts in that infrastructure, any *external*
computers need to connect to the robot using a VPN (Virtual Private
Network) to obtain an IP address in the robot subnet
(``192.168.0.x/24``). We have set up a PPTP-based VPN for this purpose,
allocating IPs in the range ``192.168.0.230-253``. (The IP prefix could
differ, e.g. it could also be ``10.0.0.x`` etc.)

Setting up an Ubuntu machine to connect to the robot's VPN
----------------------------------------------------------

connecting via Network-Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Make sure the Network-Manager PPTP plugin is installed:
   ``sudo apt-get install network-manager-pptp-gnome``
2. Create a new VPN connection in Network-Manager using PPTP protocol
3. Set **``WLAN_IP``** as the gateway address (check on the robot using
   ``ifconfig`` to find out which one that is)
4. set user (e.g. ``lamor`` and password: ``lamor2015``)
5. In the *"VPN"* tab, choose *"Advanced"*, and select *"Use
   Point-to-Point encryption (MPPE)"*
6. In the *"IPv4 Settings"* tab, choose *"Address Only"*
7. Click on *"Routes"* in the *"IPv4 Settings"* tab, and select *"Use
   this connection only for resources on its own network"*
8. Still in *"Routes"* add a static route with

-  Address: ``192.168.0.0`` (or ``10.0.0.0`` if your robot has a
   different local net)
-  Netmask: ``24``
-  Gateway: ``0.0.0.0``

1. save and connect to the new VPN network,... Tadaaa, you should be
   connected. (Note: This connection is only used to connect to the
   robot, all other network traffic on your computer still goes via the
   default route, *not* the robot!)
2. in order to use this VPN with ROS, make sure you run the
   `ros-network.sh <https://gist.github.com/marc-hanheide/1ac6d9dfd6e89d4f6126>`__
   script in each of your terminals you want to use. The argument should
   be the *local* IP of the ``ROS_MASTER``, e.g.
   ``./ros-network.sh 192.168.0.100``



Original page: https://github.com/strands-project/lamor15/wiki/VPN-to-the-robot
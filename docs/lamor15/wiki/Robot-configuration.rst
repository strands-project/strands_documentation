Overall setup
=============

(not all need to be done on all machines, some are set up already)

-  create user ``lamor`` and ``lamor-admin``
-  connect to ``doranet``
-  enable ip forward for internal PCs:
   https://gist.github.com/marc-hanheide/4773a963f5f99c6b66d0 (needs to
   be either ``wlan0`` or ``wlan1`` depending on robot)
-  put all hosts in all ``/etc/hosts``
-  generate ssh keys for lamor and lamor-admin users
   (``ssh-keygen -t rsa``), and transfer them between machines:
   ``ssh-add``, then ``ssh-copy-id``
-  enable dnsmasq with non-dhcp config:
   https://gist.github.com/marc-hanheide/4b07d3963ad2031e2696
-  enable ip-forwarding in ``/etc/sysctl.conf``
-  setup NFS for ``lamor`` user only:
   https://gist.github.com/marc-hanheide/ad621dd978c0a8b7bc43
-  create VPN setup for ``lamor`` user:
   https://github.com/strands-project/strands\_management/wiki/Robot-VPN-to-connect-from-Desktop-PCs-and-Laptops
-  put env variables in ``lamor``'s ``.bashrc``
-  install chrony and set it up (onboard:
   https://gist.github.com/cburbridge/27502dc2ad7f74f0b48e, side PC:
   https://gist.github.com/cburbridge/12eccdeb3dc2bdb63eb2)

Network setups
==============

Bob
---

Betty
-----

Linda
-----

-  robot network is ``192.168.0.0/24``
-  main PC ``linda``: ``192.168.0.100``
-  side PC ``left-cortex``: ``192.168.0.101``
-  side PC ``right-cortex``: ``192.168.0.102``

Lucie
-----

-  robot network is ``10.0.0.0/24``
-  main PC ``lucie01``: ``10.0.0.1``
-  side PC ``lucie02``: ``10.0.0.2``

Changes for LAMoR
=================

Bob
---

-  Created users on all PCs

   -  lamor -> ``uid=2000(lamor) gid=2000(lamor) groups=2000(lamor)``
   -  lamor-admin ->
      ``uid=2001(lamor-admin) gid=2001(lamor-admin) groups=2001(lamor-admin),27(sudo)``

-  Removed ``http_proxy`` from ``/etc/environment``, ``.bashrc``, and in
   the GUI
-  Generated ssh keys for lamor and lamor-admin users
   (``ssh-keygen -t rsa``), and transfered them between machines:
   ``ssh-add``, then ``ssh-copy-id``
-  Updated packages with ``sudo apt-get update`` and
   ``sudo apt-get upgrade`` on *bob*, *bobr* and *bobl*

Betty
-----

-  Created users on all PCs

   -  lamor -> ``uid=2000(lamor) gid=2000(lamor) groups=2000(lamor)``
   -  lamor-admin ->
      ``uid=2001(lamor-admin) gid=2001(lamor-admin) groups=2001(lamor-admin),27(sudo)``

-  generated ssh keys for lamor and lamor-admin users
   (``ssh-keygen -t rsa``), and transfered them between machines:
   ``ssh-add``, then ``ssh-copy-id``
-  Removed ``http_proxy`` from ``/etc/environment``, ``.bashrc``, and in
   the GUI
-  Updated packages with ``sudo apt-get update`` and
   ``sudo apt-get upgrade`` on *betty*, *bettyr* and *bettyl*

Linda
-----

-  Created users on all PCs

   -  lamor -> ``uid=2000(lamor) gid=2000(lamor) groups=2000(lamor)``
   -  lamor-admin ->
      ``uid=2001(lamor-admin) gid=2001(lamor-admin) groups=2001(lamor-admin),27(sudo)``

-  generated ssh keys for lamor and lamor-admin users
   (``ssh-keygen -t rsa``), and transfered them between machines:
   ``ssh-add``, then ``ssh-copy-id``
-  Updated packages with ``sudo apt-get update`` and
   ``sudo apt-get upgrade`` on *linda*, *left-cortex* and *right-cortex*

Lucie
-----

-  installed ``openssh-server`` on side-PC
-  installed dnsmasq
-  set up routed network
-  Created users on all PCs

   -  lamor -> ``uid=2000(lamor) gid=2000(lamor) groups=2000(lamor)``
   -  lamor-admin ->
      ``uid=2001(lamor-admin) gid=2001(lamor-admin) groups=2001(lamor-admin),27(sudo)``

-  put all hosts in all ``/etc/hosts``

   -  ``lucie01`` in lucie02
   -  ``lucie02`` in lucie01

-  installed vim ``sudo apt-get install vim`` in lucie02
-  generated ssh keys for lamor and lamor-admin users
   (``ssh-keygen -t rsa``) on ``Lucie02``, and transferred them to
   ``Lucie01``: ``ssh-add``, then ``ssh-copy-id``
-  set up NFS and VPN



Original page: https://github.com/strands-project/lamor15/wiki/Robot-configuration
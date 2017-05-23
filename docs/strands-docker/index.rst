[|image0|\ ](https://microbadger.com/images/strands/strands-base "Get
your own image badge on microbadger.com" d )

STRANDS distro docker image(s)
==============================

Do run an interactive session in the fully installed STRANDS base
system, simply make sure you have `docker installed on your
machine <https://docs.docker.com/engine/installation/>`__, and then you
can simply run

``docker run -it --rm strands/strands-base /bin/bash``

to launch an interactive session. In there, most STRANDS packages are
available, however, access to any local hardware (GPU) is not directly
possible, there is more documentation for this at
http://wiki.ros.org/docker/Tutorials/Hardware%20Acceleration

But this is enough to have a play with some STRANDS software and connect
it to other ROS components as required.

Running on a Linux host
-----------------------

If you want to run this with your local user and actually have the
docker container access your X server, run something like:

::

    docker run -it --rm \
        --user=`id -u` \
        --env="DISPLAY" \
        --workdir="/home/$USER" \
        --volume="/home/$USER:/home/$USER" \
        --volume="/etc/group:/etc/group:ro" \
        --volume="/etc/passwd:/etc/passwd:ro" \
        --volume="/etc/shadow:/etc/shadow:ro" \
        --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
        --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
        strands/strands-base /bin/bash

Running on OSX/Windows
----------------------

This is a useful guide for running X-enabled docker images on OSX:
https://blog.bennycornelissen.nl/bwc-gui-apps-in-docker-on-osx/

and here is a gist run this on a MAC:
https://gist.github.com/marc-hanheide/d9b4bb6057665acf7524c7b79827f1c8

Requirements: \* install docker on OSX:
https://docs.docker.com/docker-for-mac/ \* create a docker machine:
``docker-machine create --driver virtualbox --virtualbox-memory 2048 docker-vm``
\* ``source docker-x.sh`` from
https://gist.github.com/marc-hanheide/d9b4bb6057665acf7524c7b79827f1c8
\* run ``docker_run strands/strands-base``

Builds
======

Building locally
----------------

build locally via ``docker build --tag ros:strands --network host``

Automated builds on hub.docker.com
----------------------------------

This repository is set up to release automatically a STRANDS docker
image into the official docker repository at
https://hub.docker.com/r/strands/strands-base/

.. |image0| image:: https://images.microbadger.com/badges/image/strands/strands-base.svg


Original page: https://github.com/strands-project/strands-docker/blob/master/README.md
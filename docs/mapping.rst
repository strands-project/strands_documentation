II. Mapping and Navigation
--------------------------

a) Code
~~~~~~~~

For this step, you need:

- https://github.com/strands-project/strands_movebase.git branch:indigo-devel
  
  * A repository for all the STRANDS-augmented movebase, including 3D obstacle avoidance, etc.
  
- https://github.com/strands-project/strands_navigation.git branch:indigo_devel

  * Higher-level navigation capabilities, such as topological and monitored navigation

- https://github.com/strands-project/strands_recovery_behaviours.git branch:hydro-devel

  * This repository contains behaviours used by monitored navigation to recover the robot if trapped in unexpected situations. 
  
- https://github.com/strands-project/strands_apps.git branch:indigo_devel

  * Project specific apps and tools; for example, it contains door passing behaviour that can be performed on a topological map

- https://github.com/strands-project/strands_ui.git branch:hydro-devel

  * Some recovery behaviours require interaction with a human. This package includes user interfaces for the robots, displayed using a web browser.

- https://github.com/strands-project/strands_hri.git branch:hydro-devel

  * This package includes other human-robot-interaction packages, such as human aware navigation.
  
- https://github.com/strands-project/strands_perception_people.git branch:indigo-devel

  * In order to do HRI, we need to detect humans. 
  
- https://github.com/strands-project/strands_social.git branch:hydro-devel

  * Our robots are quite active on social medias. This feature is optional but it will not compile without this package.
  
- https://github.com/strands-project/strands_webtools.git branch:hydro-devel

  * An interface to access the real and/or simulated robot via web applications.

- https://github.com/strands-project/strands_qsr_lib.git branch:master

  * A library for Qualitative Spatial Relations and Reasoning.

- https://github.com/strands-project/fremen.git branch:master

  * Frequency Map Enhancement (FreMEn) is a method that allows to introduce dynamics into spatial models used in the mobile robotics domain




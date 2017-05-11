The strands launch files are divided in different levels one per level:

strands\_core is a level which can be used to launch every system that
has to run in the robot before actually starting the robot hardware.

strands\_robot launches the hardware of the robot is started

strands\_navigation launches the navigation system

To use the strands launch files you can create launch files for each of
this level calling the launch files and setting the needed parameters
some examples are as following

1. Launching strands\_core

::

    <launch>
        <!-- Remote Launching -->
        <arg name="machine" default="localhost" />
        <arg name="user" default="" />

        <!-- Datacentre -->
        <arg name="db_path" default="/opt/strands/ros_datacentre"/>


        <include file="$(find scitos_bringup)/launch/strands_core.launch">
            <arg name="machine"  value="$(arg machine)"/>
            <arg name="user"  value="$(arg user)"/>
            <arg name="db_path" default="$(arg db_path)"/>
        </include>
    </launch>

1. Launching strands\_robot

::

    <launch>
        <arg name="machine" default="localhost" />
        <arg name="user" default="" />

        <arg name="scitos_config" default="$(find scitos_mira)/resources/SCITOSDriver-with-udev.xml"/>

        <arg name="laser" default="/dev/laser" />

        <arg name="head_camera" default="true" />
        <arg name="head_ip" default="left-cortex" />
        <arg name="head_user" default="strands" />

        <arg name="chest_camera" default="true" />
        <arg name="chest_ip" default="right-cortex" />
        <arg name="chest_user" default="strands" />

        <arg name="with_mux" default="false"/>
        <arg name="js" default="$(optenv JOYSTICK_DEVICE /dev/js1)" />


        <!-- Robot -->
        <include file="$(find scitos_bringup)/launch/strands_robot.launch">
            <arg name="machine"  value="$(arg machine)"/>
            <arg name="user"  value="$(arg user)"/>

            <!-- SCITOS G5 Robot -->
            <arg name="scitos_config" value="$(arg scitos_config)"/>

            <!-- SICK S300 -->
            <arg name="laser"  value="$(arg laser)"/>

            <!-- Head Xtion Camera -->
            <arg name="head_camera" value="$(arg head_camera)" />
            <arg name="head_ip"     value="$(arg head_ip)" />
            <arg name="head_user"   value="$(arg head_user)" />

            <!-- Chest Xtion Camera -->
            <arg name="chest_camera" value="$(arg chest_camera)" />
            <arg name="chest_ip"     value="$(arg chest_ip)" />
            <arg name="chest_user"   value="$(arg chest_user)" />

            <!-- cmd vel mux -->
            <arg name="with_mux" value="$(arg with_mux)"/>

            <!--- Teleop Joystick -->
            <arg name="js" value="$(arg js)" />
        </include>


    </launch>

1. Launching strands\_navigation

::

    <launch>
      <arg name="machine" default="localhost" />
      <arg name="user" default=""/>

      <arg name="with_camera" default="true"/>

      <arg name="camera" default="chest_xtion"/>
      <arg name="camera_ip" default="right-cortex"/>
      <arg name="camera_user" default="strands"/>


      <arg name="map" default="/opt/strands/maps/WW_2014_06_18-cropped.yaml"/>
      <arg name="with_no_go_map" default="true"/>
      <arg name="no_go_map" default="/opt/strands/maps/WW_2014_06_18-nogo.yaml"/>
      <arg name="with_mux" default="false" />

      <arg name="topological_map" default="WW_2014_06_18"/>


      <!-- STRANDS navigation -->
      <include file="$(find scitos_bringup)/launch/strands_navigation.launch" >
        <arg name="machine" value="$(arg machine)"/>
        <arg name="user" value="$(arg user)"/>
        <!-- <arg name="remote" value="$(arg remote)"/> -->

        <!-- strands_movebase -->
        <arg name="with_camera" value="$(arg with_camera)"/>
        <arg name="camera" value="$(arg camera)"/>
        <arg name="camera_ip" value="$(arg camera_ip)"/>
        <arg name="camera_user" value="$(arg camera_user)"/>

        <arg name="map" value="$(arg map)"/>
        <arg name="with_no_go_map" value="$(arg with_no_go_map)"/>
        <arg name="no_go_map" value="$(arg no_go_map)"/>

        <arg name="with_mux" value="$(arg with_mux)"/>

        <arg name="topological_map" value="$(arg topological_map)"/>

      </include>


    </launch>


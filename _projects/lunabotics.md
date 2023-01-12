---
layout: page
title: Lunabotics Autonomy 
description: Building a full autonomy stack for a Lunar Rover for the Annual NASA Lunabotics Competition
img: assets/img/lunabotics/rover.jpg
importance: 1
category: clubs
---

> [GitHub](https://github.com/PurdueLunabotics/purdue_lunabotics), [Website](https://web.ics.purdue.edu/~lunabot/)

## Overview
The goal of the NASA Lunabotics competition is to build a rover that can autonomously navigate through obstacles and mine icy lunar regolith and deposit into a collection sieve. As the Software Lead, contributions are the following:
- Communication
- Control
- Localization and Mapping
- Navigation
- Testing and Quality Control

### Communication

- Externally, implemented communication using a router between robot and control center.

- Internally, implemented serial communication interface between onboard compute and micro-controller.

### Control 

- Implemented manual controller system logic that controls drivetrain with tank drive controls, angle of excavation tool, extension of lead screw, and deposition with analog PWM signals.

{% include yt_player.html id="QuUIjPAKYAw" %}

<div class="caption">
    Manual Control System Demo
</div>

### Localization/Mapping

- With visual-odometry data sourced from a T265 Localization camera, utilized matrix algebra to compute coordinate transformations from the camera odometry to the robot base odometry. The drift error after 2 min of continuous operation was **0.3m**.

- With 4 AprilTags fiducial markers, the collection bin is localized within **0.17m of error**.

- Using two depth cameras and a 2D lidar for perception, I combined the point clouds into a voxelized grid using **Octomap**, which was then used for generating an occupancy grid for planning. 

The following shows the result of the combination of the above implementations:

{% include figure.html path="assets/img/lunabotics/demo-mapping-obstacles.gif" title="Mapping and localization demo with obstacles" class="img-fluid rounded z-depth-1" %}
<div class="caption">
    Localization and mapping demo in the real world
</div>

### Planning

#### Global Planner - RRTStar

- Implemented the **RRT* algorithm** to plan near-optimal global paths in **under 2 sec**.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/lunabotics/sim_nav_gazebo.png" title="Gazebo environment with robot" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/lunabotics/sim_nav_rviz.png" title="Rviz environment with robot and obstacle detection" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/lunabotics/sim_nav_rrtstar.png" title="Grid representation and RRT* planning paths" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Path planning in a simulated competition arena.
</div>

### Testing and Quality Control 

- Implemented `unittest` and `rostest` frameworks in safety critical ROS packages such as navigation, reviewed PRs from the team, and integrated with the GitHub CI/CD pipeline to ensure a clean codebase.

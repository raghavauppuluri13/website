---
layout: page
title: Rope Manipulation 
description: Self-supervised rope manipulation in MuJoCo
img: assets/img/rope-manipulation/mujoco_rope_env.png
importance: 2
category: research 
---
> [Github](https://github.com/raghavauppuluri13/rope-manipulation), [Presentation](https://docs.google.com/presentation/d/1zRuhXxpXfUB-i6lupotLf98f1N1sZB_0EnAhp_hPZIs/edit?usp=sharing)

For the CS 593 Robotics course and research at [MARS Lab](https://www.purduemars.com/), I am developing a self-supervised rope manipulation robot system in MuJoCo with a Panda robot arm. This project utilizes the following components:
- Causal InfoGAN framework[^1] for planning from pixel observations
- Inverse Dynamics[^2] model mapping pixels to high-level actions
- PID/MPC-CEM for generating and executing joint-space trajectories from high-level actions

### Kinematic Planning/Control

Given start and goal poses in task-space, simple linear interpolation is used to plan discretized XYZ waypoints from start to goal. Then inverse kinematics is used to generate joint-space trajectories that are executed via PID control.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/rope-manipulation/demo_1.gif" title="Demo 1" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/rope-manipulation/demo_2.gif" title="Demo 2" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/rope-manipulation/demo_3.gif" title="Demo 3" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Random interaction rollouts with rope in MuJoCo
</div>

### Learning-based Planning from Pixels with Causal InfoGAN

**Results are still in progress**

### Inverse Dynamics from Pixels 

**Results are still in progress**

### References

[^1]: Kurutach, T., Tamar, A., Yang, G., Russell, S. J., & Abbeel, P. (2018). Learning plannable representations with causal infogan. Advances in Neural Information Processing Systems, 31.

[^2]: Nair, A., Chen, D., Agrawal, P., Isola, P., Abbeel, P., Malik, J., & Levine, S. (2017, May). Combining self-supervised learning and imitation for vision-based rope manipulation. In 2017 IEEE international conference on robotics and automation (ICRA) (pp. 2146-2153). IEEE.
  

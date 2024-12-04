#!/usr/bin/env python
# Copyright (c) 2019 TOYOTA MOTOR CORPORATION
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

#  * Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#  notice, this list of conditions and the following disclaimer in the
#  documentation and/or other materials provided with the distribution.
#  * Neither the name of Toyota Motor Corporation nor the names of its
#  contributors may be used to endorse or promote products derived from
#  this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import random
import math
import numpy as np
from scipy.spatial.distance import pdist
import argparse

import rospy
import sys
import os
import time
import string
import warnings
import re

from gazebo_ros import gazebo_interface

from gazebo_msgs.msg import *
from gazebo_msgs.srv import *
from std_srvs.srv import Empty
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Wrench
import tf.transformations as tft

from tmc_wrs_gazebo_worlds import randomizer

model_database_template = """<sdf version="1.4">
  <world name="default">
    <include>
      <uri>model://MODEL_NAME</uri>
    </include>
  </world>
</sdf>"""


def drop_object(gazebo_name, name, x, y, z, yaw):
    rospy.loginfo('Drop {0}'.format(name))
    initial_pose = Pose()
    initial_pose.position.x = x
    initial_pose.position.y = y
    initial_pose.position.z = z
    roll = 0.0
    pitch = 0.0
    # yaw = math.pi * (random.random() - 0.5)
    tmpq = tft.quaternion_from_euler(roll, pitch, yaw)
    q = Quaternion(tmpq[0], tmpq[1], tmpq[2], tmpq[3])
    initial_pose.orientation = q

    model_xml = model_database_template.replace('MODEL_NAME', name)

    gazebo_interface.spawn_sdf_model_client(gazebo_name, model_xml, rospy.get_namespace(),
                                            initial_pose, "", "/gazebo")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Drop objects to the WRS field.')
    parser.add_argument('--seed', nargs='?', type=int, default=False,
                        help='seed of random variables (default: none)')
    parser.add_argument('--percategory', nargs='?', type=int, default=6,
                        help='Number of object per category in task 1 (default: 6)')
    parser.add_argument('--obstacles', nargs='?', type=int, default=4,
                        help='Number of obstacles in task 2a (default: 4)')
    parser.add_argument('--perrow', nargs='?', type=int, default=6,
                        help='Number of objects per each rows in task 2 (default: 6)')

    args = parser.parse_args(rospy.myargv()[1:])

    if args.seed:
        random.seed(args.seed)
        np.random.seed(args.seed)

    rospy.init_node('spawn_objects')

    randomizer.generate_wrs_task(drop_object, args.seed, args.percategory, args.obstacles, args.perrow)

    rospy.loginfo('Spawn finished')
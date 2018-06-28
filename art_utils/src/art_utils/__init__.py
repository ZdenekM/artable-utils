from art_utils.art_api_helper import ArtApiHelper
from art_utils.api_definition import APIGroup, Topic, Service, Action, ArtAPI
from art_utils.object_helper import ObjectHelper

import rospy


def array_from_param(param, target_type=str, expected_length=None):

    tmp = []

    for s in rospy.get_param(param).split(","):
        tmp.append(target_type(s.strip()))

    if expected_length is not None:
        assert len(tmp) == expected_length

    return tmp

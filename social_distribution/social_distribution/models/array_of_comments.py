# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .comment import Comment  # noqa: F401,E501
from social_distribution.social_distribution import util


class ArrayOfComments(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """ArrayOfComments - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ArrayOfComments':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ArrayOfComments of this ArrayOfComments.  # noqa: E501
        :rtype: ArrayOfComments
        """
        return util.deserialize_model(dikt, cls)

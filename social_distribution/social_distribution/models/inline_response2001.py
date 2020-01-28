# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .post import Post  # noqa: F401,E501
from .util import *


class InlineResponse2001(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, query: str=None, post: Post=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger

        :param query: The query of this InlineResponse2001.  # noqa: E501
        :type query: str
        :param post: The post of this InlineResponse2001.  # noqa: E501
        :type post: Post
        """
        self.swagger_types = {
            'query': str,
            'post': Post
        }

        self.attribute_map = {
            'query': 'query',
            'post': 'post'
        }
        self._query = query
        self._post = post

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def query(self) -> str:
        """Gets the query of this InlineResponse2001.


        :return: The query of this InlineResponse2001.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query: str):
        """Sets the query of this InlineResponse2001.


        :param query: The query of this InlineResponse2001.
        :type query: str
        """

        self._query = query

    @property
    def post(self) -> Post:
        """Gets the post of this InlineResponse2001.


        :return: The post of this InlineResponse2001.
        :rtype: Post
        """
        return self._post

    @post.setter
    def post(self, post: Post):
        """Sets the post of this InlineResponse2001.


        :param post: The post of this InlineResponse2001.
        :type post: Post
        """

        self._post = post

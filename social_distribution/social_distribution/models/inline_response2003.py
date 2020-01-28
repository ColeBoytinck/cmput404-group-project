# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .util import *


class InlineResponse2003(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, query: str=None, success: bool=None, message: str=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger

        :param query: The query of this InlineResponse2003.  # noqa: E501
        :type query: str
        :param success: The success of this InlineResponse2003.  # noqa: E501
        :type success: bool
        :param message: The message of this InlineResponse2003.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'query': str,
            'success': bool,
            'message': str
        }

        self.attribute_map = {
            'query': 'query',
            'success': 'success',
            'message': 'message'
        }
        self._query = query
        self._success = success
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2003':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_3 of this InlineResponse2003.  # noqa: E501
        :rtype: InlineResponse2003
        """
        return util.deserialize_model(dikt, cls)

    @property
    def query(self) -> str:
        """Gets the query of this InlineResponse2003.


        :return: The query of this InlineResponse2003.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query: str):
        """Sets the query of this InlineResponse2003.


        :param query: The query of this InlineResponse2003.
        :type query: str
        """

        self._query = query

    @property
    def success(self) -> bool:
        """Gets the success of this InlineResponse2003.


        :return: The success of this InlineResponse2003.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success: bool):
        """Sets the success of this InlineResponse2003.


        :param success: The success of this InlineResponse2003.
        :type success: bool
        """

        self._success = success

    @property
    def message(self) -> str:
        """Gets the message of this InlineResponse2003.


        :return: The message of this InlineResponse2003.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this InlineResponse2003.


        :param message: The message of this InlineResponse2003.
        :type message: str
        """

        self._message = message

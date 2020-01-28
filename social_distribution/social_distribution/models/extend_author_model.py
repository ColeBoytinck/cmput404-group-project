# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .author import Author  # noqa: F401,E501
from .util import *


class ExtendAuthorModel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, email: str=None, bio: str=None, host: str=None, first_name: str=None, last_name: str=None, display_name: str=None, url: str=None, github: str=None, friends: List[Author]=None):  # noqa: E501
        """ExtendAuthorModel - a model defined in Swagger

        :param id: The id of this ExtendAuthorModel.  # noqa: E501
        :type id: str
        :param email: The email of this ExtendAuthorModel.  # noqa: E501
        :type email: str
        :param bio: The bio of this ExtendAuthorModel.  # noqa: E501
        :type bio: str
        :param host: The host of this ExtendAuthorModel.  # noqa: E501
        :type host: str
        :param first_name: The first_name of this ExtendAuthorModel.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this ExtendAuthorModel.  # noqa: E501
        :type last_name: str
        :param display_name: The display_name of this ExtendAuthorModel.  # noqa: E501
        :type display_name: str
        :param url: The url of this ExtendAuthorModel.  # noqa: E501
        :type url: str
        :param github: The github of this ExtendAuthorModel.  # noqa: E501
        :type github: str
        :param friends: The friends of this ExtendAuthorModel.  # noqa: E501
        :type friends: List[Author]
        """
        self.swagger_types = {
            'id': str,
            'email': str,
            'bio': str,
            'host': str,
            'first_name': str,
            'last_name': str,
            'display_name': str,
            'url': str,
            'github': str,
            'friends': List[Author]
        }

        self.attribute_map = {
            'id': 'id',
            'email': 'email',
            'bio': 'bio',
            'host': 'host',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'display_name': 'displayName',
            'url': 'url',
            'github': 'github',
            'friends': 'friends'
        }
        self._id = id
        self._email = email
        self._bio = bio
        self._host = host
        self._first_name = first_name
        self._last_name = last_name
        self._display_name = display_name
        self._url = url
        self._github = github
        self._friends = friends

    @classmethod
    def from_dict(cls, dikt) -> 'ExtendAuthorModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExtendAuthorModel of this ExtendAuthorModel.  # noqa: E501
        :rtype: ExtendAuthorModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this ExtendAuthorModel.

        ID of the author  # noqa: E501

        :return: The id of this ExtendAuthorModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ExtendAuthorModel.

        ID of the author  # noqa: E501

        :param id: The id of this ExtendAuthorModel.
        :type id: str
        """

        self._id = id

    @property
    def email(self) -> str:
        """Gets the email of this ExtendAuthorModel.

        Email  # noqa: E501

        :return: The email of this ExtendAuthorModel.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this ExtendAuthorModel.

        Email  # noqa: E501

        :param email: The email of this ExtendAuthorModel.
        :type email: str
        """

        self._email = email

    @property
    def bio(self) -> str:
        """Gets the bio of this ExtendAuthorModel.

        Author bio  # noqa: E501

        :return: The bio of this ExtendAuthorModel.
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio: str):
        """Sets the bio of this ExtendAuthorModel.

        Author bio  # noqa: E501

        :param bio: The bio of this ExtendAuthorModel.
        :type bio: str
        """

        self._bio = bio

    @property
    def host(self) -> str:
        """Gets the host of this ExtendAuthorModel.

        Home host of the author  # noqa: E501

        :return: The host of this ExtendAuthorModel.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this ExtendAuthorModel.

        Home host of the author  # noqa: E501

        :param host: The host of this ExtendAuthorModel.
        :type host: str
        """

        self._host = host

    @property
    def first_name(self) -> str:
        """Gets the first_name of this ExtendAuthorModel.

        First name  # noqa: E501

        :return: The first_name of this ExtendAuthorModel.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this ExtendAuthorModel.

        First name  # noqa: E501

        :param first_name: The first_name of this ExtendAuthorModel.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this ExtendAuthorModel.

        Last name  # noqa: E501

        :return: The last_name of this ExtendAuthorModel.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this ExtendAuthorModel.

        Last name  # noqa: E501

        :param last_name: The last_name of this ExtendAuthorModel.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def display_name(self) -> str:
        """Gets the display_name of this ExtendAuthorModel.

        The display name of the author  # noqa: E501

        :return: The display_name of this ExtendAuthorModel.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """Sets the display_name of this ExtendAuthorModel.

        The display name of the author  # noqa: E501

        :param display_name: The display_name of this ExtendAuthorModel.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def url(self) -> str:
        """Gets the url of this ExtendAuthorModel.

        Url to the author's profile  # noqa: E501

        :return: The url of this ExtendAuthorModel.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this ExtendAuthorModel.

        Url to the author's profile  # noqa: E501

        :param url: The url of this ExtendAuthorModel.
        :type url: str
        """

        self._url = url

    @property
    def github(self) -> str:
        """Gets the github of this ExtendAuthorModel.

        HATEOS url for Github API  # noqa: E501

        :return: The github of this ExtendAuthorModel.
        :rtype: str
        """
        return self._github

    @github.setter
    def github(self, github: str):
        """Sets the github of this ExtendAuthorModel.

        HATEOS url for Github API  # noqa: E501

        :param github: The github of this ExtendAuthorModel.
        :type github: str
        """

        self._github = github

    @property
    def friends(self) -> List[Author]:
        """Gets the friends of this ExtendAuthorModel.


        :return: The friends of this ExtendAuthorModel.
        :rtype: List[Author]
        """
        return self._friends

    @friends.setter
    def friends(self, friends: List[Author]):
        """Sets the friends of this ExtendAuthorModel.


        :param friends: The friends of this ExtendAuthorModel.
        :type friends: List[Author]
        """

        self._friends = friends

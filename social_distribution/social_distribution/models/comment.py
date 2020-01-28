# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .author import Author  # noqa: F401,E501
from social_distribution.social_distribution import util


class Comment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, content_type: str=None, comment: str=None, published: str=None, author: Author=None):  # noqa: E501
        """Comment - a model defined in Swagger

        :param id: The id of this Comment.  # noqa: E501
        :type id: str
        :param content_type: The content_type of this Comment.  # noqa: E501
        :type content_type: str
        :param comment: The comment of this Comment.  # noqa: E501
        :type comment: str
        :param published: The published of this Comment.  # noqa: E501
        :type published: str
        :param author: The author of this Comment.  # noqa: E501
        :type author: Author
        """
        self.swagger_types = {
            'id': str,
            'content_type': str,
            'comment': str,
            'published': str,
            'author': Author
        }

        self.attribute_map = {
            'id': 'id',
            'content_type': 'contentType',
            'comment': 'comment',
            'published': 'published',
            'author': 'author'
        }
        self._id = id
        self._content_type = content_type
        self._comment = comment
        self._published = published
        self._author = author

    @classmethod
    def from_dict(cls, dikt) -> 'Comment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Comment of this Comment.  # noqa: E501
        :rtype: Comment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Comment.

        Comment ID  # noqa: E501

        :return: The id of this Comment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Comment.

        Comment ID  # noqa: E501

        :param id: The id of this Comment.
        :type id: str
        """

        self._id = id

    @property
    def content_type(self) -> str:
        """Gets the content_type of this Comment.

        The content type of the comment  # noqa: E501

        :return: The content_type of this Comment.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: str):
        """Sets the content_type of this Comment.

        The content type of the comment  # noqa: E501

        :param content_type: The content_type of this Comment.
        :type content_type: str
        """
        allowed_values = ["text/plain", "text/markdown"]  # noqa: E501
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def comment(self) -> str:
        """Gets the comment of this Comment.

        The content of the comment  # noqa: E501

        :return: The comment of this Comment.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this Comment.

        The content of the comment  # noqa: E501

        :param comment: The comment of this Comment.
        :type comment: str
        """

        self._comment = comment

    @property
    def published(self) -> str:
        """Gets the published of this Comment.

        ISO 8601 TIMESTAMP  # noqa: E501

        :return: The published of this Comment.
        :rtype: str
        """
        return self._published

    @published.setter
    def published(self, published: str):
        """Sets the published of this Comment.

        ISO 8601 TIMESTAMP  # noqa: E501

        :param published: The published of this Comment.
        :type published: str
        """

        self._published = published

    @property
    def author(self) -> Author:
        """Gets the author of this Comment.


        :return: The author of this Comment.
        :rtype: Author
        """
        return self._author

    @author.setter
    def author(self, author: Author):
        """Sets the author of this Comment.


        :param author: The author of this Comment.
        :type author: Author
        """

        self._author = author

# coding: utf-8

"""
    OPIF Manager API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Entity(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'folder': 'Folder',
        'sub_folders': 'list[Folder]',
        'files': 'list[File]'
    }

    attribute_map = {
        'folder': 'folder',
        'sub_folders': 'subFolders',
        'files': 'files'
    }

    def __init__(self, folder=None, sub_folders=None, files=None):  # noqa: E501
        """Entity - a model defined in Swagger"""  # noqa: E501
        self._folder = None
        self._sub_folders = None
        self._files = None
        self.discriminator = None
        if folder is not None:
            self.folder = folder
        if sub_folders is not None:
            self.sub_folders = sub_folders
        if files is not None:
            self.files = files

    @property
    def folder(self):
        """Gets the folder of this Entity.  # noqa: E501


        :return: The folder of this Entity.  # noqa: E501
        :rtype: Folder
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this Entity.


        :param folder: The folder of this Entity.  # noqa: E501
        :type: Folder
        """

        self._folder = folder

    @property
    def sub_folders(self):
        """Gets the sub_folders of this Entity.  # noqa: E501


        :return: The sub_folders of this Entity.  # noqa: E501
        :rtype: list[Folder]
        """
        return self._sub_folders

    @sub_folders.setter
    def sub_folders(self, sub_folders):
        """Sets the sub_folders of this Entity.


        :param sub_folders: The sub_folders of this Entity.  # noqa: E501
        :type: list[Folder]
        """

        self._sub_folders = sub_folders

    @property
    def files(self):
        """Gets the files of this Entity.  # noqa: E501


        :return: The files of this Entity.  # noqa: E501
        :rtype: list[File]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Entity.


        :param files: The files of this Entity.  # noqa: E501
        :type: list[File]
        """

        self._files = files

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Entity, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Entity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

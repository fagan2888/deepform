# coding: utf-8

"""
    OPIF Service Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class FolderUpdate(object):
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
        'entity_folder_id': 'str',
        'entity_id': 'str',
        'folder_name': 'str',
        'created_ts': 'datetime',
        'last_update_ts': 'datetime',
        'parent_folder_id': 'str',
        'folder_path': 'str'
    }

    attribute_map = {
        'entity_folder_id': 'entity_folder_id',
        'entity_id': 'entity_id',
        'folder_name': 'folder_name',
        'created_ts': 'created_ts',
        'last_update_ts': 'last_update_ts',
        'parent_folder_id': 'parent_folder_id',
        'folder_path': 'folder_path'
    }

    def __init__(self, entity_folder_id=None, entity_id=None, folder_name=None, created_ts=None, last_update_ts=None, parent_folder_id=None, folder_path=None):  # noqa: E501
        """FolderUpdate - a model defined in Swagger"""  # noqa: E501
        self._entity_folder_id = None
        self._entity_id = None
        self._folder_name = None
        self._created_ts = None
        self._last_update_ts = None
        self._parent_folder_id = None
        self._folder_path = None
        self.discriminator = None
        if entity_folder_id is not None:
            self.entity_folder_id = entity_folder_id
        if entity_id is not None:
            self.entity_id = entity_id
        if folder_name is not None:
            self.folder_name = folder_name
        if created_ts is not None:
            self.created_ts = created_ts
        if last_update_ts is not None:
            self.last_update_ts = last_update_ts
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if folder_path is not None:
            self.folder_path = folder_path

    @property
    def entity_folder_id(self):
        """Gets the entity_folder_id of this FolderUpdate.  # noqa: E501


        :return: The entity_folder_id of this FolderUpdate.  # noqa: E501
        :rtype: str
        """
        return self._entity_folder_id

    @entity_folder_id.setter
    def entity_folder_id(self, entity_folder_id):
        """Sets the entity_folder_id of this FolderUpdate.


        :param entity_folder_id: The entity_folder_id of this FolderUpdate.  # noqa: E501
        :type: str
        """

        self._entity_folder_id = entity_folder_id

    @property
    def entity_id(self):
        """Gets the entity_id of this FolderUpdate.  # noqa: E501


        :return: The entity_id of this FolderUpdate.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this FolderUpdate.


        :param entity_id: The entity_id of this FolderUpdate.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def folder_name(self):
        """Gets the folder_name of this FolderUpdate.  # noqa: E501


        :return: The folder_name of this FolderUpdate.  # noqa: E501
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this FolderUpdate.


        :param folder_name: The folder_name of this FolderUpdate.  # noqa: E501
        :type: str
        """

        self._folder_name = folder_name

    @property
    def created_ts(self):
        """Gets the created_ts of this FolderUpdate.  # noqa: E501


        :return: The created_ts of this FolderUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._created_ts

    @created_ts.setter
    def created_ts(self, created_ts):
        """Sets the created_ts of this FolderUpdate.


        :param created_ts: The created_ts of this FolderUpdate.  # noqa: E501
        :type: datetime
        """

        self._created_ts = created_ts

    @property
    def last_update_ts(self):
        """Gets the last_update_ts of this FolderUpdate.  # noqa: E501


        :return: The last_update_ts of this FolderUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_ts

    @last_update_ts.setter
    def last_update_ts(self, last_update_ts):
        """Sets the last_update_ts of this FolderUpdate.


        :param last_update_ts: The last_update_ts of this FolderUpdate.  # noqa: E501
        :type: datetime
        """

        self._last_update_ts = last_update_ts

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this FolderUpdate.  # noqa: E501


        :return: The parent_folder_id of this FolderUpdate.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this FolderUpdate.


        :param parent_folder_id: The parent_folder_id of this FolderUpdate.  # noqa: E501
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def folder_path(self):
        """Gets the folder_path of this FolderUpdate.  # noqa: E501


        :return: The folder_path of this FolderUpdate.  # noqa: E501
        :rtype: str
        """
        return self._folder_path

    @folder_path.setter
    def folder_path(self, folder_path):
        """Sets the folder_path of this FolderUpdate.


        :param folder_path: The folder_path of this FolderUpdate.  # noqa: E501
        :type: str
        """

        self._folder_path = folder_path

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
        if issubclass(FolderUpdate, dict):
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
        if not isinstance(other, FolderUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

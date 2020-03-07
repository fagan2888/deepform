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


class Folder(object):
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
        'folder_path': 'str',
        'allow_rename_ind': 'str',
        'allow_subfolder_ind': 'str',
        'allow_upload_ind': 'str',
        'allow_delete_ind': 'str',
        'more_public_files_ind': 'str',
        'parent_folder_id': 'str',
        'file_count': 'str',
        'created_ts': 'datetime',
        'last_update_ts': 'datetime'
    }

    attribute_map = {
        'entity_folder_id': 'entity_folder_id',
        'entity_id': 'entity_id',
        'folder_name': 'folder_name',
        'folder_path': 'folder_path',
        'allow_rename_ind': 'allow_rename_ind',
        'allow_subfolder_ind': 'allow_subfolder_ind',
        'allow_upload_ind': 'allow_upload_ind',
        'allow_delete_ind': 'allow_delete_ind',
        'more_public_files_ind': 'more_public_files_ind',
        'parent_folder_id': 'parent_folder_id',
        'file_count': 'file_count',
        'created_ts': 'created_ts',
        'last_update_ts': 'last_update_ts'
    }

    def __init__(self, entity_folder_id=None, entity_id=None, folder_name=None, folder_path=None, allow_rename_ind=None, allow_subfolder_ind=None, allow_upload_ind=None, allow_delete_ind=None, more_public_files_ind=None, parent_folder_id=None, file_count=None, created_ts=None, last_update_ts=None):  # noqa: E501
        """Folder - a model defined in Swagger"""  # noqa: E501
        self._entity_folder_id = None
        self._entity_id = None
        self._folder_name = None
        self._folder_path = None
        self._allow_rename_ind = None
        self._allow_subfolder_ind = None
        self._allow_upload_ind = None
        self._allow_delete_ind = None
        self._more_public_files_ind = None
        self._parent_folder_id = None
        self._file_count = None
        self._created_ts = None
        self._last_update_ts = None
        self.discriminator = None
        if entity_folder_id is not None:
            self.entity_folder_id = entity_folder_id
        if entity_id is not None:
            self.entity_id = entity_id
        if folder_name is not None:
            self.folder_name = folder_name
        if folder_path is not None:
            self.folder_path = folder_path
        if allow_rename_ind is not None:
            self.allow_rename_ind = allow_rename_ind
        if allow_subfolder_ind is not None:
            self.allow_subfolder_ind = allow_subfolder_ind
        if allow_upload_ind is not None:
            self.allow_upload_ind = allow_upload_ind
        if allow_delete_ind is not None:
            self.allow_delete_ind = allow_delete_ind
        if more_public_files_ind is not None:
            self.more_public_files_ind = more_public_files_ind
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if file_count is not None:
            self.file_count = file_count
        if created_ts is not None:
            self.created_ts = created_ts
        if last_update_ts is not None:
            self.last_update_ts = last_update_ts

    @property
    def entity_folder_id(self):
        """Gets the entity_folder_id of this Folder.  # noqa: E501


        :return: The entity_folder_id of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._entity_folder_id

    @entity_folder_id.setter
    def entity_folder_id(self, entity_folder_id):
        """Sets the entity_folder_id of this Folder.


        :param entity_folder_id: The entity_folder_id of this Folder.  # noqa: E501
        :type: str
        """

        self._entity_folder_id = entity_folder_id

    @property
    def entity_id(self):
        """Gets the entity_id of this Folder.  # noqa: E501


        :return: The entity_id of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this Folder.


        :param entity_id: The entity_id of this Folder.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def folder_name(self):
        """Gets the folder_name of this Folder.  # noqa: E501


        :return: The folder_name of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this Folder.


        :param folder_name: The folder_name of this Folder.  # noqa: E501
        :type: str
        """

        self._folder_name = folder_name

    @property
    def folder_path(self):
        """Gets the folder_path of this Folder.  # noqa: E501


        :return: The folder_path of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._folder_path

    @folder_path.setter
    def folder_path(self, folder_path):
        """Sets the folder_path of this Folder.


        :param folder_path: The folder_path of this Folder.  # noqa: E501
        :type: str
        """

        self._folder_path = folder_path

    @property
    def allow_rename_ind(self):
        """Gets the allow_rename_ind of this Folder.  # noqa: E501


        :return: The allow_rename_ind of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._allow_rename_ind

    @allow_rename_ind.setter
    def allow_rename_ind(self, allow_rename_ind):
        """Sets the allow_rename_ind of this Folder.


        :param allow_rename_ind: The allow_rename_ind of this Folder.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if allow_rename_ind not in allowed_values:
            raise ValueError(
                "Invalid value for `allow_rename_ind` ({0}), must be one of {1}"  # noqa: E501
                .format(allow_rename_ind, allowed_values)
            )

        self._allow_rename_ind = allow_rename_ind

    @property
    def allow_subfolder_ind(self):
        """Gets the allow_subfolder_ind of this Folder.  # noqa: E501


        :return: The allow_subfolder_ind of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._allow_subfolder_ind

    @allow_subfolder_ind.setter
    def allow_subfolder_ind(self, allow_subfolder_ind):
        """Sets the allow_subfolder_ind of this Folder.


        :param allow_subfolder_ind: The allow_subfolder_ind of this Folder.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if allow_subfolder_ind not in allowed_values:
            raise ValueError(
                "Invalid value for `allow_subfolder_ind` ({0}), must be one of {1}"  # noqa: E501
                .format(allow_subfolder_ind, allowed_values)
            )

        self._allow_subfolder_ind = allow_subfolder_ind

    @property
    def allow_upload_ind(self):
        """Gets the allow_upload_ind of this Folder.  # noqa: E501


        :return: The allow_upload_ind of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._allow_upload_ind

    @allow_upload_ind.setter
    def allow_upload_ind(self, allow_upload_ind):
        """Sets the allow_upload_ind of this Folder.


        :param allow_upload_ind: The allow_upload_ind of this Folder.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if allow_upload_ind not in allowed_values:
            raise ValueError(
                "Invalid value for `allow_upload_ind` ({0}), must be one of {1}"  # noqa: E501
                .format(allow_upload_ind, allowed_values)
            )

        self._allow_upload_ind = allow_upload_ind

    @property
    def allow_delete_ind(self):
        """Gets the allow_delete_ind of this Folder.  # noqa: E501


        :return: The allow_delete_ind of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._allow_delete_ind

    @allow_delete_ind.setter
    def allow_delete_ind(self, allow_delete_ind):
        """Sets the allow_delete_ind of this Folder.


        :param allow_delete_ind: The allow_delete_ind of this Folder.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if allow_delete_ind not in allowed_values:
            raise ValueError(
                "Invalid value for `allow_delete_ind` ({0}), must be one of {1}"  # noqa: E501
                .format(allow_delete_ind, allowed_values)
            )

        self._allow_delete_ind = allow_delete_ind

    @property
    def more_public_files_ind(self):
        """Gets the more_public_files_ind of this Folder.  # noqa: E501


        :return: The more_public_files_ind of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._more_public_files_ind

    @more_public_files_ind.setter
    def more_public_files_ind(self, more_public_files_ind):
        """Sets the more_public_files_ind of this Folder.


        :param more_public_files_ind: The more_public_files_ind of this Folder.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if more_public_files_ind not in allowed_values:
            raise ValueError(
                "Invalid value for `more_public_files_ind` ({0}), must be one of {1}"  # noqa: E501
                .format(more_public_files_ind, allowed_values)
            )

        self._more_public_files_ind = more_public_files_ind

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this Folder.  # noqa: E501


        :return: The parent_folder_id of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this Folder.


        :param parent_folder_id: The parent_folder_id of this Folder.  # noqa: E501
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def file_count(self):
        """Gets the file_count of this Folder.  # noqa: E501


        :return: The file_count of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._file_count

    @file_count.setter
    def file_count(self, file_count):
        """Sets the file_count of this Folder.


        :param file_count: The file_count of this Folder.  # noqa: E501
        :type: str
        """

        self._file_count = file_count

    @property
    def created_ts(self):
        """Gets the created_ts of this Folder.  # noqa: E501


        :return: The created_ts of this Folder.  # noqa: E501
        :rtype: datetime
        """
        return self._created_ts

    @created_ts.setter
    def created_ts(self, created_ts):
        """Sets the created_ts of this Folder.


        :param created_ts: The created_ts of this Folder.  # noqa: E501
        :type: datetime
        """

        self._created_ts = created_ts

    @property
    def last_update_ts(self):
        """Gets the last_update_ts of this Folder.  # noqa: E501


        :return: The last_update_ts of this Folder.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_ts

    @last_update_ts.setter
    def last_update_ts(self, last_update_ts):
        """Sets the last_update_ts of this Folder.


        :param last_update_ts: The last_update_ts of this Folder.  # noqa: E501
        :type: datetime
        """

        self._last_update_ts = last_update_ts

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
        if issubclass(Folder, dict):
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
        if not isinstance(other, Folder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
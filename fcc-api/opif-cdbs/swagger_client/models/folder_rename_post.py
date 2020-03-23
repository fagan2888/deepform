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


class FolderRenamePost(object):
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
        'folder_id': 'str',
        'folder_name': 'str',
        'entity_id': 'str',
        'service_code': 'str'
    }

    attribute_map = {
        'folder_id': 'folderId',
        'folder_name': 'folderName',
        'entity_id': 'entityId',
        'service_code': 'serviceCode'
    }

    def __init__(self, folder_id=None, folder_name=None, entity_id=None, service_code=None):  # noqa: E501
        """FolderRenamePost - a model defined in Swagger"""  # noqa: E501
        self._folder_id = None
        self._folder_name = None
        self._entity_id = None
        self._service_code = None
        self.discriminator = None
        if folder_id is not None:
            self.folder_id = folder_id
        if folder_name is not None:
            self.folder_name = folder_name
        if entity_id is not None:
            self.entity_id = entity_id
        if service_code is not None:
            self.service_code = service_code

    @property
    def folder_id(self):
        """Gets the folder_id of this FolderRenamePost.  # noqa: E501

        Unique Id of the folder.  # noqa: E501

        :return: The folder_id of this FolderRenamePost.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this FolderRenamePost.

        Unique Id of the folder.  # noqa: E501

        :param folder_id: The folder_id of this FolderRenamePost.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def folder_name(self):
        """Gets the folder_name of this FolderRenamePost.  # noqa: E501

        Name of the new folder  # noqa: E501

        :return: The folder_name of this FolderRenamePost.  # noqa: E501
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this FolderRenamePost.

        Name of the new folder  # noqa: E501

        :param folder_name: The folder_name of this FolderRenamePost.  # noqa: E501
        :type: str
        """

        self._folder_name = folder_name

    @property
    def entity_id(self):
        """Gets the entity_id of this FolderRenamePost.  # noqa: E501

        Unique Entity Id.  # noqa: E501

        :return: The entity_id of this FolderRenamePost.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this FolderRenamePost.

        Unique Entity Id.  # noqa: E501

        :param entity_id: The entity_id of this FolderRenamePost.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def service_code(self):
        """Gets the service_code of this FolderRenamePost.  # noqa: E501

        Entity Service Code  # noqa: E501

        :return: The service_code of this FolderRenamePost.  # noqa: E501
        :rtype: str
        """
        return self._service_code

    @service_code.setter
    def service_code(self, service_code):
        """Sets the service_code of this FolderRenamePost.

        Entity Service Code  # noqa: E501

        :param service_code: The service_code of this FolderRenamePost.  # noqa: E501
        :type: str
        """

        self._service_code = service_code

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
        if issubclass(FolderRenamePost, dict):
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
        if not isinstance(other, FolderRenamePost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

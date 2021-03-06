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


class CableServiceEmpUnitsUpdatePost(object):
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
        'psid': 'str',
        'emp_units': 'list[str]',
        'access_token': 'str'
    }

    attribute_map = {
        'psid': 'psid',
        'emp_units': 'empUnits',
        'access_token': 'accessToken'
    }

    def __init__(self, psid=None, emp_units=None, access_token=None):  # noqa: E501
        """CableServiceEmpUnitsUpdatePost - a model defined in Swagger"""  # noqa: E501
        self._psid = None
        self._emp_units = None
        self._access_token = None
        self.discriminator = None
        if psid is not None:
            self.psid = psid
        if emp_units is not None:
            self.emp_units = emp_units
        if access_token is not None:
            self.access_token = access_token

    @property
    def psid(self):
        """Gets the psid of this CableServiceEmpUnitsUpdatePost.  # noqa: E501

        cable psid  # noqa: E501

        :return: The psid of this CableServiceEmpUnitsUpdatePost.  # noqa: E501
        :rtype: str
        """
        return self._psid

    @psid.setter
    def psid(self, psid):
        """Sets the psid of this CableServiceEmpUnitsUpdatePost.

        cable psid  # noqa: E501

        :param psid: The psid of this CableServiceEmpUnitsUpdatePost.  # noqa: E501
        :type: str
        """

        self._psid = psid

    @property
    def emp_units(self):
        """Gets the emp_units of this CableServiceEmpUnitsUpdatePost.  # noqa: E501

        array of empunit ids  # noqa: E501

        :return: The emp_units of this CableServiceEmpUnitsUpdatePost.  # noqa: E501
        :rtype: list[str]
        """
        return self._emp_units

    @emp_units.setter
    def emp_units(self, emp_units):
        """Sets the emp_units of this CableServiceEmpUnitsUpdatePost.

        array of empunit ids  # noqa: E501

        :param emp_units: The emp_units of this CableServiceEmpUnitsUpdatePost.  # noqa: E501
        :type: list[str]
        """

        self._emp_units = emp_units

    @property
    def access_token(self):
        """Gets the access_token of this CableServiceEmpUnitsUpdatePost.  # noqa: E501

        Access token of the entity/facility  # noqa: E501

        :return: The access_token of this CableServiceEmpUnitsUpdatePost.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this CableServiceEmpUnitsUpdatePost.

        Access token of the entity/facility  # noqa: E501

        :param access_token: The access_token of this CableServiceEmpUnitsUpdatePost.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

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
        if issubclass(CableServiceEmpUnitsUpdatePost, dict):
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
        if not isinstance(other, CableServiceEmpUnitsUpdatePost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

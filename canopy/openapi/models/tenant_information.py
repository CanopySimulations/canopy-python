# coding: utf-8

"""
    Canopy.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from canopy.openapi.configuration import Configuration


class TenantInformation(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'tenant_id': 'str',
        'name': 'str',
        'short_name': 'str',
        'users': 'list[UserInformation]'
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        'name': 'name',
        'short_name': 'shortName',
        'users': 'users'
    }

    def __init__(self, tenant_id=None, name=None, short_name=None, users=None, local_vars_configuration=None):  # noqa: E501
        """TenantInformation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tenant_id = None
        self._name = None
        self._short_name = None
        self._users = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if users is not None:
            self.users = users

    @property
    def tenant_id(self):
        """Gets the tenant_id of this TenantInformation.  # noqa: E501


        :return: The tenant_id of this TenantInformation.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this TenantInformation.


        :param tenant_id: The tenant_id of this TenantInformation.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this TenantInformation.  # noqa: E501


        :return: The name of this TenantInformation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenantInformation.


        :param name: The name of this TenantInformation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this TenantInformation.  # noqa: E501


        :return: The short_name of this TenantInformation.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this TenantInformation.


        :param short_name: The short_name of this TenantInformation.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def users(self):
        """Gets the users of this TenantInformation.  # noqa: E501


        :return: The users of this TenantInformation.  # noqa: E501
        :rtype: list[UserInformation]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this TenantInformation.


        :param users: The users of this TenantInformation.  # noqa: E501
        :type: list[UserInformation]
        """

        self._users = users

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TenantInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TenantInformation):
            return True

        return self.to_dict() != other.to_dict()
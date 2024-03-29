# coding: utf-8

"""
    Canopy.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from canopy.openapi.configuration import Configuration


class GetAccountSettingsResult(object):
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
        'username': 'object',
        'email': 'object',
        'is_enabled': 'bool',
        'is_email_confirmed': 'bool'
    }

    attribute_map = {
        'username': 'username',
        'email': 'email',
        'is_enabled': 'isEnabled',
        'is_email_confirmed': 'isEmailConfirmed'
    }

    def __init__(self, username=None, email=None, is_enabled=None, is_email_confirmed=None, local_vars_configuration=None):  # noqa: E501
        """GetAccountSettingsResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._username = None
        self._email = None
        self._is_enabled = None
        self._is_email_confirmed = None
        self.discriminator = None

        self.username = username
        self.email = email
        self.is_enabled = is_enabled
        self.is_email_confirmed = is_email_confirmed

    @property
    def username(self):
        """Gets the username of this GetAccountSettingsResult.  # noqa: E501


        :return: The username of this GetAccountSettingsResult.  # noqa: E501
        :rtype: object
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GetAccountSettingsResult.


        :param username: The username of this GetAccountSettingsResult.  # noqa: E501
        :type username: object
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def email(self):
        """Gets the email of this GetAccountSettingsResult.  # noqa: E501


        :return: The email of this GetAccountSettingsResult.  # noqa: E501
        :rtype: object
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetAccountSettingsResult.


        :param email: The email of this GetAccountSettingsResult.  # noqa: E501
        :type email: object
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def is_enabled(self):
        """Gets the is_enabled of this GetAccountSettingsResult.  # noqa: E501


        :return: The is_enabled of this GetAccountSettingsResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this GetAccountSettingsResult.


        :param is_enabled: The is_enabled of this GetAccountSettingsResult.  # noqa: E501
        :type is_enabled: bool
        """
        if self.local_vars_configuration.client_side_validation and is_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")  # noqa: E501

        self._is_enabled = is_enabled

    @property
    def is_email_confirmed(self):
        """Gets the is_email_confirmed of this GetAccountSettingsResult.  # noqa: E501


        :return: The is_email_confirmed of this GetAccountSettingsResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_email_confirmed

    @is_email_confirmed.setter
    def is_email_confirmed(self, is_email_confirmed):
        """Sets the is_email_confirmed of this GetAccountSettingsResult.


        :param is_email_confirmed: The is_email_confirmed of this GetAccountSettingsResult.  # noqa: E501
        :type is_email_confirmed: bool
        """
        if self.local_vars_configuration.client_side_validation and is_email_confirmed is None:  # noqa: E501
            raise ValueError("Invalid value for `is_email_confirmed`, must not be `None`")  # noqa: E501

        self._is_email_confirmed = is_email_confirmed

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetAccountSettingsResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetAccountSettingsResult):
            return True

        return self.to_dict() != other.to_dict()

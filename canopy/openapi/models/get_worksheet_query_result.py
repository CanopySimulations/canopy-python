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


class GetWorksheetQueryResult(object):
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
        'worksheet': 'GetWorksheetQueryResultWorksheet',
        'user_information': 'GetAllSupportSessionsQueryResultUserInformation'
    }

    attribute_map = {
        'worksheet': 'worksheet',
        'user_information': 'userInformation'
    }

    def __init__(self, worksheet=None, user_information=None, local_vars_configuration=None):  # noqa: E501
        """GetWorksheetQueryResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._worksheet = None
        self._user_information = None
        self.discriminator = None

        self.worksheet = worksheet
        self.user_information = user_information

    @property
    def worksheet(self):
        """Gets the worksheet of this GetWorksheetQueryResult.  # noqa: E501


        :return: The worksheet of this GetWorksheetQueryResult.  # noqa: E501
        :rtype: GetWorksheetQueryResultWorksheet
        """
        return self._worksheet

    @worksheet.setter
    def worksheet(self, worksheet):
        """Sets the worksheet of this GetWorksheetQueryResult.


        :param worksheet: The worksheet of this GetWorksheetQueryResult.  # noqa: E501
        :type worksheet: GetWorksheetQueryResultWorksheet
        """
        if self.local_vars_configuration.client_side_validation and worksheet is None:  # noqa: E501
            raise ValueError("Invalid value for `worksheet`, must not be `None`")  # noqa: E501

        self._worksheet = worksheet

    @property
    def user_information(self):
        """Gets the user_information of this GetWorksheetQueryResult.  # noqa: E501


        :return: The user_information of this GetWorksheetQueryResult.  # noqa: E501
        :rtype: GetAllSupportSessionsQueryResultUserInformation
        """
        return self._user_information

    @user_information.setter
    def user_information(self, user_information):
        """Sets the user_information of this GetWorksheetQueryResult.


        :param user_information: The user_information of this GetWorksheetQueryResult.  # noqa: E501
        :type user_information: GetAllSupportSessionsQueryResultUserInformation
        """
        if self.local_vars_configuration.client_side_validation and user_information is None:  # noqa: E501
            raise ValueError("Invalid value for `user_information`, must not be `None`")  # noqa: E501

        self._user_information = user_information

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
        if not isinstance(other, GetWorksheetQueryResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetWorksheetQueryResult):
            return True

        return self.to_dict() != other.to_dict()

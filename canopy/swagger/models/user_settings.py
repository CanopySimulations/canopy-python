# coding: utf-8

"""
    Canopy.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserSettings(object):
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
        'channels': 'list[ChannelSettings]',
        'charts': 'list[ChartSettings]',
        'label_definitions': 'LabelDefinitions'
    }

    attribute_map = {
        'channels': 'channels',
        'charts': 'charts',
        'label_definitions': 'labelDefinitions'
    }

    def __init__(self, channels=None, charts=None, label_definitions=None):  # noqa: E501
        """UserSettings - a model defined in Swagger"""  # noqa: E501

        self._channels = None
        self._charts = None
        self._label_definitions = None
        self.discriminator = None

        if channels is not None:
            self.channels = channels
        if charts is not None:
            self.charts = charts
        if label_definitions is not None:
            self.label_definitions = label_definitions

    @property
    def channels(self):
        """Gets the channels of this UserSettings.  # noqa: E501


        :return: The channels of this UserSettings.  # noqa: E501
        :rtype: list[ChannelSettings]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this UserSettings.


        :param channels: The channels of this UserSettings.  # noqa: E501
        :type: list[ChannelSettings]
        """

        self._channels = channels

    @property
    def charts(self):
        """Gets the charts of this UserSettings.  # noqa: E501


        :return: The charts of this UserSettings.  # noqa: E501
        :rtype: list[ChartSettings]
        """
        return self._charts

    @charts.setter
    def charts(self, charts):
        """Sets the charts of this UserSettings.


        :param charts: The charts of this UserSettings.  # noqa: E501
        :type: list[ChartSettings]
        """

        self._charts = charts

    @property
    def label_definitions(self):
        """Gets the label_definitions of this UserSettings.  # noqa: E501


        :return: The label_definitions of this UserSettings.  # noqa: E501
        :rtype: LabelDefinitions
        """
        return self._label_definitions

    @label_definitions.setter
    def label_definitions(self, label_definitions):
        """Sets the label_definitions of this UserSettings.


        :param label_definitions: The label_definitions of this UserSettings.  # noqa: E501
        :type: LabelDefinitions
        """

        self._label_definitions = label_definitions

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
        if issubclass(UserSettings, dict):
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
        if not isinstance(other, UserSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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


class ResolvedStatisticLabel(object):
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
        'minimum': 'float',
        'maximum': 'float',
        'mean': 'float'
    }

    attribute_map = {
        'minimum': 'minimum',
        'maximum': 'maximum',
        'mean': 'mean'
    }

    def __init__(self, minimum=None, maximum=None, mean=None, local_vars_configuration=None):  # noqa: E501
        """ResolvedStatisticLabel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._minimum = None
        self._maximum = None
        self._mean = None
        self.discriminator = None

        if minimum is not None:
            self.minimum = minimum
        if maximum is not None:
            self.maximum = maximum
        if mean is not None:
            self.mean = mean

    @property
    def minimum(self):
        """Gets the minimum of this ResolvedStatisticLabel.  # noqa: E501


        :return: The minimum of this ResolvedStatisticLabel.  # noqa: E501
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this ResolvedStatisticLabel.


        :param minimum: The minimum of this ResolvedStatisticLabel.  # noqa: E501
        :type: float
        """

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this ResolvedStatisticLabel.  # noqa: E501


        :return: The maximum of this ResolvedStatisticLabel.  # noqa: E501
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this ResolvedStatisticLabel.


        :param maximum: The maximum of this ResolvedStatisticLabel.  # noqa: E501
        :type: float
        """

        self._maximum = maximum

    @property
    def mean(self):
        """Gets the mean of this ResolvedStatisticLabel.  # noqa: E501


        :return: The mean of this ResolvedStatisticLabel.  # noqa: E501
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this ResolvedStatisticLabel.


        :param mean: The mean of this ResolvedStatisticLabel.  # noqa: E501
        :type: float
        """

        self._mean = mean

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
        if not isinstance(other, ResolvedStatisticLabel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResolvedStatisticLabel):
            return True

        return self.to_dict() != other.to_dict()
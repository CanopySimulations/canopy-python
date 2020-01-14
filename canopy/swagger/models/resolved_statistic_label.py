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


class ResolvedStatisticLabel(object):
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
        'minimum': 'float',
        'maximum': 'float',
        'mean': 'float'
    }

    attribute_map = {
        'minimum': 'minimum',
        'maximum': 'maximum',
        'mean': 'mean'
    }

    def __init__(self, minimum=None, maximum=None, mean=None):  # noqa: E501
        """ResolvedStatisticLabel - a model defined in Swagger"""  # noqa: E501

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
        if issubclass(ResolvedStatisticLabel, dict):
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
        if not isinstance(other, ResolvedStatisticLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
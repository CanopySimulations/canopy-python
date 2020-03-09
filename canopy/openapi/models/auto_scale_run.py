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


class AutoScaleRun(object):
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
        'error': 'AutoScaleRunError',
        'results': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'error': 'error',
        'results': 'results',
        'timestamp': 'timestamp'
    }

    def __init__(self, error=None, results=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """AutoScaleRun - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._results = None
        self._timestamp = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if results is not None:
            self.results = results
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def error(self):
        """Gets the error of this AutoScaleRun.  # noqa: E501


        :return: The error of this AutoScaleRun.  # noqa: E501
        :rtype: AutoScaleRunError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AutoScaleRun.


        :param error: The error of this AutoScaleRun.  # noqa: E501
        :type: AutoScaleRunError
        """

        self._error = error

    @property
    def results(self):
        """Gets the results of this AutoScaleRun.  # noqa: E501


        :return: The results of this AutoScaleRun.  # noqa: E501
        :rtype: str
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this AutoScaleRun.


        :param results: The results of this AutoScaleRun.  # noqa: E501
        :type: str
        """

        self._results = results

    @property
    def timestamp(self):
        """Gets the timestamp of this AutoScaleRun.  # noqa: E501


        :return: The timestamp of this AutoScaleRun.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AutoScaleRun.


        :param timestamp: The timestamp of this AutoScaleRun.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

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
        if not isinstance(other, AutoScaleRun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoScaleRun):
            return True

        return self.to_dict() != other.to_dict()
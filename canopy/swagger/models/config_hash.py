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


class ConfigHash(object):
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
        'hash': 'str',
        'hash_sim_versions': 'list[SimVersion]'
    }

    attribute_map = {
        'hash': 'hash',
        'hash_sim_versions': 'hashSimVersions'
    }

    def __init__(self, hash=None, hash_sim_versions=None):  # noqa: E501
        """ConfigHash - a model defined in Swagger"""  # noqa: E501

        self._hash = None
        self._hash_sim_versions = None
        self.discriminator = None

        if hash is not None:
            self.hash = hash
        if hash_sim_versions is not None:
            self.hash_sim_versions = hash_sim_versions

    @property
    def hash(self):
        """Gets the hash of this ConfigHash.  # noqa: E501


        :return: The hash of this ConfigHash.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ConfigHash.


        :param hash: The hash of this ConfigHash.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def hash_sim_versions(self):
        """Gets the hash_sim_versions of this ConfigHash.  # noqa: E501


        :return: The hash_sim_versions of this ConfigHash.  # noqa: E501
        :rtype: list[SimVersion]
        """
        return self._hash_sim_versions

    @hash_sim_versions.setter
    def hash_sim_versions(self, hash_sim_versions):
        """Sets the hash_sim_versions of this ConfigHash.


        :param hash_sim_versions: The hash_sim_versions of this ConfigHash.  # noqa: E501
        :type: list[SimVersion]
        """

        self._hash_sim_versions = hash_sim_versions

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
        if issubclass(ConfigHash, dict):
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
        if not isinstance(other, ConfigHash):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
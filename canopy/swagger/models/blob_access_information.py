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


class BlobAccessInformation(object):
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
        'url': 'str',
        'access_signature': 'str'
    }

    attribute_map = {
        'url': 'url',
        'access_signature': 'accessSignature'
    }

    def __init__(self, url=None, access_signature=None):  # noqa: E501
        """BlobAccessInformation - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._access_signature = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if access_signature is not None:
            self.access_signature = access_signature

    @property
    def url(self):
        """Gets the url of this BlobAccessInformation.  # noqa: E501


        :return: The url of this BlobAccessInformation.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BlobAccessInformation.


        :param url: The url of this BlobAccessInformation.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def access_signature(self):
        """Gets the access_signature of this BlobAccessInformation.  # noqa: E501


        :return: The access_signature of this BlobAccessInformation.  # noqa: E501
        :rtype: str
        """
        return self._access_signature

    @access_signature.setter
    def access_signature(self, access_signature):
        """Sets the access_signature of this BlobAccessInformation.


        :param access_signature: The access_signature of this BlobAccessInformation.  # noqa: E501
        :type: str
        """

        self._access_signature = access_signature

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
        if issubclass(BlobAccessInformation, dict):
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
        if not isinstance(other, BlobAccessInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
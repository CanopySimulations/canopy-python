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


class DocumentCustomPropertyGroup(object):
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
        'name': 'str',
        'groups': 'list[DocumentGroupResult]'
    }

    attribute_map = {
        'name': 'name',
        'groups': 'groups'
    }

    def __init__(self, name=None, groups=None):  # noqa: E501
        """DocumentCustomPropertyGroup - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._groups = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if groups is not None:
            self.groups = groups

    @property
    def name(self):
        """Gets the name of this DocumentCustomPropertyGroup.  # noqa: E501


        :return: The name of this DocumentCustomPropertyGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentCustomPropertyGroup.


        :param name: The name of this DocumentCustomPropertyGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def groups(self):
        """Gets the groups of this DocumentCustomPropertyGroup.  # noqa: E501


        :return: The groups of this DocumentCustomPropertyGroup.  # noqa: E501
        :rtype: list[DocumentGroupResult]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this DocumentCustomPropertyGroup.


        :param groups: The groups of this DocumentCustomPropertyGroup.  # noqa: E501
        :type: list[DocumentGroupResult]
        """

        self._groups = groups

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
        if issubclass(DocumentCustomPropertyGroup, dict):
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
        if not isinstance(other, DocumentCustomPropertyGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
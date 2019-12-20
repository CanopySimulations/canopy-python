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


class NewWorksheetData(object):
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
        'properties': 'list[DocumentCustomPropertyData]',
        'outline': 'WorksheetOutline',
        'notes': 'str'
    }

    attribute_map = {
        'name': 'name',
        'properties': 'properties',
        'outline': 'outline',
        'notes': 'notes'
    }

    def __init__(self, name=None, properties=None, outline=None, notes=None):  # noqa: E501
        """NewWorksheetData - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._properties = None
        self._outline = None
        self._notes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties
        if outline is not None:
            self.outline = outline
        if notes is not None:
            self.notes = notes

    @property
    def name(self):
        """Gets the name of this NewWorksheetData.  # noqa: E501


        :return: The name of this NewWorksheetData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewWorksheetData.


        :param name: The name of this NewWorksheetData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this NewWorksheetData.  # noqa: E501


        :return: The properties of this NewWorksheetData.  # noqa: E501
        :rtype: list[DocumentCustomPropertyData]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this NewWorksheetData.


        :param properties: The properties of this NewWorksheetData.  # noqa: E501
        :type: list[DocumentCustomPropertyData]
        """

        self._properties = properties

    @property
    def outline(self):
        """Gets the outline of this NewWorksheetData.  # noqa: E501


        :return: The outline of this NewWorksheetData.  # noqa: E501
        :rtype: WorksheetOutline
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this NewWorksheetData.


        :param outline: The outline of this NewWorksheetData.  # noqa: E501
        :type: WorksheetOutline
        """

        self._outline = outline

    @property
    def notes(self):
        """Gets the notes of this NewWorksheetData.  # noqa: E501


        :return: The notes of this NewWorksheetData.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this NewWorksheetData.


        :param notes: The notes of this NewWorksheetData.  # noqa: E501
        :type: str
        """

        self._notes = notes

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
        if issubclass(NewWorksheetData, dict):
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
        if not isinstance(other, NewWorksheetData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class NewConfigData(object):
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
        'config_type': 'DocumentSubType',
        'properties': 'list[DocumentCustomPropertyData]',
        'config': 'object',
        'notes': 'str',
        'sim_version': 'str',
        'parent_worksheet_id': 'DocumentId'
    }

    attribute_map = {
        'name': 'name',
        'config_type': 'configType',
        'properties': 'properties',
        'config': 'config',
        'notes': 'notes',
        'sim_version': 'simVersion',
        'parent_worksheet_id': 'parentWorksheetId'
    }

    def __init__(self, name=None, config_type=None, properties=None, config=None, notes=None, sim_version=None, parent_worksheet_id=None):  # noqa: E501
        """NewConfigData - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._config_type = None
        self._properties = None
        self._config = None
        self._notes = None
        self._sim_version = None
        self._parent_worksheet_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if config_type is not None:
            self.config_type = config_type
        if properties is not None:
            self.properties = properties
        if config is not None:
            self.config = config
        if notes is not None:
            self.notes = notes
        if sim_version is not None:
            self.sim_version = sim_version
        if parent_worksheet_id is not None:
            self.parent_worksheet_id = parent_worksheet_id

    @property
    def name(self):
        """Gets the name of this NewConfigData.  # noqa: E501


        :return: The name of this NewConfigData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewConfigData.


        :param name: The name of this NewConfigData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def config_type(self):
        """Gets the config_type of this NewConfigData.  # noqa: E501


        :return: The config_type of this NewConfigData.  # noqa: E501
        :rtype: DocumentSubType
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this NewConfigData.


        :param config_type: The config_type of this NewConfigData.  # noqa: E501
        :type: DocumentSubType
        """

        self._config_type = config_type

    @property
    def properties(self):
        """Gets the properties of this NewConfigData.  # noqa: E501


        :return: The properties of this NewConfigData.  # noqa: E501
        :rtype: list[DocumentCustomPropertyData]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this NewConfigData.


        :param properties: The properties of this NewConfigData.  # noqa: E501
        :type: list[DocumentCustomPropertyData]
        """

        self._properties = properties

    @property
    def config(self):
        """Gets the config of this NewConfigData.  # noqa: E501


        :return: The config of this NewConfigData.  # noqa: E501
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this NewConfigData.


        :param config: The config of this NewConfigData.  # noqa: E501
        :type: object
        """

        self._config = config

    @property
    def notes(self):
        """Gets the notes of this NewConfigData.  # noqa: E501


        :return: The notes of this NewConfigData.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this NewConfigData.


        :param notes: The notes of this NewConfigData.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def sim_version(self):
        """Gets the sim_version of this NewConfigData.  # noqa: E501


        :return: The sim_version of this NewConfigData.  # noqa: E501
        :rtype: str
        """
        return self._sim_version

    @sim_version.setter
    def sim_version(self, sim_version):
        """Sets the sim_version of this NewConfigData.


        :param sim_version: The sim_version of this NewConfigData.  # noqa: E501
        :type: str
        """

        self._sim_version = sim_version

    @property
    def parent_worksheet_id(self):
        """Gets the parent_worksheet_id of this NewConfigData.  # noqa: E501


        :return: The parent_worksheet_id of this NewConfigData.  # noqa: E501
        :rtype: DocumentId
        """
        return self._parent_worksheet_id

    @parent_worksheet_id.setter
    def parent_worksheet_id(self, parent_worksheet_id):
        """Sets the parent_worksheet_id of this NewConfigData.


        :param parent_worksheet_id: The parent_worksheet_id of this NewConfigData.  # noqa: E501
        :type: DocumentId
        """

        self._parent_worksheet_id = parent_worksheet_id

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
        if issubclass(NewConfigData, dict):
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
        if not isinstance(other, NewConfigData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
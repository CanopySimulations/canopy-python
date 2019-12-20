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


class GetStudyTypesQueryResult(object):
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
        'study_types': 'list[StudyTypeDefinition]',
        'sim_types': 'list[SimTypeDefinition]',
        'config_types': 'list[ConfigTypeDefinition]'
    }

    attribute_map = {
        'study_types': 'studyTypes',
        'sim_types': 'simTypes',
        'config_types': 'configTypes'
    }

    def __init__(self, study_types=None, sim_types=None, config_types=None):  # noqa: E501
        """GetStudyTypesQueryResult - a model defined in Swagger"""  # noqa: E501

        self._study_types = None
        self._sim_types = None
        self._config_types = None
        self.discriminator = None

        if study_types is not None:
            self.study_types = study_types
        if sim_types is not None:
            self.sim_types = sim_types
        if config_types is not None:
            self.config_types = config_types

    @property
    def study_types(self):
        """Gets the study_types of this GetStudyTypesQueryResult.  # noqa: E501


        :return: The study_types of this GetStudyTypesQueryResult.  # noqa: E501
        :rtype: list[StudyTypeDefinition]
        """
        return self._study_types

    @study_types.setter
    def study_types(self, study_types):
        """Sets the study_types of this GetStudyTypesQueryResult.


        :param study_types: The study_types of this GetStudyTypesQueryResult.  # noqa: E501
        :type: list[StudyTypeDefinition]
        """

        self._study_types = study_types

    @property
    def sim_types(self):
        """Gets the sim_types of this GetStudyTypesQueryResult.  # noqa: E501


        :return: The sim_types of this GetStudyTypesQueryResult.  # noqa: E501
        :rtype: list[SimTypeDefinition]
        """
        return self._sim_types

    @sim_types.setter
    def sim_types(self, sim_types):
        """Sets the sim_types of this GetStudyTypesQueryResult.


        :param sim_types: The sim_types of this GetStudyTypesQueryResult.  # noqa: E501
        :type: list[SimTypeDefinition]
        """

        self._sim_types = sim_types

    @property
    def config_types(self):
        """Gets the config_types of this GetStudyTypesQueryResult.  # noqa: E501


        :return: The config_types of this GetStudyTypesQueryResult.  # noqa: E501
        :rtype: list[ConfigTypeDefinition]
        """
        return self._config_types

    @config_types.setter
    def config_types(self, config_types):
        """Sets the config_types of this GetStudyTypesQueryResult.


        :param config_types: The config_types of this GetStudyTypesQueryResult.  # noqa: E501
        :type: list[ConfigTypeDefinition]
        """

        self._config_types = config_types

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
        if issubclass(GetStudyTypesQueryResult, dict):
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
        if not isinstance(other, GetStudyTypesQueryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

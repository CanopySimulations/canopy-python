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


class GetTenantDefaultCustomPropertyNamesQueryResult(object):
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
        'settings': 'TenantDefaultCustomPropertyNames',
        'custom_property_groups': 'list[DocumentTypeCustomPropertyGroups]',
        'study_types': 'list[str]',
        'config_types': 'list[str]'
    }

    attribute_map = {
        'settings': 'settings',
        'custom_property_groups': 'customPropertyGroups',
        'study_types': 'studyTypes',
        'config_types': 'configTypes'
    }

    def __init__(self, settings=None, custom_property_groups=None, study_types=None, config_types=None, local_vars_configuration=None):  # noqa: E501
        """GetTenantDefaultCustomPropertyNamesQueryResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._settings = None
        self._custom_property_groups = None
        self._study_types = None
        self._config_types = None
        self.discriminator = None

        if settings is not None:
            self.settings = settings
        if custom_property_groups is not None:
            self.custom_property_groups = custom_property_groups
        if study_types is not None:
            self.study_types = study_types
        if config_types is not None:
            self.config_types = config_types

    @property
    def settings(self):
        """Gets the settings of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501


        :return: The settings of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501
        :rtype: TenantDefaultCustomPropertyNames
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this GetTenantDefaultCustomPropertyNamesQueryResult.


        :param settings: The settings of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501
        :type: TenantDefaultCustomPropertyNames
        """

        self._settings = settings

    @property
    def custom_property_groups(self):
        """Gets the custom_property_groups of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501


        :return: The custom_property_groups of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501
        :rtype: list[DocumentTypeCustomPropertyGroups]
        """
        return self._custom_property_groups

    @custom_property_groups.setter
    def custom_property_groups(self, custom_property_groups):
        """Sets the custom_property_groups of this GetTenantDefaultCustomPropertyNamesQueryResult.


        :param custom_property_groups: The custom_property_groups of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501
        :type: list[DocumentTypeCustomPropertyGroups]
        """

        self._custom_property_groups = custom_property_groups

    @property
    def study_types(self):
        """Gets the study_types of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501


        :return: The study_types of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._study_types

    @study_types.setter
    def study_types(self, study_types):
        """Sets the study_types of this GetTenantDefaultCustomPropertyNamesQueryResult.


        :param study_types: The study_types of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["straightSim", "apexSim", "quasiStaticLap", "generateRacingLine", "quasiStaticLapWithGenerateRacingLine", "deploymentLap", "failureSim", "successSim", "virtual4Post", "limitSim", "driveCycleSim", "dynamicLap", "dynamicLapWithSLS", "dynamicLapHD", "dynamicMultiLap", "tyreThermalDynamicLap", "tyreThermalDynamicMultiLap", "overtakingLap", "allLapSims", "dragSim", "thermalReplay", "tyreReplay", "pacejkaCanopyConverter", "aircraftSim", "channelInference", "telemetry", "iliadCollocation", "subLimitSim", "bankedLimitSim", "postProcessUserMaths", "unknown"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(study_types).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `study_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(study_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._study_types = study_types

    @property
    def config_types(self):
        """Gets the config_types of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501


        :return: The config_types of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._config_types

    @config_types.setter
    def config_types(self, config_types):
        """Sets the config_types of this GetTenantDefaultCustomPropertyNamesQueryResult.


        :param config_types: The config_types of this GetTenantDefaultCustomPropertyNamesQueryResult.  # noqa: E501
        :type: list[str]
        """

        self._config_types = config_types

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
        if not isinstance(other, GetTenantDefaultCustomPropertyNamesQueryResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetTenantDefaultCustomPropertyNamesQueryResult):
            return True

        return self.to_dict() != other.to_dict()

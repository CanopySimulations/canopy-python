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


class SimulationColumnLabelDefinitions(object):
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
        'sim_type': 'str',
        'labels': 'list[LabelDefinition]'
    }

    attribute_map = {
        'sim_type': 'simType',
        'labels': 'labels'
    }

    def __init__(self, sim_type=None, labels=None, local_vars_configuration=None):  # noqa: E501
        """SimulationColumnLabelDefinitions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sim_type = None
        self._labels = None
        self.discriminator = None

        if sim_type is not None:
            self.sim_type = sim_type
        if labels is not None:
            self.labels = labels

    @property
    def sim_type(self):
        """Gets the sim_type of this SimulationColumnLabelDefinitions.  # noqa: E501


        :return: The sim_type of this SimulationColumnLabelDefinitions.  # noqa: E501
        :rtype: str
        """
        return self._sim_type

    @sim_type.setter
    def sim_type(self, sim_type):
        """Sets the sim_type of this SimulationColumnLabelDefinitions.


        :param sim_type: The sim_type of this SimulationColumnLabelDefinitions.  # noqa: E501
        :type: str
        """
        allowed_values = ["StraightSim", "ApexSim", "QuasiStaticLap", "GenerateRacingLine", "DeploymentLap", "FailureSim", "SuccessSim", "Virtual4Post", "LimitSim", "DriveCycleSim", "DynamicLap", "DragSim", "DynamicMultiLap", "ThermalReplay", "TyreReplay", "PacejkaCanopyConverter", "AircraftSim", "ChannelInference", "Telemetry", "OvertakingLap", "TyreThermalDynamicLap", "TyreThermalDynamicMultiLap", "DynamicLapWithSLS", "DynamicLapHD", "IliadCollocation", "SubLimitSim", "ConstraintSatisfier"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sim_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sim_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sim_type, allowed_values)
            )

        self._sim_type = sim_type

    @property
    def labels(self):
        """Gets the labels of this SimulationColumnLabelDefinitions.  # noqa: E501


        :return: The labels of this SimulationColumnLabelDefinitions.  # noqa: E501
        :rtype: list[LabelDefinition]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this SimulationColumnLabelDefinitions.


        :param labels: The labels of this SimulationColumnLabelDefinitions.  # noqa: E501
        :type: list[LabelDefinition]
        """

        self._labels = labels

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
        if not isinstance(other, SimulationColumnLabelDefinitions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationColumnLabelDefinitions):
            return True

        return self.to_dict() != other.to_dict()
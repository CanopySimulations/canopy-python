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


class StudyTypeDefinition(object):
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
        'study_type': 'str',
        'name': 'str',
        'sim_types': 'list[str]',
        'inputs': 'list[SimulationInput]',
        'pool_type': 'str',
        'build_pool_type': 'str',
        'state': 'str',
        'valid_for_transient': 'bool',
        'valid_for_inline': 'bool',
        'previous_definitions': 'list[IPreviousDefinitionStudyTypeDefinition]',
        'implicit_sim_types': 'list[str]'
    }

    attribute_map = {
        'study_type': 'studyType',
        'name': 'name',
        'sim_types': 'simTypes',
        'inputs': 'inputs',
        'pool_type': 'poolType',
        'build_pool_type': 'buildPoolType',
        'state': 'state',
        'valid_for_transient': 'validForTransient',
        'valid_for_inline': 'validForInline',
        'previous_definitions': 'previousDefinitions',
        'implicit_sim_types': 'implicitSimTypes'
    }

    def __init__(self, study_type=None, name=None, sim_types=None, inputs=None, pool_type=None, build_pool_type=None, state=None, valid_for_transient=None, valid_for_inline=None, previous_definitions=None, implicit_sim_types=None, local_vars_configuration=None):  # noqa: E501
        """StudyTypeDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._study_type = None
        self._name = None
        self._sim_types = None
        self._inputs = None
        self._pool_type = None
        self._build_pool_type = None
        self._state = None
        self._valid_for_transient = None
        self._valid_for_inline = None
        self._previous_definitions = None
        self._implicit_sim_types = None
        self.discriminator = None

        if study_type is not None:
            self.study_type = study_type
        if name is not None:
            self.name = name
        if sim_types is not None:
            self.sim_types = sim_types
        if inputs is not None:
            self.inputs = inputs
        if pool_type is not None:
            self.pool_type = pool_type
        if build_pool_type is not None:
            self.build_pool_type = build_pool_type
        if state is not None:
            self.state = state
        if valid_for_transient is not None:
            self.valid_for_transient = valid_for_transient
        if valid_for_inline is not None:
            self.valid_for_inline = valid_for_inline
        if previous_definitions is not None:
            self.previous_definitions = previous_definitions
        if implicit_sim_types is not None:
            self.implicit_sim_types = implicit_sim_types

    @property
    def study_type(self):
        """Gets the study_type of this StudyTypeDefinition.  # noqa: E501


        :return: The study_type of this StudyTypeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._study_type

    @study_type.setter
    def study_type(self, study_type):
        """Sets the study_type of this StudyTypeDefinition.


        :param study_type: The study_type of this StudyTypeDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["straightSim", "apexSim", "quasiStaticLap", "generateRacingLine", "quasiStaticLapWithGenerateRacingLine", "deploymentLap", "failureSim", "successSim", "virtual4Post", "limitSim", "driveCycleSim", "dynamicLap", "dynamicLapWithSLS", "dynamicLapHD", "dynamicMultiLap", "tyreThermalDynamicLap", "tyreThermalDynamicMultiLap", "overtakingLap", "allLapSims", "dragSim", "thermalReplay", "tyreReplay", "pacejkaCanopyConverter", "aircraftSim", "channelInference", "telemetry", "iliadCollocation", "subLimitSim", "unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and study_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `study_type` ({0}), must be one of {1}"  # noqa: E501
                .format(study_type, allowed_values)
            )

        self._study_type = study_type

    @property
    def name(self):
        """Gets the name of this StudyTypeDefinition.  # noqa: E501


        :return: The name of this StudyTypeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StudyTypeDefinition.


        :param name: The name of this StudyTypeDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sim_types(self):
        """Gets the sim_types of this StudyTypeDefinition.  # noqa: E501


        :return: The sim_types of this StudyTypeDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._sim_types

    @sim_types.setter
    def sim_types(self, sim_types):
        """Sets the sim_types of this StudyTypeDefinition.


        :param sim_types: The sim_types of this StudyTypeDefinition.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["StraightSim", "ApexSim", "QuasiStaticLap", "GenerateRacingLine", "DeploymentLap", "FailureSim", "SuccessSim", "Virtual4Post", "LimitSim", "DriveCycleSim", "DynamicLap", "DragSim", "DynamicMultiLap", "ThermalReplay", "TyreReplay", "PacejkaCanopyConverter", "AircraftSim", "ChannelInference", "Telemetry", "OvertakingLap", "TyreThermalDynamicLap", "TyreThermalDynamicMultiLap", "DynamicLapWithSLS", "DynamicLapHD", "IliadCollocation", "SubLimitSim", "ConstraintSatisfier"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(sim_types).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `sim_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(sim_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._sim_types = sim_types

    @property
    def inputs(self):
        """Gets the inputs of this StudyTypeDefinition.  # noqa: E501


        :return: The inputs of this StudyTypeDefinition.  # noqa: E501
        :rtype: list[SimulationInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this StudyTypeDefinition.


        :param inputs: The inputs of this StudyTypeDefinition.  # noqa: E501
        :type: list[SimulationInput]
        """

        self._inputs = inputs

    @property
    def pool_type(self):
        """Gets the pool_type of this StudyTypeDefinition.  # noqa: E501


        :return: The pool_type of this StudyTypeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._pool_type

    @pool_type.setter
    def pool_type(self, pool_type):
        """Sets the pool_type of this StudyTypeDefinition.


        :param pool_type: The pool_type of this StudyTypeDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["primary", "secondary", "heavy", "studyMonitor"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and pool_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `pool_type` ({0}), must be one of {1}"  # noqa: E501
                .format(pool_type, allowed_values)
            )

        self._pool_type = pool_type

    @property
    def build_pool_type(self):
        """Gets the build_pool_type of this StudyTypeDefinition.  # noqa: E501


        :return: The build_pool_type of this StudyTypeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._build_pool_type

    @build_pool_type.setter
    def build_pool_type(self, build_pool_type):
        """Sets the build_pool_type of this StudyTypeDefinition.


        :param build_pool_type: The build_pool_type of this StudyTypeDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["primary", "secondary", "heavy", "studyMonitor"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and build_pool_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `build_pool_type` ({0}), must be one of {1}"  # noqa: E501
                .format(build_pool_type, allowed_values)
            )

        self._build_pool_type = build_pool_type

    @property
    def state(self):
        """Gets the state of this StudyTypeDefinition.  # noqa: E501


        :return: The state of this StudyTypeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this StudyTypeDefinition.


        :param state: The state of this StudyTypeDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def valid_for_transient(self):
        """Gets the valid_for_transient of this StudyTypeDefinition.  # noqa: E501


        :return: The valid_for_transient of this StudyTypeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._valid_for_transient

    @valid_for_transient.setter
    def valid_for_transient(self, valid_for_transient):
        """Sets the valid_for_transient of this StudyTypeDefinition.


        :param valid_for_transient: The valid_for_transient of this StudyTypeDefinition.  # noqa: E501
        :type: bool
        """

        self._valid_for_transient = valid_for_transient

    @property
    def valid_for_inline(self):
        """Gets the valid_for_inline of this StudyTypeDefinition.  # noqa: E501


        :return: The valid_for_inline of this StudyTypeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._valid_for_inline

    @valid_for_inline.setter
    def valid_for_inline(self, valid_for_inline):
        """Sets the valid_for_inline of this StudyTypeDefinition.


        :param valid_for_inline: The valid_for_inline of this StudyTypeDefinition.  # noqa: E501
        :type: bool
        """

        self._valid_for_inline = valid_for_inline

    @property
    def previous_definitions(self):
        """Gets the previous_definitions of this StudyTypeDefinition.  # noqa: E501


        :return: The previous_definitions of this StudyTypeDefinition.  # noqa: E501
        :rtype: list[IPreviousDefinitionStudyTypeDefinition]
        """
        return self._previous_definitions

    @previous_definitions.setter
    def previous_definitions(self, previous_definitions):
        """Sets the previous_definitions of this StudyTypeDefinition.


        :param previous_definitions: The previous_definitions of this StudyTypeDefinition.  # noqa: E501
        :type: list[IPreviousDefinitionStudyTypeDefinition]
        """

        self._previous_definitions = previous_definitions

    @property
    def implicit_sim_types(self):
        """Gets the implicit_sim_types of this StudyTypeDefinition.  # noqa: E501


        :return: The implicit_sim_types of this StudyTypeDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._implicit_sim_types

    @implicit_sim_types.setter
    def implicit_sim_types(self, implicit_sim_types):
        """Sets the implicit_sim_types of this StudyTypeDefinition.


        :param implicit_sim_types: The implicit_sim_types of this StudyTypeDefinition.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["StraightSim", "ApexSim", "QuasiStaticLap", "GenerateRacingLine", "DeploymentLap", "FailureSim", "SuccessSim", "Virtual4Post", "LimitSim", "DriveCycleSim", "DynamicLap", "DragSim", "DynamicMultiLap", "ThermalReplay", "TyreReplay", "PacejkaCanopyConverter", "AircraftSim", "ChannelInference", "Telemetry", "OvertakingLap", "TyreThermalDynamicLap", "TyreThermalDynamicMultiLap", "DynamicLapWithSLS", "DynamicLapHD", "IliadCollocation", "SubLimitSim", "ConstraintSatisfier"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(implicit_sim_types).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `implicit_sim_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(implicit_sim_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._implicit_sim_types = implicit_sim_types

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
        if not isinstance(other, StudyTypeDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StudyTypeDefinition):
            return True

        return self.to_dict() != other.to_dict()
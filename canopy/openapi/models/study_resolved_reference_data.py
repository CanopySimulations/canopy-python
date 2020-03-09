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


class StudyResolvedReferenceData(object):
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
        'creation_date': 'datetime',
        'modified_date': 'datetime',
        'user_id': 'str',
        'name': 'str',
        'study_document': 'StudyDocument',
        'input_hashes': 'list[StudyInputHashes]',
        'sim_types': 'list[str]',
        'sim_version': 'str',
        'is_support_session_open': 'bool'
    }

    attribute_map = {
        'creation_date': 'creationDate',
        'modified_date': 'modifiedDate',
        'user_id': 'userId',
        'name': 'name',
        'study_document': 'studyDocument',
        'input_hashes': 'inputHashes',
        'sim_types': 'simTypes',
        'sim_version': 'simVersion',
        'is_support_session_open': 'isSupportSessionOpen'
    }

    def __init__(self, creation_date=None, modified_date=None, user_id=None, name=None, study_document=None, input_hashes=None, sim_types=None, sim_version=None, is_support_session_open=None, local_vars_configuration=None):  # noqa: E501
        """StudyResolvedReferenceData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._creation_date = None
        self._modified_date = None
        self._user_id = None
        self._name = None
        self._study_document = None
        self._input_hashes = None
        self._sim_types = None
        self._sim_version = None
        self._is_support_session_open = None
        self.discriminator = None

        if creation_date is not None:
            self.creation_date = creation_date
        if modified_date is not None:
            self.modified_date = modified_date
        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name
        if study_document is not None:
            self.study_document = study_document
        if input_hashes is not None:
            self.input_hashes = input_hashes
        if sim_types is not None:
            self.sim_types = sim_types
        if sim_version is not None:
            self.sim_version = sim_version
        if is_support_session_open is not None:
            self.is_support_session_open = is_support_session_open

    @property
    def creation_date(self):
        """Gets the creation_date of this StudyResolvedReferenceData.  # noqa: E501


        :return: The creation_date of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this StudyResolvedReferenceData.


        :param creation_date: The creation_date of this StudyResolvedReferenceData.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def modified_date(self):
        """Gets the modified_date of this StudyResolvedReferenceData.  # noqa: E501


        :return: The modified_date of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this StudyResolvedReferenceData.


        :param modified_date: The modified_date of this StudyResolvedReferenceData.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def user_id(self):
        """Gets the user_id of this StudyResolvedReferenceData.  # noqa: E501


        :return: The user_id of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this StudyResolvedReferenceData.


        :param user_id: The user_id of this StudyResolvedReferenceData.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this StudyResolvedReferenceData.  # noqa: E501


        :return: The name of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StudyResolvedReferenceData.


        :param name: The name of this StudyResolvedReferenceData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def study_document(self):
        """Gets the study_document of this StudyResolvedReferenceData.  # noqa: E501


        :return: The study_document of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: StudyDocument
        """
        return self._study_document

    @study_document.setter
    def study_document(self, study_document):
        """Sets the study_document of this StudyResolvedReferenceData.


        :param study_document: The study_document of this StudyResolvedReferenceData.  # noqa: E501
        :type: StudyDocument
        """

        self._study_document = study_document

    @property
    def input_hashes(self):
        """Gets the input_hashes of this StudyResolvedReferenceData.  # noqa: E501


        :return: The input_hashes of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: list[StudyInputHashes]
        """
        return self._input_hashes

    @input_hashes.setter
    def input_hashes(self, input_hashes):
        """Sets the input_hashes of this StudyResolvedReferenceData.


        :param input_hashes: The input_hashes of this StudyResolvedReferenceData.  # noqa: E501
        :type: list[StudyInputHashes]
        """

        self._input_hashes = input_hashes

    @property
    def sim_types(self):
        """Gets the sim_types of this StudyResolvedReferenceData.  # noqa: E501


        :return: The sim_types of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: list[str]
        """
        return self._sim_types

    @sim_types.setter
    def sim_types(self, sim_types):
        """Sets the sim_types of this StudyResolvedReferenceData.


        :param sim_types: The sim_types of this StudyResolvedReferenceData.  # noqa: E501
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
    def sim_version(self):
        """Gets the sim_version of this StudyResolvedReferenceData.  # noqa: E501


        :return: The sim_version of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: str
        """
        return self._sim_version

    @sim_version.setter
    def sim_version(self, sim_version):
        """Sets the sim_version of this StudyResolvedReferenceData.


        :param sim_version: The sim_version of this StudyResolvedReferenceData.  # noqa: E501
        :type: str
        """

        self._sim_version = sim_version

    @property
    def is_support_session_open(self):
        """Gets the is_support_session_open of this StudyResolvedReferenceData.  # noqa: E501


        :return: The is_support_session_open of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: bool
        """
        return self._is_support_session_open

    @is_support_session_open.setter
    def is_support_session_open(self, is_support_session_open):
        """Sets the is_support_session_open of this StudyResolvedReferenceData.


        :param is_support_session_open: The is_support_session_open of this StudyResolvedReferenceData.  # noqa: E501
        :type: bool
        """

        self._is_support_session_open = is_support_session_open

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
        if not isinstance(other, StudyResolvedReferenceData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StudyResolvedReferenceData):
            return True

        return self.to_dict() != other.to_dict()
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


class StudyResolvedReferenceData(object):
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
        'creation_date': 'datetime',
        'modified_date': 'datetime',
        'user_id': 'UserId',
        'name': 'str',
        'study_document': 'StudyDocument',
        'input_hashes': 'list[StudyInputHashes]',
        'sim_types': 'list[str]',
        'sim_version': 'SimVersion'
    }

    attribute_map = {
        'creation_date': 'creationDate',
        'modified_date': 'modifiedDate',
        'user_id': 'userId',
        'name': 'name',
        'study_document': 'studyDocument',
        'input_hashes': 'inputHashes',
        'sim_types': 'simTypes',
        'sim_version': 'simVersion'
    }

    def __init__(self, creation_date=None, modified_date=None, user_id=None, name=None, study_document=None, input_hashes=None, sim_types=None, sim_version=None):  # noqa: E501
        """StudyResolvedReferenceData - a model defined in Swagger"""  # noqa: E501

        self._creation_date = None
        self._modified_date = None
        self._user_id = None
        self._name = None
        self._study_document = None
        self._input_hashes = None
        self._sim_types = None
        self._sim_version = None
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
        :rtype: UserId
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this StudyResolvedReferenceData.


        :param user_id: The user_id of this StudyResolvedReferenceData.  # noqa: E501
        :type: UserId
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
        if not set(sim_types).issubset(set(allowed_values)):
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
        :rtype: SimVersion
        """
        return self._sim_version

    @sim_version.setter
    def sim_version(self, sim_version):
        """Sets the sim_version of this StudyResolvedReferenceData.


        :param sim_version: The sim_version of this StudyResolvedReferenceData.  # noqa: E501
        :type: SimVersion
        """

        self._sim_version = sim_version

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
        if issubclass(StudyResolvedReferenceData, dict):
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
        if not isinstance(other, StudyResolvedReferenceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
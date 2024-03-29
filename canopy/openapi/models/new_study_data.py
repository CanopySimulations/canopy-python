# coding: utf-8

"""
    Canopy.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from canopy.openapi.configuration import Configuration


class NewStudyData(object):
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
        'name': 'str',
        'is_transient': 'bool',
        'study_type': 'str',
        'sources': 'list[NewStudyDataSource]',
        'properties': 'list[DocumentCustomPropertyData]',
        'study': 'object',
        'notes': 'str',
        'sim_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'is_transient': 'isTransient',
        'study_type': 'studyType',
        'sources': 'sources',
        'properties': 'properties',
        'study': 'study',
        'notes': 'notes',
        'sim_version': 'simVersion'
    }

    def __init__(self, name=None, is_transient=None, study_type=None, sources=None, properties=None, study=None, notes=None, sim_version=None, local_vars_configuration=None):  # noqa: E501
        """NewStudyData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._is_transient = None
        self._study_type = None
        self._sources = None
        self._properties = None
        self._study = None
        self._notes = None
        self._sim_version = None
        self.discriminator = None

        self.name = name
        if is_transient is not None:
            self.is_transient = is_transient
        if study_type is not None:
            self.study_type = study_type
        self.sources = sources
        self.properties = properties
        self.study = study
        self.notes = notes
        self.sim_version = sim_version

    @property
    def name(self):
        """Gets the name of this NewStudyData.  # noqa: E501


        :return: The name of this NewStudyData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewStudyData.


        :param name: The name of this NewStudyData.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def is_transient(self):
        """Gets the is_transient of this NewStudyData.  # noqa: E501


        :return: The is_transient of this NewStudyData.  # noqa: E501
        :rtype: bool
        """
        return self._is_transient

    @is_transient.setter
    def is_transient(self, is_transient):
        """Sets the is_transient of this NewStudyData.


        :param is_transient: The is_transient of this NewStudyData.  # noqa: E501
        :type is_transient: bool
        """

        self._is_transient = is_transient

    @property
    def study_type(self):
        """Gets the study_type of this NewStudyData.  # noqa: E501


        :return: The study_type of this NewStudyData.  # noqa: E501
        :rtype: str
        """
        return self._study_type

    @study_type.setter
    def study_type(self, study_type):
        """Sets the study_type of this NewStudyData.


        :param study_type: The study_type of this NewStudyData.  # noqa: E501
        :type study_type: str
        """

        self._study_type = study_type

    @property
    def sources(self):
        """Gets the sources of this NewStudyData.  # noqa: E501


        :return: The sources of this NewStudyData.  # noqa: E501
        :rtype: list[NewStudyDataSource]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this NewStudyData.


        :param sources: The sources of this NewStudyData.  # noqa: E501
        :type sources: list[NewStudyDataSource]
        """

        self._sources = sources

    @property
    def properties(self):
        """Gets the properties of this NewStudyData.  # noqa: E501


        :return: The properties of this NewStudyData.  # noqa: E501
        :rtype: list[DocumentCustomPropertyData]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this NewStudyData.


        :param properties: The properties of this NewStudyData.  # noqa: E501
        :type properties: list[DocumentCustomPropertyData]
        """

        self._properties = properties

    @property
    def study(self):
        """Gets the study of this NewStudyData.  # noqa: E501


        :return: The study of this NewStudyData.  # noqa: E501
        :rtype: object
        """
        return self._study

    @study.setter
    def study(self, study):
        """Sets the study of this NewStudyData.


        :param study: The study of this NewStudyData.  # noqa: E501
        :type study: object
        """

        self._study = study

    @property
    def notes(self):
        """Gets the notes of this NewStudyData.  # noqa: E501


        :return: The notes of this NewStudyData.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this NewStudyData.


        :param notes: The notes of this NewStudyData.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def sim_version(self):
        """Gets the sim_version of this NewStudyData.  # noqa: E501


        :return: The sim_version of this NewStudyData.  # noqa: E501
        :rtype: str
        """
        return self._sim_version

    @sim_version.setter
    def sim_version(self, sim_version):
        """Sets the sim_version of this NewStudyData.


        :param sim_version: The sim_version of this NewStudyData.  # noqa: E501
        :type sim_version: str
        """

        self._sim_version = sim_version

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewStudyData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewStudyData):
            return True

        return self.to_dict() != other.to_dict()

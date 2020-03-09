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


class GetSimVersionDocumentsQueryResult(object):
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
        'sim_version': 'str',
        'documents': 'list[TextDocumentOptionalContent]',
        'units': 'dict(str, str)'
    }

    attribute_map = {
        'sim_version': 'simVersion',
        'documents': 'documents',
        'units': 'units'
    }

    def __init__(self, sim_version=None, documents=None, units=None, local_vars_configuration=None):  # noqa: E501
        """GetSimVersionDocumentsQueryResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sim_version = None
        self._documents = None
        self._units = None
        self.discriminator = None

        if sim_version is not None:
            self.sim_version = sim_version
        if documents is not None:
            self.documents = documents
        if units is not None:
            self.units = units

    @property
    def sim_version(self):
        """Gets the sim_version of this GetSimVersionDocumentsQueryResult.  # noqa: E501


        :return: The sim_version of this GetSimVersionDocumentsQueryResult.  # noqa: E501
        :rtype: str
        """
        return self._sim_version

    @sim_version.setter
    def sim_version(self, sim_version):
        """Sets the sim_version of this GetSimVersionDocumentsQueryResult.


        :param sim_version: The sim_version of this GetSimVersionDocumentsQueryResult.  # noqa: E501
        :type: str
        """

        self._sim_version = sim_version

    @property
    def documents(self):
        """Gets the documents of this GetSimVersionDocumentsQueryResult.  # noqa: E501


        :return: The documents of this GetSimVersionDocumentsQueryResult.  # noqa: E501
        :rtype: list[TextDocumentOptionalContent]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this GetSimVersionDocumentsQueryResult.


        :param documents: The documents of this GetSimVersionDocumentsQueryResult.  # noqa: E501
        :type: list[TextDocumentOptionalContent]
        """

        self._documents = documents

    @property
    def units(self):
        """Gets the units of this GetSimVersionDocumentsQueryResult.  # noqa: E501


        :return: The units of this GetSimVersionDocumentsQueryResult.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this GetSimVersionDocumentsQueryResult.


        :param units: The units of this GetSimVersionDocumentsQueryResult.  # noqa: E501
        :type: dict(str, str)
        """

        self._units = units

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
        if not isinstance(other, GetSimVersionDocumentsQueryResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSimVersionDocumentsQueryResult):
            return True

        return self.to_dict() != other.to_dict()
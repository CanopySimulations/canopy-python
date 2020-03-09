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


class StudyJobDocumentsAndContinuationToken(object):
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
        'documents': 'list[CanopyDocument]',
        'continuation_token': 'str',
        'has_more_results': 'bool'
    }

    attribute_map = {
        'documents': 'documents',
        'continuation_token': 'continuationToken',
        'has_more_results': 'hasMoreResults'
    }

    def __init__(self, documents=None, continuation_token=None, has_more_results=None, local_vars_configuration=None):  # noqa: E501
        """StudyJobDocumentsAndContinuationToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._documents = None
        self._continuation_token = None
        self._has_more_results = None
        self.discriminator = None

        if documents is not None:
            self.documents = documents
        if continuation_token is not None:
            self.continuation_token = continuation_token
        if has_more_results is not None:
            self.has_more_results = has_more_results

    @property
    def documents(self):
        """Gets the documents of this StudyJobDocumentsAndContinuationToken.  # noqa: E501


        :return: The documents of this StudyJobDocumentsAndContinuationToken.  # noqa: E501
        :rtype: list[CanopyDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this StudyJobDocumentsAndContinuationToken.


        :param documents: The documents of this StudyJobDocumentsAndContinuationToken.  # noqa: E501
        :type: list[CanopyDocument]
        """

        self._documents = documents

    @property
    def continuation_token(self):
        """Gets the continuation_token of this StudyJobDocumentsAndContinuationToken.  # noqa: E501


        :return: The continuation_token of this StudyJobDocumentsAndContinuationToken.  # noqa: E501
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this StudyJobDocumentsAndContinuationToken.


        :param continuation_token: The continuation_token of this StudyJobDocumentsAndContinuationToken.  # noqa: E501
        :type: str
        """

        self._continuation_token = continuation_token

    @property
    def has_more_results(self):
        """Gets the has_more_results of this StudyJobDocumentsAndContinuationToken.  # noqa: E501


        :return: The has_more_results of this StudyJobDocumentsAndContinuationToken.  # noqa: E501
        :rtype: bool
        """
        return self._has_more_results

    @has_more_results.setter
    def has_more_results(self, has_more_results):
        """Sets the has_more_results of this StudyJobDocumentsAndContinuationToken.


        :param has_more_results: The has_more_results of this StudyJobDocumentsAndContinuationToken.  # noqa: E501
        :type: bool
        """

        self._has_more_results = has_more_results

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
        if not isinstance(other, StudyJobDocumentsAndContinuationToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StudyJobDocumentsAndContinuationToken):
            return True

        return self.to_dict() != other.to_dict()
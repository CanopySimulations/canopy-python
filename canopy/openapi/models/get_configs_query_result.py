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


class GetConfigsQueryResult(object):
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
        'query_results': 'DocumentsAndContinuationToken',
        'group_results': 'list[DocumentCustomPropertyGroup]',
        'user_information': 'DocumentUserInformation'
    }

    attribute_map = {
        'query_results': 'queryResults',
        'group_results': 'groupResults',
        'user_information': 'userInformation'
    }

    def __init__(self, query_results=None, group_results=None, user_information=None, local_vars_configuration=None):  # noqa: E501
        """GetConfigsQueryResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query_results = None
        self._group_results = None
        self._user_information = None
        self.discriminator = None

        if query_results is not None:
            self.query_results = query_results
        if group_results is not None:
            self.group_results = group_results
        if user_information is not None:
            self.user_information = user_information

    @property
    def query_results(self):
        """Gets the query_results of this GetConfigsQueryResult.  # noqa: E501


        :return: The query_results of this GetConfigsQueryResult.  # noqa: E501
        :rtype: DocumentsAndContinuationToken
        """
        return self._query_results

    @query_results.setter
    def query_results(self, query_results):
        """Sets the query_results of this GetConfigsQueryResult.


        :param query_results: The query_results of this GetConfigsQueryResult.  # noqa: E501
        :type: DocumentsAndContinuationToken
        """

        self._query_results = query_results

    @property
    def group_results(self):
        """Gets the group_results of this GetConfigsQueryResult.  # noqa: E501


        :return: The group_results of this GetConfigsQueryResult.  # noqa: E501
        :rtype: list[DocumentCustomPropertyGroup]
        """
        return self._group_results

    @group_results.setter
    def group_results(self, group_results):
        """Sets the group_results of this GetConfigsQueryResult.


        :param group_results: The group_results of this GetConfigsQueryResult.  # noqa: E501
        :type: list[DocumentCustomPropertyGroup]
        """

        self._group_results = group_results

    @property
    def user_information(self):
        """Gets the user_information of this GetConfigsQueryResult.  # noqa: E501


        :return: The user_information of this GetConfigsQueryResult.  # noqa: E501
        :rtype: DocumentUserInformation
        """
        return self._user_information

    @user_information.setter
    def user_information(self, user_information):
        """Sets the user_information of this GetConfigsQueryResult.


        :param user_information: The user_information of this GetConfigsQueryResult.  # noqa: E501
        :type: DocumentUserInformation
        """

        self._user_information = user_information

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
        if not isinstance(other, GetConfigsQueryResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetConfigsQueryResult):
            return True

        return self.to_dict() != other.to_dict()

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


class StudyDocumentStudyDocumentDataSource(object):
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
        'config_type': 'DocumentSubType',
        'user_id': 'UserId',
        'config_id': 'str',
        'name': 'str',
        'is_edited': 'bool'
    }

    attribute_map = {
        'config_type': 'configType',
        'user_id': 'userId',
        'config_id': 'configId',
        'name': 'name',
        'is_edited': 'isEdited'
    }

    def __init__(self, config_type=None, user_id=None, config_id=None, name=None, is_edited=None):  # noqa: E501
        """StudyDocumentStudyDocumentDataSource - a model defined in Swagger"""  # noqa: E501

        self._config_type = None
        self._user_id = None
        self._config_id = None
        self._name = None
        self._is_edited = None
        self.discriminator = None

        if config_type is not None:
            self.config_type = config_type
        if user_id is not None:
            self.user_id = user_id
        if config_id is not None:
            self.config_id = config_id
        if name is not None:
            self.name = name
        if is_edited is not None:
            self.is_edited = is_edited

    @property
    def config_type(self):
        """Gets the config_type of this StudyDocumentStudyDocumentDataSource.  # noqa: E501


        :return: The config_type of this StudyDocumentStudyDocumentDataSource.  # noqa: E501
        :rtype: DocumentSubType
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this StudyDocumentStudyDocumentDataSource.


        :param config_type: The config_type of this StudyDocumentStudyDocumentDataSource.  # noqa: E501
        :type: DocumentSubType
        """

        self._config_type = config_type

    @property
    def user_id(self):
        """Gets the user_id of this StudyDocumentStudyDocumentDataSource.  # noqa: E501


        :return: The user_id of this StudyDocumentStudyDocumentDataSource.  # noqa: E501
        :rtype: UserId
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this StudyDocumentStudyDocumentDataSource.


        :param user_id: The user_id of this StudyDocumentStudyDocumentDataSource.  # noqa: E501
        :type: UserId
        """

        self._user_id = user_id

    @property
    def config_id(self):
        """Gets the config_id of this StudyDocumentStudyDocumentDataSource.  # noqa: E501


        :return: The config_id of this StudyDocumentStudyDocumentDataSource.  # noqa: E501
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this StudyDocumentStudyDocumentDataSource.


        :param config_id: The config_id of this StudyDocumentStudyDocumentDataSource.  # noqa: E501
        :type: str
        """

        self._config_id = config_id

    @property
    def name(self):
        """Gets the name of this StudyDocumentStudyDocumentDataSource.  # noqa: E501


        :return: The name of this StudyDocumentStudyDocumentDataSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StudyDocumentStudyDocumentDataSource.


        :param name: The name of this StudyDocumentStudyDocumentDataSource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_edited(self):
        """Gets the is_edited of this StudyDocumentStudyDocumentDataSource.  # noqa: E501


        :return: The is_edited of this StudyDocumentStudyDocumentDataSource.  # noqa: E501
        :rtype: bool
        """
        return self._is_edited

    @is_edited.setter
    def is_edited(self, is_edited):
        """Sets the is_edited of this StudyDocumentStudyDocumentDataSource.


        :param is_edited: The is_edited of this StudyDocumentStudyDocumentDataSource.  # noqa: E501
        :type: bool
        """

        self._is_edited = is_edited

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
        if issubclass(StudyDocumentStudyDocumentDataSource, dict):
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
        if not isinstance(other, StudyDocumentStudyDocumentDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

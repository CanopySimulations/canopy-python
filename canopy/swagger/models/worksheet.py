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


class Worksheet(object):
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
        'tenant_id': 'TenantId',
        'user_id': 'UserId',
        'worksheet_id': 'DocumentId',
        'name': 'str',
        'outline': 'WorksheetOutline',
        'resolved_labels': 'CollatedWorksheetLabels',
        'resolved_references': 'WorksheetResolvedReferences',
        'support_session': 'SupportSession',
        'properties': 'object',
        'notes': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        'user_id': 'userId',
        'worksheet_id': 'worksheetId',
        'name': 'name',
        'outline': 'outline',
        'resolved_labels': 'resolvedLabels',
        'resolved_references': 'resolvedReferences',
        'support_session': 'supportSession',
        'properties': 'properties',
        'notes': 'notes'
    }

    def __init__(self, tenant_id=None, user_id=None, worksheet_id=None, name=None, outline=None, resolved_labels=None, resolved_references=None, support_session=None, properties=None, notes=None):  # noqa: E501
        """Worksheet - a model defined in Swagger"""  # noqa: E501

        self._tenant_id = None
        self._user_id = None
        self._worksheet_id = None
        self._name = None
        self._outline = None
        self._resolved_labels = None
        self._resolved_references = None
        self._support_session = None
        self._properties = None
        self._notes = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if user_id is not None:
            self.user_id = user_id
        if worksheet_id is not None:
            self.worksheet_id = worksheet_id
        if name is not None:
            self.name = name
        if outline is not None:
            self.outline = outline
        if resolved_labels is not None:
            self.resolved_labels = resolved_labels
        if resolved_references is not None:
            self.resolved_references = resolved_references
        if support_session is not None:
            self.support_session = support_session
        if properties is not None:
            self.properties = properties
        if notes is not None:
            self.notes = notes

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Worksheet.  # noqa: E501


        :return: The tenant_id of this Worksheet.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Worksheet.


        :param tenant_id: The tenant_id of this Worksheet.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def user_id(self):
        """Gets the user_id of this Worksheet.  # noqa: E501


        :return: The user_id of this Worksheet.  # noqa: E501
        :rtype: UserId
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Worksheet.


        :param user_id: The user_id of this Worksheet.  # noqa: E501
        :type: UserId
        """

        self._user_id = user_id

    @property
    def worksheet_id(self):
        """Gets the worksheet_id of this Worksheet.  # noqa: E501


        :return: The worksheet_id of this Worksheet.  # noqa: E501
        :rtype: DocumentId
        """
        return self._worksheet_id

    @worksheet_id.setter
    def worksheet_id(self, worksheet_id):
        """Sets the worksheet_id of this Worksheet.


        :param worksheet_id: The worksheet_id of this Worksheet.  # noqa: E501
        :type: DocumentId
        """

        self._worksheet_id = worksheet_id

    @property
    def name(self):
        """Gets the name of this Worksheet.  # noqa: E501


        :return: The name of this Worksheet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Worksheet.


        :param name: The name of this Worksheet.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def outline(self):
        """Gets the outline of this Worksheet.  # noqa: E501


        :return: The outline of this Worksheet.  # noqa: E501
        :rtype: WorksheetOutline
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this Worksheet.


        :param outline: The outline of this Worksheet.  # noqa: E501
        :type: WorksheetOutline
        """

        self._outline = outline

    @property
    def resolved_labels(self):
        """Gets the resolved_labels of this Worksheet.  # noqa: E501


        :return: The resolved_labels of this Worksheet.  # noqa: E501
        :rtype: CollatedWorksheetLabels
        """
        return self._resolved_labels

    @resolved_labels.setter
    def resolved_labels(self, resolved_labels):
        """Sets the resolved_labels of this Worksheet.


        :param resolved_labels: The resolved_labels of this Worksheet.  # noqa: E501
        :type: CollatedWorksheetLabels
        """

        self._resolved_labels = resolved_labels

    @property
    def resolved_references(self):
        """Gets the resolved_references of this Worksheet.  # noqa: E501


        :return: The resolved_references of this Worksheet.  # noqa: E501
        :rtype: WorksheetResolvedReferences
        """
        return self._resolved_references

    @resolved_references.setter
    def resolved_references(self, resolved_references):
        """Sets the resolved_references of this Worksheet.


        :param resolved_references: The resolved_references of this Worksheet.  # noqa: E501
        :type: WorksheetResolvedReferences
        """

        self._resolved_references = resolved_references

    @property
    def support_session(self):
        """Gets the support_session of this Worksheet.  # noqa: E501


        :return: The support_session of this Worksheet.  # noqa: E501
        :rtype: SupportSession
        """
        return self._support_session

    @support_session.setter
    def support_session(self, support_session):
        """Sets the support_session of this Worksheet.


        :param support_session: The support_session of this Worksheet.  # noqa: E501
        :type: SupportSession
        """

        self._support_session = support_session

    @property
    def properties(self):
        """Gets the properties of this Worksheet.  # noqa: E501


        :return: The properties of this Worksheet.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Worksheet.


        :param properties: The properties of this Worksheet.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def notes(self):
        """Gets the notes of this Worksheet.  # noqa: E501


        :return: The notes of this Worksheet.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Worksheet.


        :param notes: The notes of this Worksheet.  # noqa: E501
        :type: str
        """

        self._notes = notes

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
        if issubclass(Worksheet, dict):
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
        if not isinstance(other, Worksheet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
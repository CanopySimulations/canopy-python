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


class TenantSettingsPutTenantChannelImportMappingsRequest(object):
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
        'channel_import_mappings': 'list[ChannelImportMapping]'
    }

    attribute_map = {
        'channel_import_mappings': 'channelImportMappings'
    }

    def __init__(self, channel_import_mappings=None, local_vars_configuration=None):  # noqa: E501
        """TenantSettingsPutTenantChannelImportMappingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._channel_import_mappings = None
        self.discriminator = None

        self.channel_import_mappings = channel_import_mappings

    @property
    def channel_import_mappings(self):
        """Gets the channel_import_mappings of this TenantSettingsPutTenantChannelImportMappingsRequest.  # noqa: E501


        :return: The channel_import_mappings of this TenantSettingsPutTenantChannelImportMappingsRequest.  # noqa: E501
        :rtype: list[ChannelImportMapping]
        """
        return self._channel_import_mappings

    @channel_import_mappings.setter
    def channel_import_mappings(self, channel_import_mappings):
        """Sets the channel_import_mappings of this TenantSettingsPutTenantChannelImportMappingsRequest.


        :param channel_import_mappings: The channel_import_mappings of this TenantSettingsPutTenantChannelImportMappingsRequest.  # noqa: E501
        :type channel_import_mappings: list[ChannelImportMapping]
        """

        self._channel_import_mappings = channel_import_mappings

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
        if not isinstance(other, TenantSettingsPutTenantChannelImportMappingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TenantSettingsPutTenantChannelImportMappingsRequest):
            return True

        return self.to_dict() != other.to_dict()
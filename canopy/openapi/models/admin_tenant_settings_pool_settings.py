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


class AdminTenantSettingsPoolSettings(object):
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
        'pool_id': 'object',
        'auto_scale_formula': 'str'
    }

    attribute_map = {
        'pool_id': 'poolId',
        'auto_scale_formula': 'autoScaleFormula'
    }

    def __init__(self, pool_id=None, auto_scale_formula=None, local_vars_configuration=None):  # noqa: E501
        """AdminTenantSettingsPoolSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._pool_id = None
        self._auto_scale_formula = None
        self.discriminator = None

        self.pool_id = pool_id
        self.auto_scale_formula = auto_scale_formula

    @property
    def pool_id(self):
        """Gets the pool_id of this AdminTenantSettingsPoolSettings.  # noqa: E501


        :return: The pool_id of this AdminTenantSettingsPoolSettings.  # noqa: E501
        :rtype: object
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this AdminTenantSettingsPoolSettings.


        :param pool_id: The pool_id of this AdminTenantSettingsPoolSettings.  # noqa: E501
        :type pool_id: object
        """
        if self.local_vars_configuration.client_side_validation and pool_id is None:  # noqa: E501
            raise ValueError("Invalid value for `pool_id`, must not be `None`")  # noqa: E501

        self._pool_id = pool_id

    @property
    def auto_scale_formula(self):
        """Gets the auto_scale_formula of this AdminTenantSettingsPoolSettings.  # noqa: E501


        :return: The auto_scale_formula of this AdminTenantSettingsPoolSettings.  # noqa: E501
        :rtype: str
        """
        return self._auto_scale_formula

    @auto_scale_formula.setter
    def auto_scale_formula(self, auto_scale_formula):
        """Sets the auto_scale_formula of this AdminTenantSettingsPoolSettings.


        :param auto_scale_formula: The auto_scale_formula of this AdminTenantSettingsPoolSettings.  # noqa: E501
        :type auto_scale_formula: str
        """
        if self.local_vars_configuration.client_side_validation and auto_scale_formula is None:  # noqa: E501
            raise ValueError("Invalid value for `auto_scale_formula`, must not be `None`")  # noqa: E501

        self._auto_scale_formula = auto_scale_formula

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
        if not isinstance(other, AdminTenantSettingsPoolSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdminTenantSettingsPoolSettings):
            return True

        return self.to_dict() != other.to_dict()

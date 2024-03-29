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


class GetPoolStatusQueryResult(object):
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
        'pool_state': 'PoolState',
        'allocation_state': 'AllocationState',
        'current_dedicated': 'int',
        'target_dedicated': 'int',
        'current_low_priority': 'int',
        'target_low_priority': 'int',
        'maximum_tasks_per_node': 'int',
        'schedulable_compute_nodes': 'int',
        'running_tasks': 'int',
        'compute_nodes': 'list[ComputeNodeResult]'
    }

    attribute_map = {
        'pool_id': 'poolId',
        'pool_state': 'poolState',
        'allocation_state': 'allocationState',
        'current_dedicated': 'currentDedicated',
        'target_dedicated': 'targetDedicated',
        'current_low_priority': 'currentLowPriority',
        'target_low_priority': 'targetLowPriority',
        'maximum_tasks_per_node': 'maximumTasksPerNode',
        'schedulable_compute_nodes': 'schedulableComputeNodes',
        'running_tasks': 'runningTasks',
        'compute_nodes': 'computeNodes'
    }

    def __init__(self, pool_id=None, pool_state=None, allocation_state=None, current_dedicated=None, target_dedicated=None, current_low_priority=None, target_low_priority=None, maximum_tasks_per_node=None, schedulable_compute_nodes=None, running_tasks=None, compute_nodes=None, local_vars_configuration=None):  # noqa: E501
        """GetPoolStatusQueryResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._pool_id = None
        self._pool_state = None
        self._allocation_state = None
        self._current_dedicated = None
        self._target_dedicated = None
        self._current_low_priority = None
        self._target_low_priority = None
        self._maximum_tasks_per_node = None
        self._schedulable_compute_nodes = None
        self._running_tasks = None
        self._compute_nodes = None
        self.discriminator = None

        self.pool_id = pool_id
        self.pool_state = pool_state
        self.allocation_state = allocation_state
        self.current_dedicated = current_dedicated
        self.target_dedicated = target_dedicated
        self.current_low_priority = current_low_priority
        self.target_low_priority = target_low_priority
        self.maximum_tasks_per_node = maximum_tasks_per_node
        self.schedulable_compute_nodes = schedulable_compute_nodes
        self.running_tasks = running_tasks
        self.compute_nodes = compute_nodes

    @property
    def pool_id(self):
        """Gets the pool_id of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The pool_id of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: object
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this GetPoolStatusQueryResult.


        :param pool_id: The pool_id of this GetPoolStatusQueryResult.  # noqa: E501
        :type pool_id: object
        """
        if self.local_vars_configuration.client_side_validation and pool_id is None:  # noqa: E501
            raise ValueError("Invalid value for `pool_id`, must not be `None`")  # noqa: E501

        self._pool_id = pool_id

    @property
    def pool_state(self):
        """Gets the pool_state of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The pool_state of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: PoolState
        """
        return self._pool_state

    @pool_state.setter
    def pool_state(self, pool_state):
        """Sets the pool_state of this GetPoolStatusQueryResult.


        :param pool_state: The pool_state of this GetPoolStatusQueryResult.  # noqa: E501
        :type pool_state: PoolState
        """

        self._pool_state = pool_state

    @property
    def allocation_state(self):
        """Gets the allocation_state of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The allocation_state of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: AllocationState
        """
        return self._allocation_state

    @allocation_state.setter
    def allocation_state(self, allocation_state):
        """Sets the allocation_state of this GetPoolStatusQueryResult.


        :param allocation_state: The allocation_state of this GetPoolStatusQueryResult.  # noqa: E501
        :type allocation_state: AllocationState
        """

        self._allocation_state = allocation_state

    @property
    def current_dedicated(self):
        """Gets the current_dedicated of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The current_dedicated of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: int
        """
        return self._current_dedicated

    @current_dedicated.setter
    def current_dedicated(self, current_dedicated):
        """Sets the current_dedicated of this GetPoolStatusQueryResult.


        :param current_dedicated: The current_dedicated of this GetPoolStatusQueryResult.  # noqa: E501
        :type current_dedicated: int
        """
        if self.local_vars_configuration.client_side_validation and current_dedicated is None:  # noqa: E501
            raise ValueError("Invalid value for `current_dedicated`, must not be `None`")  # noqa: E501

        self._current_dedicated = current_dedicated

    @property
    def target_dedicated(self):
        """Gets the target_dedicated of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The target_dedicated of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: int
        """
        return self._target_dedicated

    @target_dedicated.setter
    def target_dedicated(self, target_dedicated):
        """Sets the target_dedicated of this GetPoolStatusQueryResult.


        :param target_dedicated: The target_dedicated of this GetPoolStatusQueryResult.  # noqa: E501
        :type target_dedicated: int
        """
        if self.local_vars_configuration.client_side_validation and target_dedicated is None:  # noqa: E501
            raise ValueError("Invalid value for `target_dedicated`, must not be `None`")  # noqa: E501

        self._target_dedicated = target_dedicated

    @property
    def current_low_priority(self):
        """Gets the current_low_priority of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The current_low_priority of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: int
        """
        return self._current_low_priority

    @current_low_priority.setter
    def current_low_priority(self, current_low_priority):
        """Sets the current_low_priority of this GetPoolStatusQueryResult.


        :param current_low_priority: The current_low_priority of this GetPoolStatusQueryResult.  # noqa: E501
        :type current_low_priority: int
        """
        if self.local_vars_configuration.client_side_validation and current_low_priority is None:  # noqa: E501
            raise ValueError("Invalid value for `current_low_priority`, must not be `None`")  # noqa: E501

        self._current_low_priority = current_low_priority

    @property
    def target_low_priority(self):
        """Gets the target_low_priority of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The target_low_priority of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: int
        """
        return self._target_low_priority

    @target_low_priority.setter
    def target_low_priority(self, target_low_priority):
        """Sets the target_low_priority of this GetPoolStatusQueryResult.


        :param target_low_priority: The target_low_priority of this GetPoolStatusQueryResult.  # noqa: E501
        :type target_low_priority: int
        """
        if self.local_vars_configuration.client_side_validation and target_low_priority is None:  # noqa: E501
            raise ValueError("Invalid value for `target_low_priority`, must not be `None`")  # noqa: E501

        self._target_low_priority = target_low_priority

    @property
    def maximum_tasks_per_node(self):
        """Gets the maximum_tasks_per_node of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The maximum_tasks_per_node of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: int
        """
        return self._maximum_tasks_per_node

    @maximum_tasks_per_node.setter
    def maximum_tasks_per_node(self, maximum_tasks_per_node):
        """Sets the maximum_tasks_per_node of this GetPoolStatusQueryResult.


        :param maximum_tasks_per_node: The maximum_tasks_per_node of this GetPoolStatusQueryResult.  # noqa: E501
        :type maximum_tasks_per_node: int
        """
        if self.local_vars_configuration.client_side_validation and maximum_tasks_per_node is None:  # noqa: E501
            raise ValueError("Invalid value for `maximum_tasks_per_node`, must not be `None`")  # noqa: E501

        self._maximum_tasks_per_node = maximum_tasks_per_node

    @property
    def schedulable_compute_nodes(self):
        """Gets the schedulable_compute_nodes of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The schedulable_compute_nodes of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: int
        """
        return self._schedulable_compute_nodes

    @schedulable_compute_nodes.setter
    def schedulable_compute_nodes(self, schedulable_compute_nodes):
        """Sets the schedulable_compute_nodes of this GetPoolStatusQueryResult.


        :param schedulable_compute_nodes: The schedulable_compute_nodes of this GetPoolStatusQueryResult.  # noqa: E501
        :type schedulable_compute_nodes: int
        """
        if self.local_vars_configuration.client_side_validation and schedulable_compute_nodes is None:  # noqa: E501
            raise ValueError("Invalid value for `schedulable_compute_nodes`, must not be `None`")  # noqa: E501

        self._schedulable_compute_nodes = schedulable_compute_nodes

    @property
    def running_tasks(self):
        """Gets the running_tasks of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The running_tasks of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: int
        """
        return self._running_tasks

    @running_tasks.setter
    def running_tasks(self, running_tasks):
        """Sets the running_tasks of this GetPoolStatusQueryResult.


        :param running_tasks: The running_tasks of this GetPoolStatusQueryResult.  # noqa: E501
        :type running_tasks: int
        """
        if self.local_vars_configuration.client_side_validation and running_tasks is None:  # noqa: E501
            raise ValueError("Invalid value for `running_tasks`, must not be `None`")  # noqa: E501

        self._running_tasks = running_tasks

    @property
    def compute_nodes(self):
        """Gets the compute_nodes of this GetPoolStatusQueryResult.  # noqa: E501


        :return: The compute_nodes of this GetPoolStatusQueryResult.  # noqa: E501
        :rtype: list[ComputeNodeResult]
        """
        return self._compute_nodes

    @compute_nodes.setter
    def compute_nodes(self, compute_nodes):
        """Sets the compute_nodes of this GetPoolStatusQueryResult.


        :param compute_nodes: The compute_nodes of this GetPoolStatusQueryResult.  # noqa: E501
        :type compute_nodes: list[ComputeNodeResult]
        """
        if self.local_vars_configuration.client_side_validation and compute_nodes is None:  # noqa: E501
            raise ValueError("Invalid value for `compute_nodes`, must not be `None`")  # noqa: E501

        self._compute_nodes = compute_nodes

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
        if not isinstance(other, GetPoolStatusQueryResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetPoolStatusQueryResult):
            return True

        return self.to_dict() != other.to_dict()

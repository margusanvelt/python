# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1NodeSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'config_source': 'V1NodeConfigSource',
        'external_id': 'str',
        'pod_cidr': 'str',
        'provider_id': 'str',
        'taints': 'list[V1Taint]',
        'unschedulable': 'bool'
    }

    attribute_map = {
        'config_source': 'configSource',
        'external_id': 'externalID',
        'pod_cidr': 'podCIDR',
        'provider_id': 'providerID',
        'taints': 'taints',
        'unschedulable': 'unschedulable'
    }

    def __init__(self, config_source=None, external_id=None, pod_cidr=None, provider_id=None, taints=None, unschedulable=None):
        """
        V1NodeSpec - a model defined in Swagger
        """

        self._config_source = None
        self._external_id = None
        self._pod_cidr = None
        self._provider_id = None
        self._taints = None
        self._unschedulable = None
        self.discriminator = None

        if config_source is not None:
          self.config_source = config_source
        if external_id is not None:
          self.external_id = external_id
        if pod_cidr is not None:
          self.pod_cidr = pod_cidr
        if provider_id is not None:
          self.provider_id = provider_id
        if taints is not None:
          self.taints = taints
        if unschedulable is not None:
          self.unschedulable = unschedulable

    @property
    def config_source(self):
        """
        Gets the config_source of this V1NodeSpec.
        If specified, the source to get node configuration from The DynamicKubeletConfig feature gate must be enabled for the Kubelet to use this field

        :return: The config_source of this V1NodeSpec.
        :rtype: V1NodeConfigSource
        """
        return self._config_source

    @config_source.setter
    def config_source(self, config_source):
        """
        Sets the config_source of this V1NodeSpec.
        If specified, the source to get node configuration from The DynamicKubeletConfig feature gate must be enabled for the Kubelet to use this field

        :param config_source: The config_source of this V1NodeSpec.
        :type: V1NodeConfigSource
        """

        self._config_source = config_source

    @property
    def external_id(self):
        """
        Gets the external_id of this V1NodeSpec.
        Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966

        :return: The external_id of this V1NodeSpec.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this V1NodeSpec.
        Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966

        :param external_id: The external_id of this V1NodeSpec.
        :type: str
        """

        self._external_id = external_id

    @property
    def pod_cidr(self):
        """
        Gets the pod_cidr of this V1NodeSpec.
        PodCIDR represents the pod IP range assigned to the node.

        :return: The pod_cidr of this V1NodeSpec.
        :rtype: str
        """
        return self._pod_cidr

    @pod_cidr.setter
    def pod_cidr(self, pod_cidr):
        """
        Sets the pod_cidr of this V1NodeSpec.
        PodCIDR represents the pod IP range assigned to the node.

        :param pod_cidr: The pod_cidr of this V1NodeSpec.
        :type: str
        """

        self._pod_cidr = pod_cidr

    @property
    def provider_id(self):
        """
        Gets the provider_id of this V1NodeSpec.
        ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>

        :return: The provider_id of this V1NodeSpec.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """
        Sets the provider_id of this V1NodeSpec.
        ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>

        :param provider_id: The provider_id of this V1NodeSpec.
        :type: str
        """

        self._provider_id = provider_id

    @property
    def taints(self):
        """
        Gets the taints of this V1NodeSpec.
        If specified, the node's taints.

        :return: The taints of this V1NodeSpec.
        :rtype: list[V1Taint]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        """
        Sets the taints of this V1NodeSpec.
        If specified, the node's taints.

        :param taints: The taints of this V1NodeSpec.
        :type: list[V1Taint]
        """

        self._taints = taints

    @property
    def unschedulable(self):
        """
        Gets the unschedulable of this V1NodeSpec.
        Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration

        :return: The unschedulable of this V1NodeSpec.
        :rtype: bool
        """
        return self._unschedulable

    @unschedulable.setter
    def unschedulable(self, unschedulable):
        """
        Sets the unschedulable of this V1NodeSpec.
        Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration

        :param unschedulable: The unschedulable of this V1NodeSpec.
        :type: bool
        """

        self._unschedulable = unschedulable

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1NodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class V1ConfigMapKeySelector(object):
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
        'key': 'str',
        'name': 'str',
        'optional': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'optional': 'optional'
    }

    def __init__(self, key=None, name=None, optional=None):
        """
        V1ConfigMapKeySelector - a model defined in Swagger
        """

        self._key = None
        self._name = None
        self._optional = None
        self.discriminator = None

        self.key = key
        if name is not None:
          self.name = name
        if optional is not None:
          self.optional = optional

    @property
    def key(self):
        """
        Gets the key of this V1ConfigMapKeySelector.
        The key to select.

        :return: The key of this V1ConfigMapKeySelector.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this V1ConfigMapKeySelector.
        The key to select.

        :param key: The key of this V1ConfigMapKeySelector.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def name(self):
        """
        Gets the name of this V1ConfigMapKeySelector.
        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :return: The name of this V1ConfigMapKeySelector.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ConfigMapKeySelector.
        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :param name: The name of this V1ConfigMapKeySelector.
        :type: str
        """

        self._name = name

    @property
    def optional(self):
        """
        Gets the optional of this V1ConfigMapKeySelector.
        Specify whether the ConfigMap or it's key must be defined

        :return: The optional of this V1ConfigMapKeySelector.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """
        Sets the optional of this V1ConfigMapKeySelector.
        Specify whether the ConfigMap or it's key must be defined

        :param optional: The optional of this V1ConfigMapKeySelector.
        :type: bool
        """

        self._optional = optional

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
        if not isinstance(other, V1ConfigMapKeySelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

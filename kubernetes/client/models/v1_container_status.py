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


class V1ContainerStatus(object):
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
        'container_id': 'str',
        'image': 'str',
        'image_id': 'str',
        'last_state': 'V1ContainerState',
        'name': 'str',
        'ready': 'bool',
        'restart_count': 'int',
        'state': 'V1ContainerState'
    }

    attribute_map = {
        'container_id': 'containerID',
        'image': 'image',
        'image_id': 'imageID',
        'last_state': 'lastState',
        'name': 'name',
        'ready': 'ready',
        'restart_count': 'restartCount',
        'state': 'state'
    }

    def __init__(self, container_id=None, image=None, image_id=None, last_state=None, name=None, ready=None, restart_count=None, state=None):
        """
        V1ContainerStatus - a model defined in Swagger
        """

        self._container_id = None
        self._image = None
        self._image_id = None
        self._last_state = None
        self._name = None
        self._ready = None
        self._restart_count = None
        self._state = None
        self.discriminator = None

        if container_id is not None:
          self.container_id = container_id
        self.image = image
        self.image_id = image_id
        if last_state is not None:
          self.last_state = last_state
        self.name = name
        self.ready = ready
        self.restart_count = restart_count
        if state is not None:
          self.state = state

    @property
    def container_id(self):
        """
        Gets the container_id of this V1ContainerStatus.
        Container's ID in the format 'docker://<container_id>'.

        :return: The container_id of this V1ContainerStatus.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """
        Sets the container_id of this V1ContainerStatus.
        Container's ID in the format 'docker://<container_id>'.

        :param container_id: The container_id of this V1ContainerStatus.
        :type: str
        """

        self._container_id = container_id

    @property
    def image(self):
        """
        Gets the image of this V1ContainerStatus.
        The image the container is running. More info: https://kubernetes.io/docs/concepts/containers/images

        :return: The image of this V1ContainerStatus.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1ContainerStatus.
        The image the container is running. More info: https://kubernetes.io/docs/concepts/containers/images

        :param image: The image of this V1ContainerStatus.
        :type: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")

        self._image = image

    @property
    def image_id(self):
        """
        Gets the image_id of this V1ContainerStatus.
        ImageID of the container's image.

        :return: The image_id of this V1ContainerStatus.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this V1ContainerStatus.
        ImageID of the container's image.

        :param image_id: The image_id of this V1ContainerStatus.
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")

        self._image_id = image_id

    @property
    def last_state(self):
        """
        Gets the last_state of this V1ContainerStatus.
        Details about the container's last termination condition.

        :return: The last_state of this V1ContainerStatus.
        :rtype: V1ContainerState
        """
        return self._last_state

    @last_state.setter
    def last_state(self, last_state):
        """
        Sets the last_state of this V1ContainerStatus.
        Details about the container's last termination condition.

        :param last_state: The last_state of this V1ContainerStatus.
        :type: V1ContainerState
        """

        self._last_state = last_state

    @property
    def name(self):
        """
        Gets the name of this V1ContainerStatus.
        This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.

        :return: The name of this V1ContainerStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ContainerStatus.
        This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.

        :param name: The name of this V1ContainerStatus.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def ready(self):
        """
        Gets the ready of this V1ContainerStatus.
        Specifies whether the container has passed its readiness probe.

        :return: The ready of this V1ContainerStatus.
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """
        Sets the ready of this V1ContainerStatus.
        Specifies whether the container has passed its readiness probe.

        :param ready: The ready of this V1ContainerStatus.
        :type: bool
        """
        if ready is None:
            raise ValueError("Invalid value for `ready`, must not be `None`")

        self._ready = ready

    @property
    def restart_count(self):
        """
        Gets the restart_count of this V1ContainerStatus.
        The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.

        :return: The restart_count of this V1ContainerStatus.
        :rtype: int
        """
        return self._restart_count

    @restart_count.setter
    def restart_count(self, restart_count):
        """
        Sets the restart_count of this V1ContainerStatus.
        The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.

        :param restart_count: The restart_count of this V1ContainerStatus.
        :type: int
        """
        if restart_count is None:
            raise ValueError("Invalid value for `restart_count`, must not be `None`")

        self._restart_count = restart_count

    @property
    def state(self):
        """
        Gets the state of this V1ContainerStatus.
        Details about the container's current condition.

        :return: The state of this V1ContainerStatus.
        :rtype: V1ContainerState
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this V1ContainerStatus.
        Details about the container's current condition.

        :param state: The state of this V1ContainerStatus.
        :type: V1ContainerState
        """

        self._state = state

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
        if not isinstance(other, V1ContainerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

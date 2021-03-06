# coding: utf-8

"""
    Platform API

    The REST API for Platform.sh.

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RouteRepresentation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, project=None, environment=None, redirects=None, type=None, route=None):
        """
        RouteRepresentation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'project': 'str',
            'environment': 'str',
            'redirects': 'Redirects',
            'type': 'str',
            'route': 'RouteIdentification'
        }

        self.attribute_map = {
            'project': 'project',
            'environment': 'environment',
            'redirects': 'redirects',
            'type': 'type',
            'route': 'route'
        }

        self._project = project
        self._environment = environment
        self._redirects = redirects
        self._type = type
        self._route = route

    @property
    def project(self):
        """
        Gets the project of this RouteRepresentation.

        :return: The project of this RouteRepresentation.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """
        Sets the project of this RouteRepresentation.

        :param project: The project of this RouteRepresentation.
        :type: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")

        self._project = project

    @property
    def environment(self):
        """
        Gets the environment of this RouteRepresentation.

        :return: The environment of this RouteRepresentation.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this RouteRepresentation.

        :param environment: The environment of this RouteRepresentation.
        :type: str
        """
        if environment is None:
            raise ValueError("Invalid value for `environment`, must not be `None`")

        self._environment = environment

    @property
    def redirects(self):
        """
        Gets the redirects of this RouteRepresentation.

        :return: The redirects of this RouteRepresentation.
        :rtype: Redirects
        """
        return self._redirects

    @redirects.setter
    def redirects(self, redirects):
        """
        Sets the redirects of this RouteRepresentation.

        :param redirects: The redirects of this RouteRepresentation.
        :type: Redirects
        """
        if redirects is None:
            raise ValueError("Invalid value for `redirects`, must not be `None`")

        self._redirects = redirects

    @property
    def type(self):
        """
        Gets the type of this RouteRepresentation.

        :return: The type of this RouteRepresentation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RouteRepresentation.

        :param type: The type of this RouteRepresentation.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def route(self):
        """
        Gets the route of this RouteRepresentation.

        :return: The route of this RouteRepresentation.
        :rtype: RouteIdentification
        """
        return self._route

    @route.setter
    def route(self, route):
        """
        Sets the route of this RouteRepresentation.

        :param route: The route of this RouteRepresentation.
        :type: RouteIdentification
        """
        if route is None:
            raise ValueError("Invalid value for `route`, must not be `None`")

        self._route = route

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
        if not isinstance(other, RouteRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

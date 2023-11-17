# coding: utf-8

"""
    FastAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AssistantCreateRequestBodySchema(object):
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
        'model_id': 'object',
        'name': 'object',
        'description': 'object',
        'system_prompt_template': 'object',
        'plugins': 'object',
        'retrievals': 'object',
        'metadata': 'object'
    }

    attribute_map = {
        'model_id': 'model_id',
        'name': 'name',
        'description': 'description',
        'system_prompt_template': 'system_prompt_template',
        'plugins': 'plugins',
        'retrievals': 'retrievals',
        'metadata': 'metadata'
    }

    def __init__(self, model_id=None, name=None, description=None, system_prompt_template=None, plugins=None, retrievals=None, metadata=None):  # noqa: E501
        """AssistantCreateRequestBodySchema - a model defined in Swagger"""  # noqa: E501
        self._model_id = None
        self._name = None
        self._description = None
        self._system_prompt_template = None
        self._plugins = None
        self._retrievals = None
        self._metadata = None
        self.discriminator = None
        self.model_id = model_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if system_prompt_template is not None:
            self.system_prompt_template = system_prompt_template
        if plugins is not None:
            self.plugins = plugins
        if retrievals is not None:
            self.retrievals = retrievals
        if metadata is not None:
            self.metadata = metadata

    @property
    def model_id(self):
        """Gets the model_id of this AssistantCreateRequestBodySchema.  # noqa: E501


        :return: The model_id of this AssistantCreateRequestBodySchema.  # noqa: E501
        :rtype: object
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this AssistantCreateRequestBodySchema.


        :param model_id: The model_id of this AssistantCreateRequestBodySchema.  # noqa: E501
        :type: object
        """
        if model_id is None:
            raise ValueError("Invalid value for `model_id`, must not be `None`")  # noqa: E501

        self._model_id = model_id

    @property
    def name(self):
        """Gets the name of this AssistantCreateRequestBodySchema.  # noqa: E501


        :return: The name of this AssistantCreateRequestBodySchema.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssistantCreateRequestBodySchema.


        :param name: The name of this AssistantCreateRequestBodySchema.  # noqa: E501
        :type: object
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AssistantCreateRequestBodySchema.  # noqa: E501


        :return: The description of this AssistantCreateRequestBodySchema.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssistantCreateRequestBodySchema.


        :param description: The description of this AssistantCreateRequestBodySchema.  # noqa: E501
        :type: object
        """

        self._description = description

    @property
    def system_prompt_template(self):
        """Gets the system_prompt_template of this AssistantCreateRequestBodySchema.  # noqa: E501


        :return: The system_prompt_template of this AssistantCreateRequestBodySchema.  # noqa: E501
        :rtype: object
        """
        return self._system_prompt_template

    @system_prompt_template.setter
    def system_prompt_template(self, system_prompt_template):
        """Sets the system_prompt_template of this AssistantCreateRequestBodySchema.


        :param system_prompt_template: The system_prompt_template of this AssistantCreateRequestBodySchema.  # noqa: E501
        :type: object
        """

        self._system_prompt_template = system_prompt_template

    @property
    def plugins(self):
        """Gets the plugins of this AssistantCreateRequestBodySchema.  # noqa: E501


        :return: The plugins of this AssistantCreateRequestBodySchema.  # noqa: E501
        :rtype: object
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """Sets the plugins of this AssistantCreateRequestBodySchema.


        :param plugins: The plugins of this AssistantCreateRequestBodySchema.  # noqa: E501
        :type: object
        """

        self._plugins = plugins

    @property
    def retrievals(self):
        """Gets the retrievals of this AssistantCreateRequestBodySchema.  # noqa: E501


        :return: The retrievals of this AssistantCreateRequestBodySchema.  # noqa: E501
        :rtype: object
        """
        return self._retrievals

    @retrievals.setter
    def retrievals(self, retrievals):
        """Sets the retrievals of this AssistantCreateRequestBodySchema.


        :param retrievals: The retrievals of this AssistantCreateRequestBodySchema.  # noqa: E501
        :type: object
        """

        self._retrievals = retrievals

    @property
    def metadata(self):
        """Gets the metadata of this AssistantCreateRequestBodySchema.  # noqa: E501


        :return: The metadata of this AssistantCreateRequestBodySchema.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AssistantCreateRequestBodySchema.


        :param metadata: The metadata of this AssistantCreateRequestBodySchema.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

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
        if issubclass(AssistantCreateRequestBodySchema, dict):
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
        if not isinstance(other, AssistantCreateRequestBodySchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

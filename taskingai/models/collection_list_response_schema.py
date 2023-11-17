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

class CollectionListResponseSchema(object):
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
        'status': 'object',
        'fetched_count': 'object',
        'total_count': 'object',
        'has_more': 'object',
        'data': 'object'
    }

    attribute_map = {
        'status': 'status',
        'fetched_count': 'fetched_count',
        'total_count': 'total_count',
        'has_more': 'has_more',
        'data': 'data'
    }

    def __init__(self, status=None, fetched_count=None, total_count=None, has_more=None, data=None):  # noqa: E501
        """CollectionListResponseSchema - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._fetched_count = None
        self._total_count = None
        self._has_more = None
        self._data = None
        self.discriminator = None
        self.status = status
        self.fetched_count = fetched_count
        self.total_count = total_count
        self.has_more = has_more
        self.data = data

    @property
    def status(self):
        """Gets the status of this CollectionListResponseSchema.  # noqa: E501


        :return: The status of this CollectionListResponseSchema.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CollectionListResponseSchema.


        :param status: The status of this CollectionListResponseSchema.  # noqa: E501
        :type: object
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def fetched_count(self):
        """Gets the fetched_count of this CollectionListResponseSchema.  # noqa: E501


        :return: The fetched_count of this CollectionListResponseSchema.  # noqa: E501
        :rtype: object
        """
        return self._fetched_count

    @fetched_count.setter
    def fetched_count(self, fetched_count):
        """Sets the fetched_count of this CollectionListResponseSchema.


        :param fetched_count: The fetched_count of this CollectionListResponseSchema.  # noqa: E501
        :type: object
        """
        if fetched_count is None:
            raise ValueError("Invalid value for `fetched_count`, must not be `None`")  # noqa: E501

        self._fetched_count = fetched_count

    @property
    def total_count(self):
        """Gets the total_count of this CollectionListResponseSchema.  # noqa: E501


        :return: The total_count of this CollectionListResponseSchema.  # noqa: E501
        :rtype: object
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this CollectionListResponseSchema.


        :param total_count: The total_count of this CollectionListResponseSchema.  # noqa: E501
        :type: object
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

    @property
    def has_more(self):
        """Gets the has_more of this CollectionListResponseSchema.  # noqa: E501


        :return: The has_more of this CollectionListResponseSchema.  # noqa: E501
        :rtype: object
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this CollectionListResponseSchema.


        :param has_more: The has_more of this CollectionListResponseSchema.  # noqa: E501
        :type: object
        """
        if has_more is None:
            raise ValueError("Invalid value for `has_more`, must not be `None`")  # noqa: E501

        self._has_more = has_more

    @property
    def data(self):
        """Gets the data of this CollectionListResponseSchema.  # noqa: E501


        :return: The data of this CollectionListResponseSchema.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CollectionListResponseSchema.


        :param data: The data of this CollectionListResponseSchema.  # noqa: E501
        :type: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(CollectionListResponseSchema, dict):
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
        if not isinstance(other, CollectionListResponseSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

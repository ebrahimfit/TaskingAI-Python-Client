# coding: utf-8

"""
    FastAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import taskingai
from taskingai.api.assistant_api import AssistantApi  # noqa: E501
from taskingai.rest import ApiException


class TestAssistantApi(unittest.TestCase):
    """AssistantApi unit test stubs"""

    def setUp(self):
        self.api = AssistantApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_assistant(self):
        """Test case for create_assistant

        Create assistant  # noqa: E501
        """
        pass

    def test_create_chat(self):
        """Test case for create_chat

        Create chat  # noqa: E501
        """
        pass

    def test_delete_assistant(self):
        """Test case for delete_assistant

        Delete assistant  # noqa: E501
        """
        pass

    def test_delete_chat(self):
        """Test case for delete_chat

        Delete chat  # noqa: E501
        """
        pass

    def test_generate(self):
        """Test case for generate

        Generate  # noqa: E501
        """
        pass

    def test_get_assistant(self):
        """Test case for get_assistant

        Get assistant  # noqa: E501
        """
        pass

    def test_get_chat(self):
        """Test case for get_chat

        Get chat  # noqa: E501
        """
        pass

    def test_get_message(self):
        """Test case for get_message

        Get message  # noqa: E501
        """
        pass

    def test_list_assistants(self):
        """Test case for list_assistants

        List assistants  # noqa: E501
        """
        pass

    def test_list_chats(self):
        """Test case for list_chats

        List chats  # noqa: E501
        """
        pass

    def test_list_messages(self):
        """Test case for list_messages

        List messages  # noqa: E501
        """
        pass

    def test_update_assistant(self):
        """Test case for update_assistant

        Update assistant  # noqa: E501
        """
        pass

    def test_update_chat(self):
        """Test case for update_chat

        Update chat  # noqa: E501
        """
        pass

    def test_update_message(self):
        """Test case for update_message

        Update message  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

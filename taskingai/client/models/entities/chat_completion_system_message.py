# -*- coding: utf-8 -*-

# chat_completion_system_message.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional
from .chat_completion_role import ChatCompletionRole

__all__ = ["ChatCompletionSystemMessage"]


class ChatCompletionSystemMessage(BaseModel):
    content: Optional[str] = Field(None)
    role: ChatCompletionRole = Field(...)

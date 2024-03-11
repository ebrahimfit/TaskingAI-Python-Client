# -*- coding: utf-8 -*-

# record_list_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import List
from ..entities.record import Record

__all__ = ["RecordListResponse"]


class RecordListResponse(BaseModel):
    status: str = Field("success")
    data: List[Record] = Field(...)
    fetched_count: int = Field(...)
    has_more: bool = Field(...)

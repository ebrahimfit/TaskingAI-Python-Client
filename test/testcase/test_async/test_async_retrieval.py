import pytest
import os
import asyncio
from taskingai.retrieval import *
from taskingai.file import a_upload_file
from taskingai.client.models import UploadFilePurpose
from test.config import Config
from test.common.logger import logger
from test.testcase.test_async import Base
from test.common.utils import (
    assume_collection_result,
    assume_record_result,
    assume_chunk_result,
    assume_query_chunk_result,
)


@pytest.mark.test_async
class TestCollection(Base):
    @pytest.mark.run(order=21)
    @pytest.mark.asyncio
    async def test_a_create_collection(self):
        # Create a collection.

        create_list = [
            {
                "capacity": 1000,
                "embedding_model_id": Config.openai_text_embedding_model_id,
                "name": "test",
                "description": "description",
                "metadata": {"key1": "value1", "key2": "value2"},
            },
            {
                "capacity": 1000,
                "embedding_model_id": Config.openai_text_embedding_model_id,
                "type": "qa",
                "name": "test",
                "description": "description",
                "metadata": {"key1": "value1", "key2": "value2"},
            },

        ]
        for index, create_dict in enumerate(create_list):
            res = await a_create_collection(**create_dict)
            res_dict = vars(res)
            logger.info(res_dict)
            assume_collection_result(create_dict, res_dict)
            if index == 0:
                Base.collection_id = res_dict["collection_id"]
            else:
                Base.qa_collection_id = res_dict["collection_id"]

    @pytest.mark.run(order=22)
    @pytest.mark.asyncio
    async def test_a_list_collections(self):
        # List collections.

        nums_limit = 1
        res = await a_list_collections(limit=nums_limit)
        pytest.assume(len(res) == nums_limit)
        after_id = res[-1].collection_id
        after_res = await a_list_collections(limit=nums_limit, after=after_id)
        pytest.assume(len(after_res) == nums_limit)
        twice_nums_list = await a_list_collections(limit=nums_limit * 2)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])
        before_id = after_res[0].collection_id
        before_res = await a_list_collections(limit=nums_limit, before=before_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=23)
    @pytest.mark.asyncio
    async def test_a_get_collection(self):
        # Get a collection.
        res = await a_get_collection(collection_id=self.collection_id)
        res_dict = vars(res)
        pytest.assume(res_dict["status"] == "ready")
        pytest.assume(res_dict["collection_id"] == self.collection_id)

    @pytest.mark.run(order=24)
    @pytest.mark.asyncio
    async def test_a_update_collection(self):
        # Update a collection.

        update_collection_data = {
            "collection_id": self.collection_id,
            "name": "test_update",
            "description": "description_update",
            "metadata": {"key1": "value1", "key2": "value2"},
        }
        res = await a_update_collection(**update_collection_data)
        res_dict = vars(res)
        assume_collection_result(update_collection_data, res_dict)

    @pytest.mark.run(order=80)
    @pytest.mark.asyncio
    async def test_a_delete_collection(self):
        # List collections.
        old_res = await a_list_collections(order="desc", limit=100, after=None, before=None)
        old_nums = len(old_res)
        for index, collection in enumerate(old_res):
            collection_id = collection.collection_id
            # Delete a collection.
            await a_delete_collection(collection_id=collection_id)
            if index == old_nums - 1:
                new_collections = await a_list_collections(order="desc", limit=100, after=None, before=None)
                # List collections.
                new_nums = len(new_collections)
                pytest.assume(new_nums == 0)


@pytest.mark.test_async
class TestRecord(Base):
    text_splitter_list = [
        # {"type": "token", "chunk_size": 100, "chunk_overlap": 10},
        # TokenTextSplitter(chunk_size=200, chunk_overlap=20),
        {"type": "separator", "chunk_size": 100, "chunk_overlap": 10, "separators": [".", "!", "?"]},
        TextSplitter(type="separator", chunk_size=200, chunk_overlap=20, separators=[".", "!", "?"]),
    ]

    upload_file_data_list = []
    upload_qa_file_data_list = []
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    files = os.listdir(base_path + "/files")
    for file in files:
        filepath = os.path.join(base_path, "files", file)
        if os.path.isfile(filepath):
            upload_file_dict = {"purpose": UploadFilePurpose.RECORD_FILE}
            upload_file_dict.update({"file": open(filepath, "rb")})
            upload_file_data_list.append(upload_file_dict)

    qa_files = os.listdir(base_path + "/qa_files")
    for file in qa_files:
        filepath = os.path.join(base_path, "qa_files", file)
        if os.path.isfile(filepath):
            upload_qa_file_dict = {"purpose": "qa_record_file"}
            upload_qa_file_dict.update({"file": open(filepath, "rb")})
            upload_qa_file_data_list.append(upload_qa_file_dict)

    @pytest.mark.run(order=31)
    @pytest.mark.asyncio
    @pytest.mark.parametrize("text_splitter", text_splitter_list)
    async def test_a_create_record_by_text(self, text_splitter):
        text = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        create_record_data = {
            "type": "text",
            "title": "Machine learning",
            "collection_id": self.collection_id,
            "content": text,
            "text_splitter": text_splitter,
            "metadata": {"key1": "value1", "key2": "value2"},
        }
        res = await a_create_record(**create_record_data)
        res_dict = vars(res)
        assume_record_result(create_record_data, res_dict)
        Base.record_id = res_dict["record_id"]

    @pytest.mark.run(order=31)
    @pytest.mark.asyncio
    async def test_a_create_record_by_web(self):
        text_splitter = TokenTextSplitter(chunk_size=200, chunk_overlap=100)
        create_record_data = {
            "type": "web",
            "title": "Machine learning",
            "collection_id": self.collection_id,
            "url": "https://docs.tasking.ai/docs/guide/getting_started/overview/",
            "text_splitter": text_splitter,
            "metadata": {"key1": "value1", "key2": "value2"},
        }

        res = await a_create_record(**create_record_data)
        res_dict = vars(res)
        assume_record_result(create_record_data, res_dict)

    @pytest.mark.run(order=31)
    @pytest.mark.asyncio
    @pytest.mark.parametrize("upload_file_data", upload_file_data_list[:2])
    async def test_a_create_record_by_file(self, upload_file_data):
        upload_file_res = await a_upload_file(**upload_file_data)
        upload_file_dict = vars(upload_file_res)
        file_id = upload_file_dict["file_id"]
        pytest.assume(file_id is not None)

        text_splitter = TokenTextSplitter(chunk_size=200, chunk_overlap=100)
        create_record_data = {
            "type": "file",
            "title": "Machine learning",
            "collection_id": self.collection_id,
            "file_id": file_id,
            "text_splitter": text_splitter,
            "metadata": {"key1": "value1", "key2": "value2"},
        }

        res = await a_create_record(**create_record_data)
        res_dict = vars(res)
        assume_record_result(create_record_data, res_dict)

    @pytest.mark.run(order=32)
    @pytest.mark.asyncio
    @pytest.mark.parametrize("upload_qa_file_data", upload_qa_file_data_list)
    async def test_create_record_by_qa_file(self, upload_qa_file_data):
        # upload file
        upload_file_res = await a_upload_file(**upload_qa_file_data)
        upload_file_dict = vars(upload_file_res)
        file_id = upload_file_dict["file_id"]
        pytest.assume(file_id is not None)

        text_splitter = TokenTextSplitter(chunk_size=200, chunk_overlap=20)
        create_record_data = {
            "type": "qa_sheet",
            "collection_id": self.qa_collection_id,
            "file_id": file_id,
            "metadata": {"key1": "value1", "key2": "value2"},
        }

        res = create_record(**create_record_data)
        res_dict = vars(res)
        assume_record_result(create_record_data, res_dict)
        Base.qa_record_id = res_dict["record_id"]

    @pytest.mark.run(order=32)
    @pytest.mark.asyncio
    async def test_a_list_records(self):
        # List records.

        nums_limit = 1
        res = await a_list_records(limit=nums_limit, collection_id=self.collection_id)
        pytest.assume(len(res) == nums_limit)

        after_id = res[-1].record_id
        after_res = await a_list_records(limit=nums_limit, after=after_id, collection_id=self.collection_id)
        pytest.assume(len(after_res) == nums_limit)

        twice_nums_list = await a_list_records(limit=nums_limit * 2, collection_id=self.collection_id)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])

        before_id = after_res[0].record_id
        before_res = await a_list_records(limit=nums_limit, before=before_id, collection_id=self.collection_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

        @pytest.mark.run(order=32)
        @pytest.mark.asyncio
        async def test_a_list_qa_records(self):
            # List records.

            nums_limit = 1
            res = await a_list_records(limit=nums_limit, collection_id=self.qa_collection_id)
            pytest.assume(len(res) == nums_limit)

            after_id = res[-1].record_id
            after_res = await a_list_records(limit=nums_limit, after=after_id, collection_id=self.qa_collection_id)
            pytest.assume(len(after_res) == nums_limit)

            twice_nums_list = await a_list_records(limit=nums_limit * 2, collection_id=self.qa_collection_id)
            pytest.assume(len(twice_nums_list) == nums_limit * 2)
            pytest.assume(after_res[-1] == twice_nums_list[-1])
            pytest.assume(after_res[0] == twice_nums_list[nums_limit])

            before_id = after_res[0].record_id
            before_res = await a_list_records(limit=nums_limit, before=before_id, collection_id=self.qa_collection_id)
            pytest.assume(len(before_res) == nums_limit)
            pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
            pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=33)
    @pytest.mark.asyncio
    async def test_a_get_record(self):
        # Get a record.
        await asyncio.sleep(Config.sleep_time)
        res = await a_get_record(collection_id=self.collection_id, record_id=self.record_id)
        logger.info(f"a_get_record:{res}")
        res_dict = vars(res)
        pytest.assume(res_dict["collection_id"] == self.collection_id)
        pytest.assume(res_dict["record_id"] == self.record_id)
        pytest.assume(res_dict["status"] == "ready")

    @pytest.mark.run(order=33)
    @pytest.mark.asyncio
    async def test_a_get_qa_record(self):
        # Get a record.
        await asyncio.sleep(Config.sleep_time)
        res = await a_get_record(collection_id=self.qa_collection_id, record_id=self.qa_record_id)
        logger.info(f"a_get_record:{res}")
        res_dict = vars(res)
        pytest.assume(res_dict["collection_id"] == self.qa_collection_id)
        pytest.assume(res_dict["record_id"] == self.qa_record_id)
        pytest.assume(res_dict["status"] == "ready")

    @pytest.mark.run(order=34)
    @pytest.mark.asyncio
    @pytest.mark.parametrize("text_splitter", text_splitter_list)
    async def test_a_update_record_by_text(self, text_splitter):
        # Update a record.
        await asyncio.sleep(Config.sleep_time)
        update_record_data = {
            "collection_id": self.collection_id,
            "record_id": self.record_id,
            "content": "TaskingAI is an AI-native application development platform that unifies modules like Model, Retrieval, Assistant, and Tool into one seamless ecosystem, streamlining the creation and deployment of applications for developers.",
            "text_splitter": text_splitter,
            "metadata": {"test": "test"},
        }
        res = await a_update_record(**update_record_data)
        logger.info(f"a_update_record:{res}")
        res_dict = vars(res)
        assume_record_result(update_record_data, res_dict)

    @pytest.mark.run(order=34)
    @pytest.mark.asyncio
    @pytest.mark.parametrize("text_splitter", text_splitter_list)
    async def test_a_update_record_by_web(self, text_splitter):
        # Update a record.
        await asyncio.sleep(Config.sleep_time)
        update_record_data = {
            "type": "web",
            "title": "Machine learning",
            "collection_id": self.collection_id,
            "record_id": self.record_id,
            "url": "https://docs.tasking.ai/docs/guide/getting_started/overview/",
            "text_splitter": text_splitter,
            "metadata": {"test": "test"},
        }
        res = await a_update_record(**update_record_data)
        logger.info(f"a_update_record:{res}")
        res_dict = vars(res)
        assume_record_result(update_record_data, res_dict)

    @pytest.mark.run(order=34)
    @pytest.mark.asyncio
    @pytest.mark.parametrize("upload_file_data", upload_file_data_list[2:3])
    async def test_a_update_record_by_file(self, upload_file_data):
        # upload file
        await asyncio.sleep(Config.sleep_time)
        upload_file_res = await a_upload_file(**upload_file_data)
        upload_file_dict = vars(upload_file_res)
        file_id = upload_file_dict["file_id"]
        pytest.assume(file_id is not None)

        # Update a record.

        update_record_data = {
            "type": "file",
            "title": "Machine learning",
            "collection_id": self.collection_id,
            "record_id": self.record_id,
            "file_id": file_id,
            "text_splitter": TokenTextSplitter(chunk_size=200, chunk_overlap=100),
            "metadata": {"test": "test"},
        }
        res = await a_update_record(**update_record_data)
        logger.info(f"a_update_record:{res}")
        res_dict = vars(res)
        assume_record_result(update_record_data, res_dict)

    @pytest.mark.run(order=34)
    @pytest.mark.asyncio
    @pytest.mark.parametrize("upload_qa_file_data", upload_qa_file_data_list)
    async def test_a_update_qa_record(self, upload_qa_file_data):
        # upload file
        await asyncio.sleep(Config.sleep_time)
        upload_file_res = await a_upload_file(**upload_qa_file_data)
        upload_file_dict = vars(upload_file_res)
        file_id = upload_file_dict["file_id"]
        pytest.assume(file_id is not None)

        # Update a record.

        update_record_data = {
            "type": "qa_sheet",
            "collection_id": self.qa_collection_id,
            "record_id": self.qa_record_id,
            "file_id": file_id,
            "metadata": {"test": "test"},
        }
        res = await a_update_record(**update_record_data)
        logger.info(f"a_update_record:{res}")
        res_dict = vars(res)
        # assume_record_result(update_record_data, res_dict)

    @pytest.mark.run(order=79)
    @pytest.mark.asyncio
    async def test_a_delete_record(self):
        # List records.

        records = await a_list_records(
            collection_id=self.collection_id, order="desc", limit=20, after=None, before=None
        )
        old_nums = len(records)
        for index, record in enumerate(records):
            record_id = record.record_id

            # Delete a record.

            await a_delete_record(collection_id=self.collection_id, record_id=record_id)

            # List records.
            if index == old_nums - 1:
                new_records = await a_list_records(
                    collection_id=self.collection_id, order="desc", limit=20, after=None, before=None
                )
                record_ids = [record.record_id for record in new_records]
                pytest.assume(record_id not in record_ids)
                new_nums = len(new_records)
                pytest.assume(new_nums == 0)

    @pytest.mark.run(order=79)
    @pytest.mark.asyncio
    async def test_a_delete_qa_record(self):
        # List records.

        records = await a_list_records(
            collection_id=self.qa_collection_id, order="desc", limit=20, after=None, before=None
        )
        old_nums = len(records)
        for index, record in enumerate(records):
            record_id = record.record_id

            # Delete a record.

            await a_delete_record(collection_id=self.qa_collection_id, record_id=record_id)

            # List records.
            if index == old_nums - 1:
                new_records = await a_list_records(
                    collection_id=self.qa_collection_id, order="desc", limit=20, after=None, before=None
                )
                record_ids = [record.record_id for record in new_records]
                pytest.assume(record_id not in record_ids)
                new_nums = len(new_records)
                pytest.assume(new_nums == 0)


@pytest.mark.test_async
class TestChunk(Base):

    @pytest.mark.run(order=41)
    @pytest.mark.asyncio
    async def test_a_query_chunks(self):
        # Query chunks.

        query_text = "Machine learning"
        top_k = 1
        res = await a_query_chunks(
            collection_id=self.collection_id, query_text=query_text, top_k=top_k, max_tokens=20000, score_threshold=0.04
        )
        pytest.assume(len(res) == top_k)
        for chunk in res:
            chunk_dict = vars(chunk)
            assume_query_chunk_result(query_text, chunk_dict)
            pytest.assume(chunk_dict["score"] >= 0.04)

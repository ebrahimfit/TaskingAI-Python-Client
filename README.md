# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:

```python
import taskingai 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import taskingai
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
body = taskingai.AssistantCreateRequestBodySchema()  # AssistantCreateRequestBodySchema | 

try:
    # Create assistant
    api_response = api_instance.create_assistant(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->create_assistant: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
body = taskingai.ChatCreateRequestBodySchema()  # ChatCreateRequestBodySchema | 
assistant_id = NULL  # object | 

try:
    # Create chat
    api_response = api_instance.create_chat(body, assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->create_chat: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
assistant_id = NULL  # object | 

try:
    # Delete assistant
    api_response = api_instance.delete_assistant(assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->delete_assistant: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
assistant_id = NULL  # object | 
chat_id = NULL  # object | 

try:
    # Delete chat
    api_response = api_instance.delete_chat(assistant_id, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->delete_chat: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
body = taskingai.ChatGenerateRequestBodySchema()  # ChatGenerateRequestBodySchema | 
assistant_id = NULL  # object | 
chat_id = NULL  # object | 

try:
    # Generate
    api_response = api_instance.generate(body, assistant_id, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->generate: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
assistant_id = NULL  # object | 

try:
    # Get assistant
    api_response = api_instance.get_assistant(assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->get_assistant: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
assistant_id = NULL  # object | 
chat_id = NULL  # object | 

try:
    # Get chat
    api_response = api_instance.get_chat(assistant_id, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->get_chat: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
assistant_id = NULL  # object | 
chat_id = NULL  # object | 
message_id = NULL  # object | 

try:
    # Get message
    api_response = api_instance.get_message(assistant_id, chat_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->get_message: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
limit = 20  # object |  (optional) (default to 20)
order = desc  # object |  (optional) (default to desc)
after = NULL  # object |  (optional)
before = NULL  # object |  (optional)
offset = NULL  # object |  (optional)

try:
    # List assistants
    api_response = api_instance.list_assistants(limit=limit, order=order, after=after, before=before, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->list_assistants: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
assistant_id = NULL  # object | 

try:
    # List chats
    api_response = api_instance.list_chats(assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->list_chats: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
assistant_id = NULL  # object | 
chat_id = NULL  # object | 
limit = 20  # object |  (optional) (default to 20)
order = desc  # object |  (optional) (default to desc)
after = NULL  # object |  (optional)
before = NULL  # object |  (optional)

try:
    # List messages
    api_response = api_instance.list_messages(assistant_id, chat_id, limit=limit, order=order, after=after,
                                              before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->list_messages: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
body = taskingai.AssistantUpdateRequestBodySchema()  # AssistantUpdateRequestBodySchema | 
assistant_id = NULL  # object | 

try:
    # Update assistant
    api_response = api_instance.update_assistant(body, assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->update_assistant: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
body = taskingai.ChatUpdateRequestBodySchema()  # ChatUpdateRequestBodySchema | 
assistant_id = NULL  # object | 
chat_id = NULL  # object | 

try:
    # Update chat
    api_response = api_instance.update_chat(body, assistant_id, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->update_chat: %s\n" % e)

# create an instance of the API class
api_instance = taskingai.AssistantApi(taskingai.ApiClient(configuration))
body = taskingai.MessageUpdateRequestBodySchema()  # MessageUpdateRequestBodySchema | 
assistant_id = NULL  # object | 
chat_id = NULL  # object | 
message_id = NULL  # object | 

try:
    # Update message
    api_response = api_instance.update_message(body, assistant_id, chat_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->update_message: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AssistantApi* | [**create_assistant**](docs/AssistantApi.md#create_assistant) | **POST** /api/v1/assistants | Create assistant
*AssistantApi* | [**create_chat**](docs/AssistantApi.md#create_chat) | **POST** /api/v1/assistants/{assistant_id}/chats | Create chat
*AssistantApi* | [**delete_assistant**](docs/AssistantApi.md#delete_assistant) | **DELETE** /api/v1/assistants/{assistant_id} | Delete assistant
*AssistantApi* | [**delete_chat**](docs/AssistantApi.md#delete_chat) | **DELETE** /api/v1/assistants/{assistant_id}/chats/{chat_id} | Delete chat
*AssistantApi* | [**generate**](docs/AssistantApi.md#generate) | **POST** /api/v1/assistants/{assistant_id}/chats/{chat_id}/generate | Generate
*AssistantApi* | [**get_assistant**](docs/AssistantApi.md#get_assistant) | **GET** /api/v1/assistants/{assistant_id} | Get assistant
*AssistantApi* | [**get_chat**](docs/AssistantApi.md#get_chat) | **GET** /api/v1/assistants/{assistant_id}/chats/{chat_id} | Get chat
*AssistantApi* | [**get_message**](docs/AssistantApi.md#get_message) | **GET** /api/v1/assistants/{assistant_id}/chats/{chat_id}/messages/{message_id} | Get message
*AssistantApi* | [**list_assistants**](docs/AssistantApi.md#list_assistants) | **GET** /api/v1/assistants | List assistants
*AssistantApi* | [**list_chats**](docs/AssistantApi.md#list_chats) | **GET** /api/v1/assistants/{assistant_id}/chats | List chats
*AssistantApi* | [**list_messages**](docs/AssistantApi.md#list_messages) | **GET** /api/v1/assistants/{assistant_id}/chats/{chat_id}/messages | List messages
*AssistantApi* | [**update_assistant**](docs/AssistantApi.md#update_assistant) | **POST** /api/v1/assistants/{assistant_id} | Update assistant
*AssistantApi* | [**update_chat**](docs/AssistantApi.md#update_chat) | **POST** /api/v1/assistants/{assistant_id}/chats/{chat_id} | Update chat
*AssistantApi* | [**update_message**](docs/AssistantApi.md#update_message) | **POST** /api/v1/assistants/{assistant_id}/chats/{chat_id}/messages/{message_id} | Update message
*RetrievalApi* | [**create_collection**](docs/RetrievalApi.md#create_collection) | **POST** /api/v1/collections | Create collection
*RetrievalApi* | [**create_record**](docs/RetrievalApi.md#create_record) | **POST** /api/v1/collections/{collection_id}/records | Create record
*RetrievalApi* | [**delete_collection**](docs/RetrievalApi.md#delete_collection) | **DELETE** /api/v1/collections/{collection_id} | Delete collection
*RetrievalApi* | [**delete_record**](docs/RetrievalApi.md#delete_record) | **DELETE** /api/v1/collections/{collection_id}/records/{record_id} | Delete record
*RetrievalApi* | [**get_collection**](docs/RetrievalApi.md#get_collection) | **GET** /api/v1/collections/{collection_id} | Get collection
*RetrievalApi* | [**get_record**](docs/RetrievalApi.md#get_record) | **GET** /api/v1/collections/{collection_id}/records/{record_id} | Get record
*RetrievalApi* | [**list_collections**](docs/RetrievalApi.md#list_collections) | **GET** /api/v1/collections | List collections
*RetrievalApi* | [**list_records**](docs/RetrievalApi.md#list_records) | **GET** /api/v1/collections/{collection_id}/records | List records
*RetrievalApi* | [**query_chunks**](docs/RetrievalApi.md#query_chunks) | **POST** /api/v1/collections/{collection_id}/chunks/params | Query chunks
*RetrievalApi* | [**update_collection**](docs/RetrievalApi.md#update_collection) | **POST** /api/v1/collections/{collection_id} | Update collection
*RetrievalApi* | [**update_record**](docs/RetrievalApi.md#update_record) | **POST** /api/v1/collections/{collection_id}/records/{record_id} | Update record

## Documentation For Models

 - [Assistant](docs/Assistant.md)
 - [AssistantCreateRequestBodySchema](docs/AssistantCreateRequestBodySchema.md)
 - [AssistantCreateResponseSchema](docs/AssistantCreateResponseSchema.md)
 - [AssistantGetResponseSchema](docs/AssistantGetResponseSchema.md)
 - [AssistantListResponseSchema](docs/AssistantListResponseSchema.md)
 - [AssistantUpdateRequestBodySchema](docs/AssistantUpdateRequestBodySchema.md)
 - [AssistantUpdateResponseSchema](docs/AssistantUpdateResponseSchema.md)
 - [BaseSuccessEmptyOutSchema](docs/BaseSuccessEmptyOutSchema.md)
 - [Chat](docs/Chat.md)
 - [ChatCreateRequestBodySchema](docs/ChatCreateRequestBodySchema.md)
 - [ChatCreateResponseSchema](docs/ChatCreateResponseSchema.md)
 - [ChatGenerateRequestBodySchema](docs/ChatGenerateRequestBodySchema.md)
 - [ChatGenerateResponseSchema](docs/ChatGenerateResponseSchema.md)
 - [ChatGenerateUserMessage](docs/ChatGenerateUserMessage.md)
 - [ChatGetResponseSchema](docs/ChatGetResponseSchema.md)
 - [ChatListResponseSchema](docs/ChatListResponseSchema.md)
 - [ChatUpdateRequestBodySchema](docs/ChatUpdateRequestBodySchema.md)
 - [ChatUpdateResponseSchema](docs/ChatUpdateResponseSchema.md)
 - [Chunk](docs/Chunk.md)
 - [ChunkQueryRequestBodySchema](docs/ChunkQueryRequestBodySchema.md)
 - [ChunkQueryResponseSchema](docs/ChunkQueryResponseSchema.md)
 - [Collection](docs/Collection.md)
 - [CollectionCreateRequestBodySchema](docs/CollectionCreateRequestBodySchema.md)
 - [CollectionCreateResponseSchema](docs/CollectionCreateResponseSchema.md)
 - [CollectionGetResponseSchema](docs/CollectionGetResponseSchema.md)
 - [CollectionListResponseSchema](docs/CollectionListResponseSchema.md)
 - [CollectionUpdateRequestBodySchema](docs/CollectionUpdateRequestBodySchema.md)
 - [CollectionUpdateResponseSchema](docs/CollectionUpdateResponseSchema.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Message](docs/Message.md)
 - [MessageContent](docs/MessageContent.md)
 - [MessageGetResponseSchema](docs/MessageGetResponseSchema.md)
 - [MessageListResponseSchema](docs/MessageListResponseSchema.md)
 - [MessageUpdateRequestBodySchema](docs/MessageUpdateRequestBodySchema.md)
 - [MessageUpdateResponseSchema](docs/MessageUpdateResponseSchema.md)
 - [Record](docs/Record.md)
 - [RecordCreateRequestBodySchema](docs/RecordCreateRequestBodySchema.md)
 - [RecordCreateResponseSchema](docs/RecordCreateResponseSchema.md)
 - [RecordGetResponseSchema](docs/RecordGetResponseSchema.md)
 - [RecordListResponseSchema](docs/RecordListResponseSchema.md)
 - [RecordUpdateRequestBodySchema](docs/RecordUpdateRequestBodySchema.md)
 - [RecordUpdateResponseSchema](docs/RecordUpdateResponseSchema.md)
 - [ValidationError](docs/ValidationError.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author



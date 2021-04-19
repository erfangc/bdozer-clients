# openapi_client.TagControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tag**](TagControllerApi.md#delete_tag) | **DELETE** /api/tags/{id} | 
[**find_tag**](TagControllerApi.md#find_tag) | **GET** /api/tags | 
[**save_tag**](TagControllerApi.md#save_tag) | **POST** /api/tags | 


# **delete_tag**
> delete_tag(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import tag_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_controller_api.TagControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_tag(id)
    except openapi_client.ApiException as e:
        print("Exception when calling TagControllerApi->delete_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tag**
> [Tag] find_tag(term)



### Example

```python
import time
import openapi_client
from openapi_client.api import tag_controller_api
from openapi_client.model.tag import Tag
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_controller_api.TagControllerApi(api_client)
    term = "term_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.find_tag(term)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TagControllerApi->find_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  |

### Return type

[**[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_tag**
> save_tag(tag)



### Example

```python
import time
import openapi_client
from openapi_client.api import tag_controller_api
from openapi_client.model.tag import Tag
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tag_controller_api.TagControllerApi(api_client)
    tag = Tag(
        get_id="get_id_example",
        description="description_example",
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.save_tag(tag)
    except openapi_client.ApiException as e:
        print("Exception when calling TagControllerApi->save_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**Tag**](Tag.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


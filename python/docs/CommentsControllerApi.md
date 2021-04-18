# openapi_client.CommentsControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_comments**](CommentsControllerApi.md#get_comments) | **GET** /public/comments/{stockAnalysisId} | 
[**post_comment**](CommentsControllerApi.md#post_comment) | **POST** /public/comments | 


# **get_comments**
> [Comment] get_comments(stock_analysis_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import comments_controller_api
from openapi_client.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = comments_controller_api.CommentsControllerApi(api_client)
    stock_analysis_id = "stockAnalysisId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_comments(stock_analysis_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CommentsControllerApi->get_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_analysis_id** | **str**|  |

### Return type

[**[Comment]**](Comment.md)

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

# **post_comment**
> post_comment(comment)



### Example

```python
import time
import openapi_client
from openapi_client.api import comments_controller_api
from openapi_client.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = comments_controller_api.CommentsControllerApi(api_client)
    comment = Comment(
        get_id="get_id_example",
        stock_analysis_id="stock_analysis_id_example",
        text="text_example",
        last_updated=dateutil_parser('1970-01-01T00:00:00.00Z'),
        user_id="user_id_example",
        name="name_example",
    ) # Comment | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.post_comment(comment)
    except openapi_client.ApiException as e:
        print("Exception when calling CommentsControllerApi->post_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment** | [**Comment**](Comment.md)|  |

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


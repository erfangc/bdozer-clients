# openapi_client.EdgarExplorerControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_entities**](EdgarExplorerControllerApi.md#search_entities) | **GET** /public/edgar-explorer/entities | 
[**search_filings**](EdgarExplorerControllerApi.md#search_filings) | **GET** /public/edgar-explorer/filings | 


# **search_entities**
> [EdgarEntity] search_entities(term)



### Example

```python
import time
import openapi_client
from openapi_client.api import edgar_explorer_controller_api
from openapi_client.model.edgar_entity import EdgarEntity
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = edgar_explorer_controller_api.EdgarExplorerControllerApi(api_client)
    term = "term_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_entities(term)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EdgarExplorerControllerApi->search_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  |

### Return type

[**[EdgarEntity]**](EdgarEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_filings**
> [EdgarFilingMetadata] search_filings(cik)



### Example

```python
import time
import openapi_client
from openapi_client.api import edgar_explorer_controller_api
from openapi_client.model.edgar_filing_metadata import EdgarFilingMetadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = edgar_explorer_controller_api.EdgarExplorerControllerApi(api_client)
    cik = "cik_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_filings(cik)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EdgarExplorerControllerApi->search_filings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik** | **str**|  |

### Return type

[**[EdgarFilingMetadata]**](EdgarFilingMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


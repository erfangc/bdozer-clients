# openapi_client.FactBaseControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_filing**](FactBaseControllerApi.md#ingest_filing) | **POST** /api/fact-base/filing-ingestor | 
[**ingest_q4_facts**](FactBaseControllerApi.md#ingest_q4_facts) | **POST** /api/fact-base/filing-ingestor/q4 | 
[**latest**](FactBaseControllerApi.md#latest) | **POST** /api/fact-base/latest | 


# **ingest_filing**
> ingest_filing(cik, adsh)



### Example

```python
import time
import openapi_client
from openapi_client.api import fact_base_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fact_base_controller_api.FactBaseControllerApi(api_client)
    cik = "cik_example" # str | 
    adsh = "adsh_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.ingest_filing(cik, adsh)
    except openapi_client.ApiException as e:
        print("Exception when calling FactBaseControllerApi->ingest_filing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik** | **str**|  |
 **adsh** | **str**|  |

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

# **ingest_q4_facts**
> ingest_q4_facts(cik, year)



### Example

```python
import time
import openapi_client
from openapi_client.api import fact_base_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fact_base_controller_api.FactBaseControllerApi(api_client)
    cik = "cik_example" # str | 
    year = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.ingest_q4_facts(cik, year)
    except openapi_client.ApiException as e:
        print("Exception when calling FactBaseControllerApi->ingest_q4_facts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik** | **str**|  |
 **year** | **int**|  |

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

# **latest**
> latest()



### Example

```python
import time
import openapi_client
from openapi_client.api import fact_base_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fact_base_controller_api.FactBaseControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.latest()
    except openapi_client.ApiException as e:
        print("Exception when calling FactBaseControllerApi->latest: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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


# openapi_client.FactBaseUnsecuredControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_annual_time_series**](FactBaseUnsecuredControllerApi.md#get_annual_time_series) | **GET** /public/fact-base/{factId}/time-series | 
[**get_annual_time_series1**](FactBaseUnsecuredControllerApi.md#get_annual_time_series1) | **GET** /public/fact-base/time-series | 
[**get_fact**](FactBaseUnsecuredControllerApi.md#get_fact) | **GET** /public/fact-base/{factId} | 


# **get_annual_time_series**
> [Fact] get_annual_time_series(fact_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import fact_base_unsecured_controller_api
from openapi_client.model.fact import Fact
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fact_base_unsecured_controller_api.FactBaseUnsecuredControllerApi(api_client)
    fact_id = "factId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_annual_time_series(fact_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FactBaseUnsecuredControllerApi->get_annual_time_series: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fact_id** | **str**|  |

### Return type

[**[Fact]**](Fact.md)

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

# **get_annual_time_series1**
> [AggregatedFact] get_annual_time_series1(fact_ids)



### Example

```python
import time
import openapi_client
from openapi_client.api import fact_base_unsecured_controller_api
from openapi_client.model.aggregated_fact import AggregatedFact
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fact_base_unsecured_controller_api.FactBaseUnsecuredControllerApi(api_client)
    fact_ids = [
        "factIds_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_annual_time_series1(fact_ids)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FactBaseUnsecuredControllerApi->get_annual_time_series1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fact_ids** | **[str]**|  |

### Return type

[**[AggregatedFact]**](AggregatedFact.md)

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

# **get_fact**
> Fact get_fact(fact_id)



### Example

```python
import time
import openapi_client
from openapi_client.api import fact_base_unsecured_controller_api
from openapi_client.model.fact import Fact
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fact_base_unsecured_controller_api.FactBaseUnsecuredControllerApi(api_client)
    fact_id = "factId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fact(fact_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FactBaseUnsecuredControllerApi->get_fact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fact_id** | **str**|  |

### Return type

[**Fact**](Fact.md)

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


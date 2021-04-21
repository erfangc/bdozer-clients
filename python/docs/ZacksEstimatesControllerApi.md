# openapi_client.ZacksEstimatesControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revenue_projections**](ZacksEstimatesControllerApi.md#revenue_projections) | **GET** /api/zacks-estimates/revenue-projections | 


# **revenue_projections**
> Discrete revenue_projections(ticker)



### Example

```python
import time
import openapi_client
from openapi_client.api import zacks_estimates_controller_api
from openapi_client.model.discrete import Discrete
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = zacks_estimates_controller_api.ZacksEstimatesControllerApi(api_client)
    ticker = "ticker_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.revenue_projections(ticker)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZacksEstimatesControllerApi->revenue_projections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  |

### Return type

[**Discrete**](Discrete.md)

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


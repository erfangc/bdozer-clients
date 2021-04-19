# openapi_client.ModelBuilderFactoryControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**best_effort_model**](ModelBuilderFactoryControllerApi.md#best_effort_model) | **GET** /api/sec/model-builder-factory | 


# **best_effort_model**
> Model best_effort_model(cik, adsh)



### Example

```python
import time
import openapi_client
from openapi_client.api import model_builder_factory_controller_api
from openapi_client.model.model import Model
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = model_builder_factory_controller_api.ModelBuilderFactoryControllerApi(api_client)
    cik = "cik_example" # str | 
    adsh = "adsh_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.best_effort_model(cik, adsh)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModelBuilderFactoryControllerApi->best_effort_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik** | **str**|  |
 **adsh** | **str**|  |

### Return type

[**Model**](Model.md)

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


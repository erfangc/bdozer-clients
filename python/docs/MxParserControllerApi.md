# openapi_client.MxParserControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate1**](MxParserControllerApi.md#evaluate1) | **POST** /api/mxparser | 


# **evaluate1**
> MxParserEvaluateResponse evaluate1(mx_parser_evaluate_request)



### Example

```python
import time
import openapi_client
from openapi_client.api import mx_parser_controller_api
from openapi_client.model.mx_parser_evaluate_request import MxParserEvaluateRequest
from openapi_client.model.mx_parser_evaluate_response import MxParserEvaluateResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mx_parser_controller_api.MxParserControllerApi(api_client)
    mx_parser_evaluate_request = MxParserEvaluateRequest(
        formula="formula_example",
    ) # MxParserEvaluateRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.evaluate1(mx_parser_evaluate_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MxParserControllerApi->evaluate1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mx_parser_evaluate_request** | [**MxParserEvaluateRequest**](MxParserEvaluateRequest.md)|  |

### Return type

[**MxParserEvaluateResponse**](MxParserEvaluateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


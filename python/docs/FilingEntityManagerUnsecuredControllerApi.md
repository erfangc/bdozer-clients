# openapi_client.FilingEntityManagerUnsecuredControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_filing_entity**](FilingEntityManagerUnsecuredControllerApi.md#get_filing_entity) | **GET** /public/filing-entity-manager/{cik} | 


# **get_filing_entity**
> FilingEntity get_filing_entity(cik)



### Example

```python
import time
import openapi_client
from openapi_client.api import filing_entity_manager_unsecured_controller_api
from openapi_client.model.filing_entity import FilingEntity
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = filing_entity_manager_unsecured_controller_api.FilingEntityManagerUnsecuredControllerApi(api_client)
    cik = "cik_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_filing_entity(cik)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FilingEntityManagerUnsecuredControllerApi->get_filing_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik** | **str**|  |

### Return type

[**FilingEntity**](FilingEntity.md)

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


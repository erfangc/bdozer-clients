# openapi_client.StockAnalysisExcelDownloaderControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](StockAnalysisExcelDownloaderControllerApi.md#download) | **GET** /api/stock-analyzer/workflow/{id}/download | 


# **download**
> [str] download(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_excel_downloader_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = stock_analysis_excel_downloader_controller_api.StockAnalysisExcelDownloaderControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.download(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisExcelDownloaderControllerApi->download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**[str]**

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


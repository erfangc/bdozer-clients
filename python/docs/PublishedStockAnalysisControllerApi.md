# openapi_client.PublishedStockAnalysisControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_published_stock_analyses**](PublishedStockAnalysisControllerApi.md#find_published_stock_analyses) | **GET** /public/published-stock-analyses | 
[**get_published_stock_analysis**](PublishedStockAnalysisControllerApi.md#get_published_stock_analysis) | **GET** /public/published-stock-analyses/{id} | 


# **find_published_stock_analyses**
> FindStockAnalysisResponse find_published_stock_analyses()



### Example

```python
import time
import openapi_client
from openapi_client.api import published_stock_analysis_controller_api
from openapi_client.model.find_stock_analysis_response import FindStockAnalysisResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = published_stock_analysis_controller_api.PublishedStockAnalysisControllerApi(api_client)
    user_id = "userId_example" # str |  (optional)
    cik = "cik_example" # str |  (optional)
    ticker = "ticker_example" # str |  (optional)
    skip = 1 # int |  (optional)
    limit = 1 # int |  (optional)
    term = "term_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.find_published_stock_analyses(user_id=user_id, cik=cik, ticker=ticker, skip=skip, limit=limit, term=term)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PublishedStockAnalysisControllerApi->find_published_stock_analyses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional]
 **cik** | **str**|  | [optional]
 **ticker** | **str**|  | [optional]
 **skip** | **int**|  | [optional]
 **limit** | **int**|  | [optional]
 **term** | **str**|  | [optional]

### Return type

[**FindStockAnalysisResponse**](FindStockAnalysisResponse.md)

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

# **get_published_stock_analysis**
> StockAnalysis2 get_published_stock_analysis(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import published_stock_analysis_controller_api
from openapi_client.model.stock_analysis2 import StockAnalysis2
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = published_stock_analysis_controller_api.PublishedStockAnalysisControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_published_stock_analysis(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PublishedStockAnalysisControllerApi->get_published_stock_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**StockAnalysis2**](StockAnalysis2.md)

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


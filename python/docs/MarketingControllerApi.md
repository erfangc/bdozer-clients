# openapi_client.MarketingControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**early_access_requests**](MarketingControllerApi.md#early_access_requests) | **POST** /public/marketing/early-access-requests | 
[**feedback20210329**](MarketingControllerApi.md#feedback20210329) | **POST** /public/marketing/2021-03-29/feedback | 
[**stock_analysis_interest**](MarketingControllerApi.md#stock_analysis_interest) | **POST** /public/marketing/stock-analysis-interest | 
[**stock_analysis_request**](MarketingControllerApi.md#stock_analysis_request) | **POST** /public/marketing/stock-analysis-request | 


# **early_access_requests**
> early_access_requests(early_access_request)



### Example

```python
import time
import openapi_client
from openapi_client.api import marketing_controller_api
from openapi_client.model.early_access_request import EarlyAccessRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = marketing_controller_api.MarketingControllerApi(api_client)
    early_access_request = EarlyAccessRequest(
        get_id="get_id_example",
        email="email_example",
        last_updated=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # EarlyAccessRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.early_access_requests(early_access_request)
    except openapi_client.ApiException as e:
        print("Exception when calling MarketingControllerApi->early_access_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **early_access_request** | [**EarlyAccessRequest**](EarlyAccessRequest.md)|  |

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

# **feedback20210329**
> feedback20210329(feedback)



### Example

```python
import time
import openapi_client
from openapi_client.api import marketing_controller_api
from openapi_client.model.feedback import Feedback
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = marketing_controller_api.MarketingControllerApi(api_client)
    feedback = Feedback(
        get_id="get_id_example",
        body={},
        last_updated=dateutil_parser('1970-01-01T00:00:00.00Z'),
        version="version_example",
    ) # Feedback | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.feedback20210329(feedback)
    except openapi_client.ApiException as e:
        print("Exception when calling MarketingControllerApi->feedback20210329: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback** | [**Feedback**](Feedback.md)|  |

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

# **stock_analysis_interest**
> stock_analysis_interest(stock_analysis_interest)



### Example

```python
import time
import openapi_client
from openapi_client.api import marketing_controller_api
from openapi_client.model.stock_analysis_interest import StockAnalysisInterest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = marketing_controller_api.MarketingControllerApi(api_client)
    stock_analysis_interest = StockAnalysisInterest(
        get_id="get_id_example",
        email="email_example",
        requests=[
            StockAnalysisRequest(
                get_id="get_id_example",
                cik="cik_example",
                ticker="ticker_example",
                last_updated=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        last_updated=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # StockAnalysisInterest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.stock_analysis_interest(stock_analysis_interest)
    except openapi_client.ApiException as e:
        print("Exception when calling MarketingControllerApi->stock_analysis_interest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_analysis_interest** | [**StockAnalysisInterest**](StockAnalysisInterest.md)|  |

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

# **stock_analysis_request**
> stock_analysis_request(stock_analysis_request)



### Example

```python
import time
import openapi_client
from openapi_client.api import marketing_controller_api
from openapi_client.model.stock_analysis_request import StockAnalysisRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = marketing_controller_api.MarketingControllerApi(api_client)
    stock_analysis_request = [
        StockAnalysisRequest(
            get_id="get_id_example",
            cik="cik_example",
            ticker="ticker_example",
            last_updated=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ] # [StockAnalysisRequest] | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.stock_analysis_request(stock_analysis_request)
    except openapi_client.ApiException as e:
        print("Exception when calling MarketingControllerApi->stock_analysis_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_analysis_request** | [**[StockAnalysisRequest]**](StockAnalysisRequest.md)|  |

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


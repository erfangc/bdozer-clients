# openapi_client.RevenueModelerControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_revenue_model**](RevenueModelerControllerApi.md#delete_revenue_model) | **DELETE** /api/revenue-modeler/{id} | 
[**get_revenue_model**](RevenueModelerControllerApi.md#get_revenue_model) | **GET** /api/revenue-modeler/{id} | 
[**model_revenue**](RevenueModelerControllerApi.md#model_revenue) | **POST** /api/revenue-modeler/model-revenue | 
[**save_revenue_model**](RevenueModelerControllerApi.md#save_revenue_model) | **POST** /api/revenue-modeler | 


# **delete_revenue_model**
> delete_revenue_model(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import revenue_modeler_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revenue_modeler_controller_api.RevenueModelerControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_revenue_model(id)
    except openapi_client.ApiException as e:
        print("Exception when calling RevenueModelerControllerApi->delete_revenue_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get_revenue_model**
> RevenueModel get_revenue_model(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import revenue_modeler_controller_api
from openapi_client.model.revenue_model import RevenueModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revenue_modeler_controller_api.RevenueModelerControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_revenue_model(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RevenueModelerControllerApi->get_revenue_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**RevenueModel**](RevenueModel.md)

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

# **model_revenue**
> ManualProjections model_revenue(revenue_model)



### Example

```python
import time
import openapi_client
from openapi_client.api import revenue_modeler_controller_api
from openapi_client.model.manual_projections import ManualProjections
from openapi_client.model.revenue_model import RevenueModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revenue_modeler_controller_api.RevenueModelerControllerApi(api_client)
    revenue_model = RevenueModel(
        get_id="get_id_example",
        revenue_driver_type="ZacksEstimates",
        stock_analysis_id="stock_analysis_id_example",
        terminal_year=1,
        terminal_year_average_revenue_per_user=3.14,
        terminal_year_active_user=3.14,
    ) # RevenueModel | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.model_revenue(revenue_model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RevenueModelerControllerApi->model_revenue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revenue_model** | [**RevenueModel**](RevenueModel.md)|  |

### Return type

[**ManualProjections**](ManualProjections.md)

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

# **save_revenue_model**
> save_revenue_model(revenue_model)



### Example

```python
import time
import openapi_client
from openapi_client.api import revenue_modeler_controller_api
from openapi_client.model.revenue_model import RevenueModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = revenue_modeler_controller_api.RevenueModelerControllerApi(api_client)
    revenue_model = RevenueModel(
        get_id="get_id_example",
        revenue_driver_type="ZacksEstimates",
        stock_analysis_id="stock_analysis_id_example",
        terminal_year=1,
        terminal_year_average_revenue_per_user=3.14,
        terminal_year_active_user=3.14,
    ) # RevenueModel | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.save_revenue_model(revenue_model)
    except openapi_client.ApiException as e:
        print("Exception when calling RevenueModelerControllerApi->save_revenue_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revenue_model** | [**RevenueModel**](RevenueModel.md)|  |

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


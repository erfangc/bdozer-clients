# openapi_client.FilingEntityManagerControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bootstrap_filing_entity**](FilingEntityManagerControllerApi.md#bootstrap_filing_entity) | **POST** /api/filing-entity-manager/{cik} | 
[**bootstrap_filing_entity_sync**](FilingEntityManagerControllerApi.md#bootstrap_filing_entity_sync) | **POST** /api/filing-entity-manager/{cik}/sync | 
[**create_filing_entity**](FilingEntityManagerControllerApi.md#create_filing_entity) | **POST** /api/filing-entity-manager/{cik}/create | 
[**save_filing_entity**](FilingEntityManagerControllerApi.md#save_filing_entity) | **POST** /api/filing-entity-manager | 


# **bootstrap_filing_entity**
> FilingEntity bootstrap_filing_entity(cik)



### Example

```python
import time
import openapi_client
from openapi_client.api import filing_entity_manager_controller_api
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
    api_instance = filing_entity_manager_controller_api.FilingEntityManagerControllerApi(api_client)
    cik = "cik_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bootstrap_filing_entity(cik)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FilingEntityManagerControllerApi->bootstrap_filing_entity: %s\n" % e)
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

# **bootstrap_filing_entity_sync**
> FilingEntity bootstrap_filing_entity_sync(cik)



### Example

```python
import time
import openapi_client
from openapi_client.api import filing_entity_manager_controller_api
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
    api_instance = filing_entity_manager_controller_api.FilingEntityManagerControllerApi(api_client)
    cik = "cik_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bootstrap_filing_entity_sync(cik)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FilingEntityManagerControllerApi->bootstrap_filing_entity_sync: %s\n" % e)
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

# **create_filing_entity**
> FilingEntity create_filing_entity(cik)



### Example

```python
import time
import openapi_client
from openapi_client.api import filing_entity_manager_controller_api
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
    api_instance = filing_entity_manager_controller_api.FilingEntityManagerControllerApi(api_client)
    cik = "cik_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_filing_entity(cik)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FilingEntityManagerControllerApi->create_filing_entity: %s\n" % e)
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

# **save_filing_entity**
> save_filing_entity(filing_entity)



### Example

```python
import time
import openapi_client
from openapi_client.api import filing_entity_manager_controller_api
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
    api_instance = filing_entity_manager_controller_api.FilingEntityManagerControllerApi(api_client)
    filing_entity = FilingEntity(
        get_id="get_id_example",
        cik="cik_example",
        trading_symbol="trading_symbol_example",
        name="name_example",
        entity_type="entity_type_example",
        sic="sic_example",
        sic_description="sic_description_example",
        insider_transaction_for_owner_exists=1,
        insider_transaction_for_issuer_exists=1,
        tickers=[
            "tickers_example",
        ],
        exchanges=[],
        ein="ein_example",
        description="description_example",
        website="website_example",
        investor_website="investor_website_example",
        category="category_example",
        fiscal_year_end="fiscal_year_end_example",
        state_of_incorporation="state_of_incorporation_example",
        state_of_incorporation_description="state_of_incorporation_description_example",
        phone="phone_example",
        business_address=Address(
            sheet=1,
            sheet_name="sheet_name_example",
            row=1,
            column=1,
            column_letter="column_letter_example",
        ),
        status_message="status_message_example",
        last_updated="last_updated_example",
        latest_adsh="latest_adsh_example",
        model_template=ModelTemplate(
            name="name_example",
            template="template_example",
        ),
    ) # FilingEntity | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.save_filing_entity(filing_entity)
    except openapi_client.ApiException as e:
        print("Exception when calling FilingEntityManagerControllerApi->save_filing_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filing_entity** | [**FilingEntity**](FilingEntity.md)|  |

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


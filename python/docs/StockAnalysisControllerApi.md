# openapi_client.StockAnalysisControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_stock_analysis**](StockAnalysisControllerApi.md#delete_stock_analysis) | **DELETE** /api/stock-analyzer/stock-analyses/{id} | 
[**evaluate_stock_analysis**](StockAnalysisControllerApi.md#evaluate_stock_analysis) | **POST** /api/stock-analyzer/stock-analyses/evaluate | 
[**find_stock_analyses**](StockAnalysisControllerApi.md#find_stock_analyses) | **GET** /api/stock-analyzer/stock-analyses | 
[**get_stock_analysis**](StockAnalysisControllerApi.md#get_stock_analysis) | **GET** /api/stock-analyzer/stock-analyses/{id} | 
[**publish**](StockAnalysisControllerApi.md#publish) | **POST** /api/stock-analyzer/stock-analyses/{id}/publish | 
[**refresh_stock_analysis**](StockAnalysisControllerApi.md#refresh_stock_analysis) | **POST** /api/stock-analyzer/stock-analyses/refresh | Refresh a stock analysis by rerunning the model
[**save_stock_analysis**](StockAnalysisControllerApi.md#save_stock_analysis) | **POST** /api/stock-analyzer/stock-analyses | 
[**unpublish**](StockAnalysisControllerApi.md#unpublish) | **POST** /api/stock-analyzer/stock-analyses/{id}/unpublish | 


# **delete_stock_analysis**
> delete_stock_analysis(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_controller_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = stock_analysis_controller_api.StockAnalysisControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_stock_analysis(id)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisControllerApi->delete_stock_analysis: %s\n" % e)
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

# **evaluate_stock_analysis**
> EvaluateModelResponse evaluate_stock_analysis(evaluate_model_request)



         This API evaluates a model you've assembled and return a stock analysis object                   The passed in Model represents high level relationship between the various financial statement items of underlying a stock          Calling this method evaluates those relationships and turn them into real numbers                  This API does not persist (save) the stock analysis. Please call the stock analysis service API to save the analysis                  This is a stateless calculator         

### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_controller_api
from openapi_client.model.evaluate_model_request import EvaluateModelRequest
from openapi_client.model.evaluate_model_response import EvaluateModelResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = stock_analysis_controller_api.StockAnalysisControllerApi(api_client)
    evaluate_model_request = EvaluateModelRequest(
        model=Model(
            ticker="ticker_example",
            cik="cik_example",
            adsh="adsh_example",
            name="name_example",
            item_overrides=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[
                            "fact_ids_example",
                        ],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[
                            Component(
                                weight=3.14,
                                item_name="item_name_example",
                            ),
                        ],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={
                            "key": "key_example",
                        },
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            suppressed_items=[
                "suppressed_items_example",
            ],
            total_revenue_concept_name="total_revenue_concept_name_example",
            eps_concept_name="eps_concept_name_example",
            net_income_concept_name="net_income_concept_name_example",
            shares_outstanding_concept_name="shares_outstanding_concept_name_example",
            income_statement_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            balance_sheet_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            cash_flow_statement_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            other_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            beta=3.14,
            risk_free_rate=3.14,
            equity_risk_premium=3.14,
            terminal_growth_rate=3.14,
            periods=1,
            excel_column_offset=1,
            excel_row_offset=1,
        ),
    ) # EvaluateModelRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.evaluate_stock_analysis(evaluate_model_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisControllerApi->evaluate_stock_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluate_model_request** | [**EvaluateModelRequest**](EvaluateModelRequest.md)|  |

### Return type

[**EvaluateModelResponse**](EvaluateModelResponse.md)

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

# **find_stock_analyses**
> FindStockAnalysisResponse find_stock_analyses()



### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_controller_api
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
    api_instance = stock_analysis_controller_api.StockAnalysisControllerApi(api_client)
    published = True # bool |  (optional)
    user_id = "userId_example" # str |  (optional)
    cik = "cik_example" # str |  (optional)
    ticker = "ticker_example" # str |  (optional)
    skip = 1 # int |  (optional)
    limit = 1 # int |  (optional)
    term = "term_example" # str |  (optional)
    tags = [
        "tags_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.find_stock_analyses(published=published, user_id=user_id, cik=cik, ticker=ticker, skip=skip, limit=limit, term=term, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisControllerApi->find_stock_analyses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **published** | **bool**|  | [optional]
 **user_id** | **str**|  | [optional]
 **cik** | **str**|  | [optional]
 **ticker** | **str**|  | [optional]
 **skip** | **int**|  | [optional]
 **limit** | **int**|  | [optional]
 **term** | **str**|  | [optional]
 **tags** | **[str]**|  | [optional]

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

# **get_stock_analysis**
> StockAnalysis2 get_stock_analysis(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_controller_api
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
    api_instance = stock_analysis_controller_api.StockAnalysisControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_stock_analysis(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisControllerApi->get_stock_analysis: %s\n" % e)
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

# **publish**
> StockAnalysis2 publish(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_controller_api
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
    api_instance = stock_analysis_controller_api.StockAnalysisControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.publish(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisControllerApi->publish: %s\n" % e)
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

# **refresh_stock_analysis**
> StockAnalysis2 refresh_stock_analysis(stock_analysis2)

Refresh a stock analysis by rerunning the model

         This API refreshes an existing stock analysis and re-evaluate         the model attached to it to produce renewed outputs. Call this API          when you are in possession of a previously run stock analysis                  The returned refreshed stock analysis preserve all the metadata, model overrides         of the original analysis                  This API does not persist (save) the new analysis. This API is a stateless calculator         

### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_controller_api
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
    api_instance = stock_analysis_controller_api.StockAnalysisControllerApi(api_client)
    stock_analysis2 = StockAnalysis2(
        get_id="get_id_example",
        name="name_example",
        description="description_example",
        cik="cik_example",
        ticker="ticker_example",
        model=Model(
            ticker="ticker_example",
            cik="cik_example",
            adsh="adsh_example",
            name="name_example",
            item_overrides=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[
                            "fact_ids_example",
                        ],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[
                            Component(
                                weight=3.14,
                                item_name="item_name_example",
                            ),
                        ],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={
                            "key": "key_example",
                        },
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            suppressed_items=[
                "suppressed_items_example",
            ],
            total_revenue_concept_name="total_revenue_concept_name_example",
            eps_concept_name="eps_concept_name_example",
            net_income_concept_name="net_income_concept_name_example",
            shares_outstanding_concept_name="shares_outstanding_concept_name_example",
            income_statement_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            balance_sheet_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            cash_flow_statement_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            other_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            beta=3.14,
            risk_free_rate=3.14,
            equity_risk_premium=3.14,
            terminal_growth_rate=3.14,
            periods=1,
            excel_column_offset=1,
            excel_row_offset=1,
        ),
        cells=[
            Cell(
                period=1,
                name="name_example",
                item=Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
                value=3.14,
                formula="formula_example",
                excel_formula="excel_formula_example",
                address=Address(
                    sheet=1,
                    sheet_name="sheet_name_example",
                    row=1,
                    column=1,
                    column_letter="column_letter_example",
                ),
                dependent_cell_names=[
                    "dependent_cell_names_example",
                ],
            ),
        ],
        derived_stock_analytics=DerivedStockAnalytics(
            zero_growth_price=3.14,
            business_waterfall={
                "key": Waterfall(
                    revenue=Cell(
                        period=1,
                        name="name_example",
                        item=Item(
                            name="name_example",
                            description="description_example",
                            type="Discrete",
                            historical_value=HistoricalValue(
                                fact_id="fact_id_example",
                                fact_ids=[],
                                concept_name="concept_name_example",
                                document_fiscal_period_focus="document_fiscal_period_focus_example",
                                document_fiscal_year_focus=1,
                                document_period_end_date="document_period_end_date_example",
                                value=3.14,
                                start_date="start_date_example",
                                end_date="end_date_example",
                                instant="instant_example",
                            ),
                            formula="formula_example",
                            sum_of_other_items=SumOfOtherItems(
                                components=[],
                            ),
                            unit_sales_revenue=UnitSalesRevenue(
                                steady_state_units_sold=3.14,
                                average_selling_price=3.14,
                                initial_units_sold=3.14,
                            ),
                            discrete=Discrete(
                                formulas={},
                            ),
                            percent_of_total_asset=PercentOfTotalAsset(
                                percent_of_total_asset=3.14,
                            ),
                            percent_of_revenue=PercentOfRevenue(
                                percent_of_revenue=3.14,
                            ),
                            compounded_growth=CompoundedGrowth(
                                growth_rate=3.14,
                            ),
                            fixed_cost=FixedCost(
                                cost=3.14,
                            ),
                            commentaries=Commentary(
                                commentary="commentary_example",
                                generator_class="generator_class_example",
                            ),
                            subtotal=True,
                        ),
                        value=3.14,
                        formula="formula_example",
                        excel_formula="excel_formula_example",
                        address=Address(
                            sheet=1,
                            sheet_name="sheet_name_example",
                            row=1,
                            column=1,
                            column_letter="column_letter_example",
                        ),
                        dependent_cell_names=[],
                    ),
                    expenses=[
                        Cell(
                            period=1,
                            name="name_example",
                            item=Item(
                                name="name_example",
                                description="description_example",
                                type="Discrete",
                                historical_value=HistoricalValue(
                                    fact_id="fact_id_example",
                                    fact_ids=[],
                                    concept_name="concept_name_example",
                                    document_fiscal_period_focus="document_fiscal_period_focus_example",
                                    document_fiscal_year_focus=1,
                                    document_period_end_date="document_period_end_date_example",
                                    value=3.14,
                                    start_date="start_date_example",
                                    end_date="end_date_example",
                                    instant="instant_example",
                                ),
                                formula="formula_example",
                                sum_of_other_items=SumOfOtherItems(
                                    components=[],
                                ),
                                unit_sales_revenue=UnitSalesRevenue(
                                    steady_state_units_sold=3.14,
                                    average_selling_price=3.14,
                                    initial_units_sold=3.14,
                                ),
                                discrete=Discrete(
                                    formulas={},
                                ),
                                percent_of_total_asset=PercentOfTotalAsset(
                                    percent_of_total_asset=3.14,
                                ),
                                percent_of_revenue=PercentOfRevenue(
                                    percent_of_revenue=3.14,
                                ),
                                compounded_growth=CompoundedGrowth(
                                    growth_rate=3.14,
                                ),
                                fixed_cost=FixedCost(
                                    cost=3.14,
                                ),
                                commentaries=Commentary(
                                    commentary="commentary_example",
                                    generator_class="generator_class_example",
                                ),
                                subtotal=True,
                            ),
                            value=3.14,
                            formula="formula_example",
                            excel_formula="excel_formula_example",
                            address=Address(
                                sheet=1,
                                sheet_name="sheet_name_example",
                                row=1,
                                column=1,
                                column_letter="column_letter_example",
                            ),
                            dependent_cell_names=[],
                        ),
                    ],
                    profit=Cell(
                        period=1,
                        name="name_example",
                        item=Item(
                            name="name_example",
                            description="description_example",
                            type="Discrete",
                            historical_value=HistoricalValue(
                                fact_id="fact_id_example",
                                fact_ids=[],
                                concept_name="concept_name_example",
                                document_fiscal_period_focus="document_fiscal_period_focus_example",
                                document_fiscal_year_focus=1,
                                document_period_end_date="document_period_end_date_example",
                                value=3.14,
                                start_date="start_date_example",
                                end_date="end_date_example",
                                instant="instant_example",
                            ),
                            formula="formula_example",
                            sum_of_other_items=SumOfOtherItems(
                                components=[],
                            ),
                            unit_sales_revenue=UnitSalesRevenue(
                                steady_state_units_sold=3.14,
                                average_selling_price=3.14,
                                initial_units_sold=3.14,
                            ),
                            discrete=Discrete(
                                formulas={},
                            ),
                            percent_of_total_asset=PercentOfTotalAsset(
                                percent_of_total_asset=3.14,
                            ),
                            percent_of_revenue=PercentOfRevenue(
                                percent_of_revenue=3.14,
                            ),
                            compounded_growth=CompoundedGrowth(
                                growth_rate=3.14,
                            ),
                            fixed_cost=FixedCost(
                                cost=3.14,
                            ),
                            commentaries=Commentary(
                                commentary="commentary_example",
                                generator_class="generator_class_example",
                            ),
                            subtotal=True,
                        ),
                        value=3.14,
                        formula="formula_example",
                        excel_formula="excel_formula_example",
                        address=Address(
                            sheet=1,
                            sheet_name="sheet_name_example",
                            row=1,
                            column=1,
                            column_letter="column_letter_example",
                        ),
                        dependent_cell_names=[],
                    ),
                ),
            },
            share_outstanding=Item(
                name="name_example",
                description="description_example",
                type="Discrete",
                historical_value=HistoricalValue(
                    fact_id="fact_id_example",
                    fact_ids=[],
                    concept_name="concept_name_example",
                    document_fiscal_period_focus="document_fiscal_period_focus_example",
                    document_fiscal_year_focus=1,
                    document_period_end_date="document_period_end_date_example",
                    value=3.14,
                    start_date="start_date_example",
                    end_date="end_date_example",
                    instant="instant_example",
                ),
                formula="formula_example",
                sum_of_other_items=SumOfOtherItems(
                    components=[],
                ),
                unit_sales_revenue=UnitSalesRevenue(
                    steady_state_units_sold=3.14,
                    average_selling_price=3.14,
                    initial_units_sold=3.14,
                ),
                discrete=Discrete(
                    formulas={},
                ),
                percent_of_total_asset=PercentOfTotalAsset(
                    percent_of_total_asset=3.14,
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                compounded_growth=CompoundedGrowth(
                    growth_rate=3.14,
                ),
                fixed_cost=FixedCost(
                    cost=3.14,
                ),
                commentaries=Commentary(
                    commentary="commentary_example",
                    generator_class="generator_class_example",
                ),
                subtotal=True,
            ),
            profit_per_share=Item(
                name="name_example",
                description="description_example",
                type="Discrete",
                historical_value=HistoricalValue(
                    fact_id="fact_id_example",
                    fact_ids=[],
                    concept_name="concept_name_example",
                    document_fiscal_period_focus="document_fiscal_period_focus_example",
                    document_fiscal_year_focus=1,
                    document_period_end_date="document_period_end_date_example",
                    value=3.14,
                    start_date="start_date_example",
                    end_date="end_date_example",
                    instant="instant_example",
                ),
                formula="formula_example",
                sum_of_other_items=SumOfOtherItems(
                    components=[],
                ),
                unit_sales_revenue=UnitSalesRevenue(
                    steady_state_units_sold=3.14,
                    average_selling_price=3.14,
                    initial_units_sold=3.14,
                ),
                discrete=Discrete(
                    formulas={},
                ),
                percent_of_total_asset=PercentOfTotalAsset(
                    percent_of_total_asset=3.14,
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                compounded_growth=CompoundedGrowth(
                    growth_rate=3.14,
                ),
                fixed_cost=FixedCost(
                    cost=3.14,
                ),
                commentaries=Commentary(
                    commentary="commentary_example",
                    generator_class="generator_class_example",
                ),
                subtotal=True,
            ),
            target_price=3.14,
            discount_rate=3.14,
            revenue_cagr=3.14,
            current_price=3.14,
        ),
        user_id="user_id_example",
        tags=[
            "tags_example",
        ],
        published=True,
        last_updated=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # StockAnalysis2 | 

    # example passing only required values which don't have defaults set
    try:
        # Refresh a stock analysis by rerunning the model
        api_response = api_instance.refresh_stock_analysis(stock_analysis2)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisControllerApi->refresh_stock_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_analysis2** | [**StockAnalysis2**](StockAnalysis2.md)|  |

### Return type

[**StockAnalysis2**](StockAnalysis2.md)

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

# **save_stock_analysis**
> save_stock_analysis(stock_analysis2)



### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_controller_api
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
    api_instance = stock_analysis_controller_api.StockAnalysisControllerApi(api_client)
    stock_analysis2 = StockAnalysis2(
        get_id="get_id_example",
        name="name_example",
        description="description_example",
        cik="cik_example",
        ticker="ticker_example",
        model=Model(
            ticker="ticker_example",
            cik="cik_example",
            adsh="adsh_example",
            name="name_example",
            item_overrides=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[
                            "fact_ids_example",
                        ],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[
                            Component(
                                weight=3.14,
                                item_name="item_name_example",
                            ),
                        ],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={
                            "key": "key_example",
                        },
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            suppressed_items=[
                "suppressed_items_example",
            ],
            total_revenue_concept_name="total_revenue_concept_name_example",
            eps_concept_name="eps_concept_name_example",
            net_income_concept_name="net_income_concept_name_example",
            shares_outstanding_concept_name="shares_outstanding_concept_name_example",
            income_statement_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            balance_sheet_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            cash_flow_statement_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            other_items=[
                Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            beta=3.14,
            risk_free_rate=3.14,
            equity_risk_premium=3.14,
            terminal_growth_rate=3.14,
            periods=1,
            excel_column_offset=1,
            excel_row_offset=1,
        ),
        cells=[
            Cell(
                period=1,
                name="name_example",
                item=Item(
                    name="name_example",
                    description="description_example",
                    type="Discrete",
                    historical_value=HistoricalValue(
                        fact_id="fact_id_example",
                        fact_ids=[],
                        concept_name="concept_name_example",
                        document_fiscal_period_focus="document_fiscal_period_focus_example",
                        document_fiscal_year_focus=1,
                        document_period_end_date="document_period_end_date_example",
                        value=3.14,
                        start_date="start_date_example",
                        end_date="end_date_example",
                        instant="instant_example",
                    ),
                    formula="formula_example",
                    sum_of_other_items=SumOfOtherItems(
                        components=[],
                    ),
                    unit_sales_revenue=UnitSalesRevenue(
                        steady_state_units_sold=3.14,
                        average_selling_price=3.14,
                        initial_units_sold=3.14,
                    ),
                    discrete=Discrete(
                        formulas={},
                    ),
                    percent_of_total_asset=PercentOfTotalAsset(
                        percent_of_total_asset=3.14,
                    ),
                    percent_of_revenue=PercentOfRevenue(
                        percent_of_revenue=3.14,
                    ),
                    compounded_growth=CompoundedGrowth(
                        growth_rate=3.14,
                    ),
                    fixed_cost=FixedCost(
                        cost=3.14,
                    ),
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
                value=3.14,
                formula="formula_example",
                excel_formula="excel_formula_example",
                address=Address(
                    sheet=1,
                    sheet_name="sheet_name_example",
                    row=1,
                    column=1,
                    column_letter="column_letter_example",
                ),
                dependent_cell_names=[
                    "dependent_cell_names_example",
                ],
            ),
        ],
        derived_stock_analytics=DerivedStockAnalytics(
            zero_growth_price=3.14,
            business_waterfall={
                "key": Waterfall(
                    revenue=Cell(
                        period=1,
                        name="name_example",
                        item=Item(
                            name="name_example",
                            description="description_example",
                            type="Discrete",
                            historical_value=HistoricalValue(
                                fact_id="fact_id_example",
                                fact_ids=[],
                                concept_name="concept_name_example",
                                document_fiscal_period_focus="document_fiscal_period_focus_example",
                                document_fiscal_year_focus=1,
                                document_period_end_date="document_period_end_date_example",
                                value=3.14,
                                start_date="start_date_example",
                                end_date="end_date_example",
                                instant="instant_example",
                            ),
                            formula="formula_example",
                            sum_of_other_items=SumOfOtherItems(
                                components=[],
                            ),
                            unit_sales_revenue=UnitSalesRevenue(
                                steady_state_units_sold=3.14,
                                average_selling_price=3.14,
                                initial_units_sold=3.14,
                            ),
                            discrete=Discrete(
                                formulas={},
                            ),
                            percent_of_total_asset=PercentOfTotalAsset(
                                percent_of_total_asset=3.14,
                            ),
                            percent_of_revenue=PercentOfRevenue(
                                percent_of_revenue=3.14,
                            ),
                            compounded_growth=CompoundedGrowth(
                                growth_rate=3.14,
                            ),
                            fixed_cost=FixedCost(
                                cost=3.14,
                            ),
                            commentaries=Commentary(
                                commentary="commentary_example",
                                generator_class="generator_class_example",
                            ),
                            subtotal=True,
                        ),
                        value=3.14,
                        formula="formula_example",
                        excel_formula="excel_formula_example",
                        address=Address(
                            sheet=1,
                            sheet_name="sheet_name_example",
                            row=1,
                            column=1,
                            column_letter="column_letter_example",
                        ),
                        dependent_cell_names=[],
                    ),
                    expenses=[
                        Cell(
                            period=1,
                            name="name_example",
                            item=Item(
                                name="name_example",
                                description="description_example",
                                type="Discrete",
                                historical_value=HistoricalValue(
                                    fact_id="fact_id_example",
                                    fact_ids=[],
                                    concept_name="concept_name_example",
                                    document_fiscal_period_focus="document_fiscal_period_focus_example",
                                    document_fiscal_year_focus=1,
                                    document_period_end_date="document_period_end_date_example",
                                    value=3.14,
                                    start_date="start_date_example",
                                    end_date="end_date_example",
                                    instant="instant_example",
                                ),
                                formula="formula_example",
                                sum_of_other_items=SumOfOtherItems(
                                    components=[],
                                ),
                                unit_sales_revenue=UnitSalesRevenue(
                                    steady_state_units_sold=3.14,
                                    average_selling_price=3.14,
                                    initial_units_sold=3.14,
                                ),
                                discrete=Discrete(
                                    formulas={},
                                ),
                                percent_of_total_asset=PercentOfTotalAsset(
                                    percent_of_total_asset=3.14,
                                ),
                                percent_of_revenue=PercentOfRevenue(
                                    percent_of_revenue=3.14,
                                ),
                                compounded_growth=CompoundedGrowth(
                                    growth_rate=3.14,
                                ),
                                fixed_cost=FixedCost(
                                    cost=3.14,
                                ),
                                commentaries=Commentary(
                                    commentary="commentary_example",
                                    generator_class="generator_class_example",
                                ),
                                subtotal=True,
                            ),
                            value=3.14,
                            formula="formula_example",
                            excel_formula="excel_formula_example",
                            address=Address(
                                sheet=1,
                                sheet_name="sheet_name_example",
                                row=1,
                                column=1,
                                column_letter="column_letter_example",
                            ),
                            dependent_cell_names=[],
                        ),
                    ],
                    profit=Cell(
                        period=1,
                        name="name_example",
                        item=Item(
                            name="name_example",
                            description="description_example",
                            type="Discrete",
                            historical_value=HistoricalValue(
                                fact_id="fact_id_example",
                                fact_ids=[],
                                concept_name="concept_name_example",
                                document_fiscal_period_focus="document_fiscal_period_focus_example",
                                document_fiscal_year_focus=1,
                                document_period_end_date="document_period_end_date_example",
                                value=3.14,
                                start_date="start_date_example",
                                end_date="end_date_example",
                                instant="instant_example",
                            ),
                            formula="formula_example",
                            sum_of_other_items=SumOfOtherItems(
                                components=[],
                            ),
                            unit_sales_revenue=UnitSalesRevenue(
                                steady_state_units_sold=3.14,
                                average_selling_price=3.14,
                                initial_units_sold=3.14,
                            ),
                            discrete=Discrete(
                                formulas={},
                            ),
                            percent_of_total_asset=PercentOfTotalAsset(
                                percent_of_total_asset=3.14,
                            ),
                            percent_of_revenue=PercentOfRevenue(
                                percent_of_revenue=3.14,
                            ),
                            compounded_growth=CompoundedGrowth(
                                growth_rate=3.14,
                            ),
                            fixed_cost=FixedCost(
                                cost=3.14,
                            ),
                            commentaries=Commentary(
                                commentary="commentary_example",
                                generator_class="generator_class_example",
                            ),
                            subtotal=True,
                        ),
                        value=3.14,
                        formula="formula_example",
                        excel_formula="excel_formula_example",
                        address=Address(
                            sheet=1,
                            sheet_name="sheet_name_example",
                            row=1,
                            column=1,
                            column_letter="column_letter_example",
                        ),
                        dependent_cell_names=[],
                    ),
                ),
            },
            share_outstanding=Item(
                name="name_example",
                description="description_example",
                type="Discrete",
                historical_value=HistoricalValue(
                    fact_id="fact_id_example",
                    fact_ids=[],
                    concept_name="concept_name_example",
                    document_fiscal_period_focus="document_fiscal_period_focus_example",
                    document_fiscal_year_focus=1,
                    document_period_end_date="document_period_end_date_example",
                    value=3.14,
                    start_date="start_date_example",
                    end_date="end_date_example",
                    instant="instant_example",
                ),
                formula="formula_example",
                sum_of_other_items=SumOfOtherItems(
                    components=[],
                ),
                unit_sales_revenue=UnitSalesRevenue(
                    steady_state_units_sold=3.14,
                    average_selling_price=3.14,
                    initial_units_sold=3.14,
                ),
                discrete=Discrete(
                    formulas={},
                ),
                percent_of_total_asset=PercentOfTotalAsset(
                    percent_of_total_asset=3.14,
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                compounded_growth=CompoundedGrowth(
                    growth_rate=3.14,
                ),
                fixed_cost=FixedCost(
                    cost=3.14,
                ),
                commentaries=Commentary(
                    commentary="commentary_example",
                    generator_class="generator_class_example",
                ),
                subtotal=True,
            ),
            profit_per_share=Item(
                name="name_example",
                description="description_example",
                type="Discrete",
                historical_value=HistoricalValue(
                    fact_id="fact_id_example",
                    fact_ids=[],
                    concept_name="concept_name_example",
                    document_fiscal_period_focus="document_fiscal_period_focus_example",
                    document_fiscal_year_focus=1,
                    document_period_end_date="document_period_end_date_example",
                    value=3.14,
                    start_date="start_date_example",
                    end_date="end_date_example",
                    instant="instant_example",
                ),
                formula="formula_example",
                sum_of_other_items=SumOfOtherItems(
                    components=[],
                ),
                unit_sales_revenue=UnitSalesRevenue(
                    steady_state_units_sold=3.14,
                    average_selling_price=3.14,
                    initial_units_sold=3.14,
                ),
                discrete=Discrete(
                    formulas={},
                ),
                percent_of_total_asset=PercentOfTotalAsset(
                    percent_of_total_asset=3.14,
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                compounded_growth=CompoundedGrowth(
                    growth_rate=3.14,
                ),
                fixed_cost=FixedCost(
                    cost=3.14,
                ),
                commentaries=Commentary(
                    commentary="commentary_example",
                    generator_class="generator_class_example",
                ),
                subtotal=True,
            ),
            target_price=3.14,
            discount_rate=3.14,
            revenue_cagr=3.14,
            current_price=3.14,
        ),
        user_id="user_id_example",
        tags=[
            "tags_example",
        ],
        published=True,
        last_updated=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # StockAnalysis2 | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.save_stock_analysis(stock_analysis2)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisControllerApi->save_stock_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_analysis2** | [**StockAnalysis2**](StockAnalysis2.md)|  |

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

# **unpublish**
> StockAnalysis2 unpublish(id)



### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_controller_api
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
    api_instance = stock_analysis_controller_api.StockAnalysisControllerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.unpublish(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisControllerApi->unpublish: %s\n" % e)
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


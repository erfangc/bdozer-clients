# openapi_client.StockAnalysisWorkflowControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](StockAnalysisWorkflowControllerApi.md#create) | **GET** /api/stock-analyzer/workflow/{cik} | 
[**evaluate**](StockAnalysisWorkflowControllerApi.md#evaluate) | **POST** /api/stock-analyzer/workflow/evaluate | 
[**refresh**](StockAnalysisWorkflowControllerApi.md#refresh) | **POST** /api/stock-analyzer/workflow/refresh | 


# **create**
> StockAnalysis2 create(cik)



### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_workflow_controller_api
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
    api_instance = stock_analysis_workflow_controller_api.StockAnalysisWorkflowControllerApi(api_client)
    cik = "cik_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create(cik)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisWorkflowControllerApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik** | **str**|  |

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

# **evaluate**
> StockAnalysis2 evaluate(evaluate_model_request)



         This API evaluates a model you've assembled and return a stock analysis object                   The passed in Model represents high level relationship between the various financial statement items of underlying a stock          Calling this method evaluates those relationships and turn them into real numbers                  This API does not persist (save) the stock analysis. Please call the stock analysis service API to save the analysis                  This is a stateless calculator     

### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_workflow_controller_api
from openapi_client.model.evaluate_model_request import EvaluateModelRequest
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
    api_instance = stock_analysis_workflow_controller_api.StockAnalysisWorkflowControllerApi(api_client)
    evaluate_model_request = EvaluateModelRequest(
        get_id="get_id_example",
        name="name_example",
        description="description_example",
        model=Model(
            ticker="ticker_example",
            cik="cik_example",
            adsh="adsh_example",
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            total_revenue_concept_name="total_revenue_concept_name_example",
            eps_concept_name="eps_concept_name_example",
            net_income_concept_name="net_income_concept_name_example",
            ebit_concept_name="ebit_concept_name_example",
            operating_cost_concept_name="operating_cost_concept_name_example",
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
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
        api_response = api_instance.evaluate(evaluate_model_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisWorkflowControllerApi->evaluate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluate_model_request** | [**EvaluateModelRequest**](EvaluateModelRequest.md)|  |

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

# **refresh**
> StockAnalysis2 refresh(stock_analysis2)



### Example

```python
import time
import openapi_client
from openapi_client.api import stock_analysis_workflow_controller_api
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
    api_instance = stock_analysis_workflow_controller_api.StockAnalysisWorkflowControllerApi(api_client)
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
                    commentaries=Commentary(
                        commentary="commentary_example",
                        generator_class="generator_class_example",
                    ),
                    subtotal=True,
                ),
            ],
            total_revenue_concept_name="total_revenue_concept_name_example",
            eps_concept_name="eps_concept_name_example",
            net_income_concept_name="net_income_concept_name_example",
            ebit_concept_name="ebit_concept_name_example",
            operating_cost_concept_name="operating_cost_concept_name_example",
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
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
                    subscription_revenue=SubscriptionRevenue(
                        total_subscription_at_terminal_year=3.14,
                        initial_subscriptions=3.14,
                        average_revenue_per_subscription=3.14,
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
                    stock_based_compensation=True,
                    non_cash_expense=True,
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
                            subscription_revenue=SubscriptionRevenue(
                                total_subscription_at_terminal_year=3.14,
                                initial_subscriptions=3.14,
                                average_revenue_per_subscription=3.14,
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
                            stock_based_compensation=True,
                            non_cash_expense=True,
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
                                subscription_revenue=SubscriptionRevenue(
                                    total_subscription_at_terminal_year=3.14,
                                    initial_subscriptions=3.14,
                                    average_revenue_per_subscription=3.14,
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
                                stock_based_compensation=True,
                                non_cash_expense=True,
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
                            subscription_revenue=SubscriptionRevenue(
                                total_subscription_at_terminal_year=3.14,
                                initial_subscriptions=3.14,
                                average_revenue_per_subscription=3.14,
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
                            stock_based_compensation=True,
                            non_cash_expense=True,
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
                subscription_revenue=SubscriptionRevenue(
                    total_subscription_at_terminal_year=3.14,
                    initial_subscriptions=3.14,
                    average_revenue_per_subscription=3.14,
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
                stock_based_compensation=True,
                non_cash_expense=True,
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
                subscription_revenue=SubscriptionRevenue(
                    total_subscription_at_terminal_year=3.14,
                    initial_subscriptions=3.14,
                    average_revenue_per_subscription=3.14,
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
                stock_based_compensation=True,
                non_cash_expense=True,
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
        api_response = api_instance.refresh(stock_analysis2)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StockAnalysisWorkflowControllerApi->refresh: %s\n" % e)
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


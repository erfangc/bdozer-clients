# openapi_client.FactAutoFillerControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fixed_cost_auto_fills**](FactAutoFillerControllerApi.md#get_fixed_cost_auto_fills) | **POST** /api/fact-auto-filler/{factId}/fixed-cost | 
[**get_percent_of_items_auto_fills**](FactAutoFillerControllerApi.md#get_percent_of_items_auto_fills) | **POST** /api/fact-auto-filler/{itemName}/percent-of-another-item | 
[**get_percent_of_revenue_auto_fills**](FactAutoFillerControllerApi.md#get_percent_of_revenue_auto_fills) | **POST** /api/fact-auto-filler/{itemName}/percent-of-revenue | 


# **get_fixed_cost_auto_fills**
> [FixedCostAutoFill] get_fixed_cost_auto_fills(fact_id, model)



### Example

```python
import time
import openapi_client
from openapi_client.api import fact_auto_filler_controller_api
from openapi_client.model.fixed_cost_auto_fill import FixedCostAutoFill
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
    api_instance = fact_auto_filler_controller_api.FactAutoFillerControllerApi(api_client)
    fact_id = "factId_example" # str | 
    model = Model(
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
                discrete=Discrete(
                    formulas={
                        "key": "key_example",
                    },
                ),
                manual_projections=ManualProjections(
                    manual_projections=[
                        ManualProjection(
                            fiscal_year=1,
                            value=3.14,
                        ),
                    ],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
            ),
        ],
        beta=3.14,
        risk_free_rate=3.14,
        equity_risk_premium=3.14,
        terminal_growth_rate=3.14,
        periods=1,
        excel_column_offset=1,
        excel_row_offset=1,
    ) # Model | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fixed_cost_auto_fills(fact_id, model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FactAutoFillerControllerApi->get_fixed_cost_auto_fills: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fact_id** | **str**|  |
 **model** | [**Model**](Model.md)|  |

### Return type

[**[FixedCostAutoFill]**](FixedCostAutoFill.md)

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

# **get_percent_of_items_auto_fills**
> [PercentOfAnotherItemAutoFill] get_percent_of_items_auto_fills(item_name, dependent_item_name, model)



### Example

```python
import time
import openapi_client
from openapi_client.api import fact_auto_filler_controller_api
from openapi_client.model.percent_of_another_item_auto_fill import PercentOfAnotherItemAutoFill
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
    api_instance = fact_auto_filler_controller_api.FactAutoFillerControllerApi(api_client)
    item_name = "itemName_example" # str | 
    dependent_item_name = "dependentItemName_example" # str | 
    model = Model(
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
                discrete=Discrete(
                    formulas={
                        "key": "key_example",
                    },
                ),
                manual_projections=ManualProjections(
                    manual_projections=[
                        ManualProjection(
                            fiscal_year=1,
                            value=3.14,
                        ),
                    ],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
            ),
        ],
        beta=3.14,
        risk_free_rate=3.14,
        equity_risk_premium=3.14,
        terminal_growth_rate=3.14,
        periods=1,
        excel_column_offset=1,
        excel_row_offset=1,
    ) # Model | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_percent_of_items_auto_fills(item_name, dependent_item_name, model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FactAutoFillerControllerApi->get_percent_of_items_auto_fills: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_name** | **str**|  |
 **dependent_item_name** | **str**|  |
 **model** | [**Model**](Model.md)|  |

### Return type

[**[PercentOfAnotherItemAutoFill]**](PercentOfAnotherItemAutoFill.md)

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

# **get_percent_of_revenue_auto_fills**
> [PercentOfRevenueAutoFill] get_percent_of_revenue_auto_fills(item_name, model)



### Example

```python
import time
import openapi_client
from openapi_client.api import fact_auto_filler_controller_api
from openapi_client.model.percent_of_revenue_auto_fill import PercentOfRevenueAutoFill
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
    api_instance = fact_auto_filler_controller_api.FactAutoFillerControllerApi(api_client)
    item_name = "itemName_example" # str | 
    model = Model(
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
                discrete=Discrete(
                    formulas={
                        "key": "key_example",
                    },
                ),
                manual_projections=ManualProjections(
                    manual_projections=[
                        ManualProjection(
                            fiscal_year=1,
                            value=3.14,
                        ),
                    ],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
                discrete=Discrete(
                    formulas={},
                ),
                manual_projections=ManualProjections(
                    manual_projections=[],
                ),
                percent_of_revenue=PercentOfRevenue(
                    percent_of_revenue=3.14,
                ),
                percent_of_another_item=PercentOfAnotherItem(
                    item_name="item_name_example",
                    percent=3.14,
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
            ),
        ],
        beta=3.14,
        risk_free_rate=3.14,
        equity_risk_premium=3.14,
        terminal_growth_rate=3.14,
        periods=1,
        excel_column_offset=1,
        excel_row_offset=1,
    ) # Model | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_percent_of_revenue_auto_fills(item_name, model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FactAutoFillerControllerApi->get_percent_of_revenue_auto_fills: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_name** | **str**|  |
 **model** | [**Model**](Model.md)|  |

### Return type

[**[PercentOfRevenueAutoFill]**](PercentOfRevenueAutoFill.md)

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


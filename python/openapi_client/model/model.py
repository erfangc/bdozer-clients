"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from openapi_client.model.item import Item
    globals()['Item'] = Item


class Model(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'item_overrides': ([Item],),  # noqa: E501
            'income_statement_items': ([Item],),  # noqa: E501
            'balance_sheet_items': ([Item],),  # noqa: E501
            'cash_flow_statement_items': ([Item],),  # noqa: E501
            'other_items': ([Item],),  # noqa: E501
            'beta': (float,),  # noqa: E501
            'risk_free_rate': (float,),  # noqa: E501
            'equity_risk_premium': (float,),  # noqa: E501
            'terminal_growth_rate': (float,),  # noqa: E501
            'periods': (int,),  # noqa: E501
            'excel_column_offset': (int,),  # noqa: E501
            'excel_row_offset': (int,),  # noqa: E501
            'ticker': (str,),  # noqa: E501
            'cik': (str,),  # noqa: E501
            'adsh': (str,),  # noqa: E501
            'total_revenue_concept_name': (str,),  # noqa: E501
            'eps_concept_name': (str,),  # noqa: E501
            'net_income_concept_name': (str,),  # noqa: E501
            'shares_outstanding_concept_name': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'item_overrides': 'itemOverrides',  # noqa: E501
        'income_statement_items': 'incomeStatementItems',  # noqa: E501
        'balance_sheet_items': 'balanceSheetItems',  # noqa: E501
        'cash_flow_statement_items': 'cashFlowStatementItems',  # noqa: E501
        'other_items': 'otherItems',  # noqa: E501
        'beta': 'beta',  # noqa: E501
        'risk_free_rate': 'riskFreeRate',  # noqa: E501
        'equity_risk_premium': 'equityRiskPremium',  # noqa: E501
        'terminal_growth_rate': 'terminalGrowthRate',  # noqa: E501
        'periods': 'periods',  # noqa: E501
        'excel_column_offset': 'excelColumnOffset',  # noqa: E501
        'excel_row_offset': 'excelRowOffset',  # noqa: E501
        'ticker': 'ticker',  # noqa: E501
        'cik': 'cik',  # noqa: E501
        'adsh': 'adsh',  # noqa: E501
        'total_revenue_concept_name': 'totalRevenueConceptName',  # noqa: E501
        'eps_concept_name': 'epsConceptName',  # noqa: E501
        'net_income_concept_name': 'netIncomeConceptName',  # noqa: E501
        'shares_outstanding_concept_name': 'sharesOutstandingConceptName',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, item_overrides, income_statement_items, balance_sheet_items, cash_flow_statement_items, other_items, beta, risk_free_rate, equity_risk_premium, terminal_growth_rate, periods, excel_column_offset, excel_row_offset, *args, **kwargs):  # noqa: E501
        """Model - a model defined in OpenAPI

        Args:
            item_overrides ([Item]):
            income_statement_items ([Item]):
            balance_sheet_items ([Item]):
            cash_flow_statement_items ([Item]):
            other_items ([Item]):
            beta (float):
            risk_free_rate (float):
            equity_risk_premium (float):
            terminal_growth_rate (float):
            periods (int):
            excel_column_offset (int):
            excel_row_offset (int):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ticker (str): [optional]  # noqa: E501
            cik (str): [optional]  # noqa: E501
            adsh (str): [optional]  # noqa: E501
            total_revenue_concept_name (str): [optional]  # noqa: E501
            eps_concept_name (str): [optional]  # noqa: E501
            net_income_concept_name (str): [optional]  # noqa: E501
            shares_outstanding_concept_name (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.item_overrides = item_overrides
        self.income_statement_items = income_statement_items
        self.balance_sheet_items = balance_sheet_items
        self.cash_flow_statement_items = cash_flow_statement_items
        self.other_items = other_items
        self.beta = beta
        self.risk_free_rate = risk_free_rate
        self.equity_risk_premium = equity_risk_premium
        self.terminal_growth_rate = terminal_growth_rate
        self.periods = periods
        self.excel_column_offset = excel_column_offset
        self.excel_row_offset = excel_row_offset
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

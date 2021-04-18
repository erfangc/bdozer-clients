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
    from openapi_client.model.commentary import Commentary
    from openapi_client.model.compounded_growth import CompoundedGrowth
    from openapi_client.model.discrete import Discrete
    from openapi_client.model.fixed_cost import FixedCost
    from openapi_client.model.historical_value import HistoricalValue
    from openapi_client.model.percent_of_revenue import PercentOfRevenue
    from openapi_client.model.percent_of_total_asset import PercentOfTotalAsset
    from openapi_client.model.subscription_revenue import SubscriptionRevenue
    from openapi_client.model.sum_of_other_items import SumOfOtherItems
    from openapi_client.model.unit_sales_revenue import UnitSalesRevenue
    globals()['Commentary'] = Commentary
    globals()['CompoundedGrowth'] = CompoundedGrowth
    globals()['Discrete'] = Discrete
    globals()['FixedCost'] = FixedCost
    globals()['HistoricalValue'] = HistoricalValue
    globals()['PercentOfRevenue'] = PercentOfRevenue
    globals()['PercentOfTotalAsset'] = PercentOfTotalAsset
    globals()['SubscriptionRevenue'] = SubscriptionRevenue
    globals()['SumOfOtherItems'] = SumOfOtherItems
    globals()['UnitSalesRevenue'] = UnitSalesRevenue


class Item(ModelNormal):
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
        ('type',): {
            'DISCRETE': "Discrete",
            'SUBSCRIPTIONREVENUE': "SubscriptionRevenue",
            'COMPOUNDEDGROWTH': "CompoundedGrowth",
            'SUMOFOTHERITEMS': "SumOfOtherItems",
            'UNITSALESREVENUE': "UnitSalesRevenue",
            'CUSTOM': "Custom",
            'PERCENTOFREVENUE': "PercentOfRevenue",
            'PERCENTOFTOTALASSET': "PercentOfTotalAsset",
            'FIXEDCOST': "FixedCost",
        },
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
            'name': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'formula': (str,),  # noqa: E501
            'subtotal': (bool,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'historical_value': (HistoricalValue,),  # noqa: E501
            'sum_of_other_items': (SumOfOtherItems,),  # noqa: E501
            'subscription_revenue': (SubscriptionRevenue,),  # noqa: E501
            'unit_sales_revenue': (UnitSalesRevenue,),  # noqa: E501
            'discrete': (Discrete,),  # noqa: E501
            'percent_of_total_asset': (PercentOfTotalAsset,),  # noqa: E501
            'percent_of_revenue': (PercentOfRevenue,),  # noqa: E501
            'compounded_growth': (CompoundedGrowth,),  # noqa: E501
            'fixed_cost': (FixedCost,),  # noqa: E501
            'stock_based_compensation': (bool,),  # noqa: E501
            'non_cash_expense': (bool,),  # noqa: E501
            'commentaries': (Commentary,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'type': 'type',  # noqa: E501
        'formula': 'formula',  # noqa: E501
        'subtotal': 'subtotal',  # noqa: E501
        'description': 'description',  # noqa: E501
        'historical_value': 'historicalValue',  # noqa: E501
        'sum_of_other_items': 'sumOfOtherItems',  # noqa: E501
        'subscription_revenue': 'subscriptionRevenue',  # noqa: E501
        'unit_sales_revenue': 'unitSalesRevenue',  # noqa: E501
        'discrete': 'discrete',  # noqa: E501
        'percent_of_total_asset': 'percentOfTotalAsset',  # noqa: E501
        'percent_of_revenue': 'percentOfRevenue',  # noqa: E501
        'compounded_growth': 'compoundedGrowth',  # noqa: E501
        'fixed_cost': 'fixedCost',  # noqa: E501
        'stock_based_compensation': 'stockBasedCompensation',  # noqa: E501
        'non_cash_expense': 'nonCashExpense',  # noqa: E501
        'commentaries': 'commentaries',  # noqa: E501
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
    def __init__(self, name, type, formula, subtotal, *args, **kwargs):  # noqa: E501
        """Item - a model defined in OpenAPI

        Args:
            name (str):
            type (str):
            formula (str):
            subtotal (bool):

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
            description (str): [optional]  # noqa: E501
            historical_value (HistoricalValue): [optional]  # noqa: E501
            sum_of_other_items (SumOfOtherItems): [optional]  # noqa: E501
            subscription_revenue (SubscriptionRevenue): [optional]  # noqa: E501
            unit_sales_revenue (UnitSalesRevenue): [optional]  # noqa: E501
            discrete (Discrete): [optional]  # noqa: E501
            percent_of_total_asset (PercentOfTotalAsset): [optional]  # noqa: E501
            percent_of_revenue (PercentOfRevenue): [optional]  # noqa: E501
            compounded_growth (CompoundedGrowth): [optional]  # noqa: E501
            fixed_cost (FixedCost): [optional]  # noqa: E501
            stock_based_compensation (bool): [optional]  # noqa: E501
            non_cash_expense (bool): [optional]  # noqa: E501
            commentaries (Commentary): [optional]  # noqa: E501
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

        self.name = name
        self.type = type
        self.formula = formula
        self.subtotal = subtotal
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

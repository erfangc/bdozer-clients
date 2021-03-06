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
    from openapi_client.model.xbrl_explicit_member import XbrlExplicitMember
    globals()['XbrlExplicitMember'] = XbrlExplicitMember


class Fact(ModelNormal):
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
        ('document_fiscal_period_focus',): {
            'FY': "FY",
            'Q1': "Q1",
            'Q2': "Q2",
            'Q3': "Q3",
            'Q4': "Q4",
            'NA': "NA",
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
            'get_id': (str,),  # noqa: E501
            'instance_document_element_id': (str,),  # noqa: E501
            'instance_document_element_name': (str,),  # noqa: E501
            'cik': (str,),  # noqa: E501
            'adsh': (str,),  # noqa: E501
            'entity_name': (str,),  # noqa: E501
            'primary_symbol': (str,),  # noqa: E501
            'form_type': (str,),  # noqa: E501
            'concept_name': (str,),  # noqa: E501
            'concept_href': (str,),  # noqa: E501
            'namespace': (str,),  # noqa: E501
            'document_fiscal_period_focus': (str,),  # noqa: E501
            'document_fiscal_year_focus': (int,),  # noqa: E501
            'document_period_end_date': (date,),  # noqa: E501
            'explicit_members': ([XbrlExplicitMember],),  # noqa: E501
            'source_document': (str,),  # noqa: E501
            'string_value': (str,),  # noqa: E501
            'last_updated': (str,),  # noqa: E501
            'instant': (date,),  # noqa: E501
            'start_date': (date,),  # noqa: E501
            'end_date': (date,),  # noqa: E501
            'label': (str,),  # noqa: E501
            'verbose_label': (str,),  # noqa: E501
            'label_terse': (str,),  # noqa: E501
            'documentation': (str,),  # noqa: E501
            'double_value': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'get_id': 'get_id',  # noqa: E501
        'instance_document_element_id': 'instanceDocumentElementId',  # noqa: E501
        'instance_document_element_name': 'instanceDocumentElementName',  # noqa: E501
        'cik': 'cik',  # noqa: E501
        'adsh': 'adsh',  # noqa: E501
        'entity_name': 'entityName',  # noqa: E501
        'primary_symbol': 'primarySymbol',  # noqa: E501
        'form_type': 'formType',  # noqa: E501
        'concept_name': 'conceptName',  # noqa: E501
        'concept_href': 'conceptHref',  # noqa: E501
        'namespace': 'namespace',  # noqa: E501
        'document_fiscal_period_focus': 'documentFiscalPeriodFocus',  # noqa: E501
        'document_fiscal_year_focus': 'documentFiscalYearFocus',  # noqa: E501
        'document_period_end_date': 'documentPeriodEndDate',  # noqa: E501
        'explicit_members': 'explicitMembers',  # noqa: E501
        'source_document': 'sourceDocument',  # noqa: E501
        'string_value': 'stringValue',  # noqa: E501
        'last_updated': 'lastUpdated',  # noqa: E501
        'instant': 'instant',  # noqa: E501
        'start_date': 'startDate',  # noqa: E501
        'end_date': 'endDate',  # noqa: E501
        'label': 'label',  # noqa: E501
        'verbose_label': 'verboseLabel',  # noqa: E501
        'label_terse': 'labelTerse',  # noqa: E501
        'documentation': 'documentation',  # noqa: E501
        'double_value': 'doubleValue',  # noqa: E501
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
    def __init__(self, get_id, instance_document_element_id, instance_document_element_name, cik, adsh, entity_name, primary_symbol, form_type, concept_name, concept_href, namespace, document_fiscal_period_focus, document_fiscal_year_focus, document_period_end_date, explicit_members, source_document, string_value, last_updated, *args, **kwargs):  # noqa: E501
        """Fact - a model defined in OpenAPI

        Args:
            get_id (str):
            instance_document_element_id (str):
            instance_document_element_name (str):
            cik (str):
            adsh (str):
            entity_name (str):
            primary_symbol (str):
            form_type (str):
            concept_name (str):
            concept_href (str):
            namespace (str):
            document_fiscal_period_focus (str):
            document_fiscal_year_focus (int):
            document_period_end_date (date):
            explicit_members ([XbrlExplicitMember]):
            source_document (str):
            string_value (str):
            last_updated (str):

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
            instant (date): [optional]  # noqa: E501
            start_date (date): [optional]  # noqa: E501
            end_date (date): [optional]  # noqa: E501
            label (str): [optional]  # noqa: E501
            verbose_label (str): [optional]  # noqa: E501
            label_terse (str): [optional]  # noqa: E501
            documentation (str): [optional]  # noqa: E501
            double_value (float): [optional]  # noqa: E501
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

        self.get_id = get_id
        self.instance_document_element_id = instance_document_element_id
        self.instance_document_element_name = instance_document_element_name
        self.cik = cik
        self.adsh = adsh
        self.entity_name = entity_name
        self.primary_symbol = primary_symbol
        self.form_type = form_type
        self.concept_name = concept_name
        self.concept_href = concept_href
        self.namespace = namespace
        self.document_fiscal_period_focus = document_fiscal_period_focus
        self.document_fiscal_year_focus = document_fiscal_year_focus
        self.document_period_end_date = document_period_end_date
        self.explicit_members = explicit_members
        self.source_document = source_document
        self.string_value = string_value
        self.last_updated = last_updated
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

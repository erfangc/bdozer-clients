"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.fact_base_controller_api import FactBaseControllerApi  # noqa: E501


class TestFactBaseControllerApi(unittest.TestCase):
    """FactBaseControllerApi unit test stubs"""

    def setUp(self):
        self.api = FactBaseControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ingest_filing(self):
        """Test case for ingest_filing

        """
        pass

    def test_ingest_q4_facts(self):
        """Test case for ingest_q4_facts

        """
        pass

    def test_run_rss_filing_ingestor(self):
        """Test case for run_rss_filing_ingestor

        """
        pass


if __name__ == '__main__':
    unittest.main()

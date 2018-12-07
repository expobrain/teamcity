# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dohq_teamcity
from dohq_teamcity.api.build_api import BuildApi  # noqa: E501
from dohq_teamcity.rest import ApiException


class TestBuildApi(unittest.TestCase):
    """BuildApi unit test stubs"""

    def setUp(self):
        self.api = dohq_teamcity.api.build_api.BuildApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_tags(self):
        """Test case for add_tags

        """
        pass

    def test_cancel_build(self):
        """Test case for cancel_build

        """
        pass

    def test_cancel_build_0(self):
        """Test case for cancel_build_0

        """
        pass

    def test_delete_build(self):
        """Test case for delete_build

        """
        pass

    def test_delete_builds(self):
        """Test case for delete_builds

        """
        pass

    def test_delete_comment(self):
        """Test case for delete_comment

        """
        pass

    def test_get_artifacts_directory(self):
        """Test case for get_artifacts_directory

        """
        pass

    def test_get_canceled_info(self):
        """Test case for get_canceled_info

        """
        pass

    def test_get_children(self):
        """Test case for get_children

        """
        pass

    def test_get_children_alias(self):
        """Test case for get_children_alias

        """
        pass

    def test_get_content(self):
        """Test case for get_content

        """
        pass

    def test_get_content_alias(self):
        """Test case for get_content_alias

        """
        pass

    def test_get_metadata(self):
        """Test case for get_metadata

        """
        pass

    def test_get_parameter(self):
        """Test case for get_parameter

        """
        pass

    def test_get_pinned(self):
        """Test case for get_pinned

        """
        pass

    def test_get_problems(self):
        """Test case for get_problems

        """
        pass

    def test_get_root(self):
        """Test case for get_root

        """
        pass

    def test_get_tests(self):
        """Test case for get_tests

        """
        pass

    def test_get_zipped(self):
        """Test case for get_zipped

        """
        pass

    def test_pin_build(self):
        """Test case for pin_build

        """
        pass

    def test_replace_comment(self):
        """Test case for replace_comment

        """
        pass

    def test_replace_tags(self):
        """Test case for replace_tags

        """
        pass

    def test_serve_aggregated_build_status(self):
        """Test case for serve_aggregated_build_status

        """
        pass

    def test_serve_aggregated_build_status_icon(self):
        """Test case for serve_aggregated_build_status_icon

        """
        pass

    def test_serve_all_builds(self):
        """Test case for serve_all_builds

        """
        pass

    def test_serve_build(self):
        """Test case for serve_build

        """
        pass

    def test_serve_build_actual_parameters(self):
        """Test case for serve_build_actual_parameters

        """
        pass

    def test_serve_build_field_by_build_only(self):
        """Test case for serve_build_field_by_build_only

        """
        pass

    def test_serve_build_related_issues(self):
        """Test case for serve_build_related_issues

        """
        pass

    def test_serve_build_related_issues_old(self):
        """Test case for serve_build_related_issues_old

        """
        pass

    def test_serve_build_statistic_value(self):
        """Test case for serve_build_statistic_value

        """
        pass

    def test_serve_build_statistic_values(self):
        """Test case for serve_build_statistic_values

        """
        pass

    def test_serve_build_status_icon(self):
        """Test case for serve_build_status_icon

        """
        pass

    def test_serve_source_file(self):
        """Test case for serve_source_file

        """
        pass

    def test_serve_tags(self):
        """Test case for serve_tags

        """
        pass

    def test_unpin_build(self):
        """Test case for unpin_build

        """
        pass


if __name__ == '__main__':
    unittest.main()
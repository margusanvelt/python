# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.authorization_v1_api import AuthorizationV1Api


class TestAuthorizationV1Api(unittest.TestCase):
    """ AuthorizationV1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.authorization_v1_api.AuthorizationV1Api()

    def tearDown(self):
        pass

    def test_create_namespaced_local_subject_access_review(self):
        """
        Test case for create_namespaced_local_subject_access_review

        
        """
        pass

    def test_create_self_subject_access_review(self):
        """
        Test case for create_self_subject_access_review

        
        """
        pass

    def test_create_self_subject_rules_review(self):
        """
        Test case for create_self_subject_rules_review

        
        """
        pass

    def test_create_subject_access_review(self):
        """
        Test case for create_subject_access_review

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass


if __name__ == '__main__':
    unittest.main()

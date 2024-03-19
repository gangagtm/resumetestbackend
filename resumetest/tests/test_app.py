import pytest
import unittest
from resumetest.viewcount.app import lambda_handler
import json
      
# class TestVisitor(unittest.TestCase):
#     def test_lambda_handler(self):
#         res_api = lambda_handler('a', 'b')
#         self.assertEqual(res_api['statusCode'],200,msg=None)
        
    #need add to pipeline python3 -m unittest test.py


def test_lambda_handler():
    res_api = lambda_handler('a', 'b')
    assert res_api["statusCode"] == 200

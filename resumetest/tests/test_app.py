import pytest
import unittest
from resumetest.viewcount.app import lambda_handler
import json
      

def test_lambda_handler():
    res_api = lambda_handler('a', 'b')
    assert res_api["statusCode"] == 200

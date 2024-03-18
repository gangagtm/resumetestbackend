# tests/test_app.py

import boto3
import json
import pytest
from unittest.mock import MagicMock
from resumetest.viewcount.app import lambda_handler

@pytest.fixture
def mock_dynamodb_table():
    return MagicMock()

def test_lambda_handler(mock_dynamodb_table):
    # Arrange
    event = {}
    context = {}

    # Mocking DynamoDB response
    mock_response = {'Item': {'views': 5}}
    mock_dynamodb_table.get_item.return_value = mock_response

    # Act
    result = lambda_handler(event, context)

    # Assert
    assert result['statusCode'] == 200
    assert result['body'] == '6'  # Incremented view count as a string
    assert mock_dynamodb_table.put_item.called  # Assert that put_item was called

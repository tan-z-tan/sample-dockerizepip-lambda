import json
import numpy as np


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "numpy_value": np.random.rand(3, 2).tolist(),
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
        
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

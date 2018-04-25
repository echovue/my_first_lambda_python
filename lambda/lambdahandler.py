# Main entry method for lambda
def lambda_handler(event, context):
    value = event['initialValue']
    value2 = value + 1
    return {"initialValue": value, "incrementedValue": value2}
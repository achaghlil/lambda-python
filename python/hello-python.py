import json;

def lambda_handler(event, context):
    if 'price' in event and 'discount' in event:
        price = int(event['price'])
        discount = int(event['discount'])
        result = price*(1-discount/100)
        result = f'The discounted price is : {result}'
    else:
        result = 'Missing Price or Discount parameters'
    return {
        'statusCode' : 200,
        'body' : json.dumps(result)
    }
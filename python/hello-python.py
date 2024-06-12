def lambda_handler(event, context):
   message = 'Hello {} !'.format(event['key1'])
   return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
   }

   
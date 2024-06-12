import json;

def lambda_handler(event, context):
   price = int(event['price'])
   discount = int(event['discount'])
   result = price*(1-discount/100)
   
   return {
       'statusCode' : 200,
       'body' : 
   }

   
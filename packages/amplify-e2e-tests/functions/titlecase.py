from titlecase import titlecase
import json

def handler(event, context):
  with open('/opt/data.txt', 'r') as f:
    optContent = f.read()

  return {
    'statusCode': 200,
    'body': json.dumps(titlecase('{{testString}} ') + optContent)
  }

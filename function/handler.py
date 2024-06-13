from datetime import datetime
import cowsay

def handler(event, context):
    return {
        'statusCode': 200,
        'body': cowsay.get_output_string('cow', datetime.now().isoformat())
    }

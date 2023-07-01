import http.server
import socketserver
import boto3
import os

# vars
table_name = 'redirections_table'
aws_region = 'us-east-1'
http_port = 8215

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name=aws_region)
table = dynamodb.Table(table_name)

class RedirectionHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path[1:]  # Remove leading '/'

        # Retrieve redirection mappings from DynamoDB
        response = table.get_item(Key={'source_uri': path})
        if 'Item' in response:
            item = response['Item']
            new_path = item['target_uri']
            self.send_response(302)
            self.send_header('Location', new_path)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Page not found')

# Set up the HTTP server
port = int(os.environ.get('PORT', http_port))
handler = RedirectionHandler
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()

# End;

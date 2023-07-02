import http.server
import socketserver
import boto3
import os
import logging
from sys import stdout

# logging
# logger
logger = logging.getLogger()
logger_level = 'DEBUG' # CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logger.setLevel(logger_level)
logFormatter = logging.Formatter("stdout - %(name)s - [%(asctime)s] - %(levelname)s - \"%(filename)s:%(funcName)s\" - \"%(message)s\"")
consoleHandler = logging.StreamHandler(stdout) #set streamhandler to stdout
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

# 172.17.0.1 - - [02/Jul/2023 00:28:48] "GET /health-check HTTP/1.1" 200 -
# root         2023-07-02 00:28:48,825 DEBUG    app-url-shortener.py:do_GET path2: [health-check]

# vars
table_name = 'redirections_table'
aws_region = 'us-east-1'
http_port = 8215
server_address = '0.0.0.0'

# Connect to DynamoDB
#dynamodb = boto3.resource('dynamodb', region_name=aws_region)
#table = dynamodb.Table(table_name)

class RedirectionHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path[1:]  # Remove leading '/'
        print(path)
        logger.info("path: [%s]", path)
        logger.debug("path2: [%s]", path)

#        self.send_response(302)
#        self.send_header('Location', '/hehehe')
#        self.end_headers()

        if (path == 'health-check'):
            print("/health-check")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello!')
        else:
            print("else")
            self.send_response(302)
            self.send_header('Location', '/caiu-no-else')
            self.end_headers()




#            # Retrieve redirection mappings from DynamoDB
#            response = table.get_item(Key={'source_uri': path})
#            if 'Item' in response:
#                item = response['Item']
#                new_path = item['target_uri']
#                self.send_response(301)
#                self.send_header('Location', new_path)
#                self.end_headers()
#            else:
#                self.send_response(302)
#                self.send_header('Location', 'https://github.com/groorj/aws-url-shortener')
#                self.end_headers()

# Set up the HTTP server
port = int(os.environ.get('PORT', http_port))
handler = RedirectionHandler
with socketserver.TCPServer((server_address, port), handler) as httpd:
    # print(f"Serving at port {port}")
    logger.info("Serving at port [%s]", port)
    httpd.serve_forever()

# End;

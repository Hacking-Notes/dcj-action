from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import time

def send_requests():
    print("\nStarting to send requests from request.txt...")
    try:
        # Read the request from file
        with open('request.txt', 'r') as f:
            raw_request = f.read().strip()
        
        # Parse the basic request info
        lines = raw_request.split('\n')
        method, path, _ = lines[0].split(' ')
        headers = {}
        body = None
        
        # Find where headers end and body begins
        for i, line in enumerate(lines[1:], 1):
            if not line.strip():
                if i < len(lines)-1:
                    body = '\n'.join(lines[i+1:])
                break
            if ': ' in line:
                key, value = line.split(': ', 1)
                headers[key] = value

        # Get the host and build URL
        host = headers.get('Host', '').strip()
        url = f"https://{host}{path}"
        
        print(f"Will send requests to: {url}")
        print("\nSending request...")
        
        # Keep sending requests until we get a 200
        while True:
            try:
                response = requests.request(
                    method=method,
                    url=url,
                    headers=headers,
                    data=body,
                    verify=False,
                    timeout=5
                )
                print(f"Got response: {response.status_code}")
                
                if response.status_code == 200:
                    print("Got 200! Stopping.")
                    break
                    
            except Exception as e:
                print(f"Request failed: {str(e)}")
            
            time.sleep(1)
            
    except Exception as e:
        print(f"Error: {str(e)}")

class RequestHandler(BaseHTTPRequestHandler):
    def handle_one_request(self):
        """Handle a single HTTP request."""
        try:
            print("Received traffic! Starting to send requests...")
            send_requests()  # Start sending requests immediately
            self.server.server_close()  # Stop the server
        except Exception as e:
            print(f"Error: {str(e)}")

def run_server():
    port = 8085
    server = HTTPServer(('', port), RequestHandler)
    print(f"Server started on port {port}")
    print("Waiting for ANY traffic to start sending requests...")
    server.serve_forever()

if __name__ == '__main__':
    import urllib3
    urllib3.disable_warnings()
    run_server() 
# Request Repeater Server

<a href=https://hacking-poc.com/doubleclickjacking>https://hacking-poc.com/doubleclickjacking</a>

## Files

### server.py
The main server that:
1. Listens on port 8085
2. Starts sending requests when it receives ANY traffic
3. Keeps sending requests until getting a 200 response

### request.txt
Contains the raw HTTP request to be sent. Format should be exactly like a Burp Suite request:
```
METHOD /path HTTP/1.1
Host: example.com
Header1: value1
Header2: value2

request body here
```

## Setup

1. Install requirements:
```bash
pip install requests
```

2. Create your request.txt file with the HTTP request you want to send

3. Run the server:
```bash
python server.py
```

## Usage

Follow these steps to execute the attack:

1. **Visit the Exploit Page**  
   Navigate to [https://hacking-poc.com/doubleclickjacking](https://hacking-poc.com/doubleclickjacking).

2. **Prepare the Request**  
   - Edit the file named `request.txt`.  
   - Insert the HTTP request you wish to repeat into `request.txt`.

3. **Start the Server**  
   Launch the server that will monitor for user visits.

4. **Wait for a Target**  
   The server continuously checks for a user visiting the double clickjacking link.

5. **Trigger the Attack**  
   Once a user is detected, the server will:  
   - Stop listening for new requests.  
   - Begin sending the HTTP request from `request.txt`.  
   - Continue sending the request until it receives a `200 OK` response, indicating the authorized action has been completed.


## Example Output
```
Server started on port 8085
Waiting for ANY traffic to start sending requests...
Received traffic! Starting to send requests...

Starting to send requests from request.txt...
Will send requests to: https://example.com/api/endpoint

Sending request...
Got response: 403
Got response: 403
Got response: 403
``` 

from mitmproxy import http
import time

# Initialize a list to track request details
requests_data = []

def request(flow: http.HTTPFlow) -> None:
    # Capture request data when it's made
    start_time = time.time()
    requests_data.append({
        'url': flow.request.url,
        'start_time': start_time,
        'status_code': None,
        'end_time': None,
        'duration': None,
        'content_length': None
    })

def response(flow: http.HTTPFlow) -> None:
    # Capture details about each response
    res = flow.response
    end_time = time.time()

    # Find the matching request based on the URL
    for req in requests_data:
        if req['url'] == flow.request.url:
            req['status_code'] = res.status_code
            req['end_time'] = end_time
            req['duration'] = end_time - req['start_time']
            req['content_length'] = len(res.content)
            break

    # Print captured details
    print(f"URL: {flow.request.url}")
    print(f"Status: {res.status_code}")
    print(f"Time: {req['duration']} seconds")
    print(f"Content Size: {req['content_length']} bytes")
    print("\n\n")

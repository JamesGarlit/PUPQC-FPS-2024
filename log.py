import logging

# Configure logging
logging.basicConfig(filename='fps.log'
                    , level=logging.DEBUG
                    , format='%(asctime)s - %(levelname)s - %(message)s')

# Simulate processing a request
def process_request(request):
    # Simulate an error condition
    if request.get("error"):
        raise ValueError("An error occurred during request processing.")
    return "Request processed successfully from process_request"

# Handle incoming requests
def handle_request(request):
    try:
        # Call the request processing function
        result = process_request(request)
        logging.info(f"Request processed successfully from handle_request: {result}")
        return result
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        return "An error occurred during request processing"

# Simulate web system usage
if __name__ == "__main__":
    request_data = {"key": "value"}
    response = handle_request(request_data)
    print(response)

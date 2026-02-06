# Import necessary libraries from Flask
from flask import Flask, render_template, request, jsonify
# Import the custom get_response function from the chat module
from chat import get_response

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.get("/")
def index_get():
    """
    Handle GET requests to the root URL.
    Render the base.html template.
    
    Returns:
    The rendered HTML template for the home page.
    """
    return render_template("base.html")

# Define a route for making predictions
@app.post("/predict")
def predict():
    """
    Handle POST requests to the /predict URL.
    Process the incoming JSON message and get a response from the chatbot.
    
    Returns:
    A JSON response containing the chatbot's answer.
    """
    # Get the message from the JSON data in the request
    text = request.get_json().get("message")
    # Get the response from the chatbot
    response = get_response(text)
    # Create a dictionary with the response
    message = {"answer": response}
    # Return the response as a JSON object
    return jsonify(message)

# Run the Flask application
if __name__ == "__main__":
    # Start the Flask app in debug mode
    app.run(debug=True)
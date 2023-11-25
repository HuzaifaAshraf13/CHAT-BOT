import os
from flask import Flask, render_template, request
import openai
# not workin heck
app = Flask(__name__)

# Set up OpenAI API credentials
openai_api_key = os.environ.get("OPENAI_API_KEY")
# If no API key found in environment variable, use the one provided in code
if openai_api_key is None:
    openai_api_key = ""
else:
    print("Using API key from environment variable")

openai.api_key = openai_api_key


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")


# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    if completion.choices[0].message != None:
        return completion.choices[0].message

    else:
        return 'Failed to Generate response!'


if __name__ == '__main__':
    app.run()

from flask import Flask, request, redirect
import twilio.twiml
import os

 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def hello_monkey():
    """Respond and greet the caller by name."""

    body_message = str(request.values.get('Body', None))
    rocketnamesarray = body_message.split(' ')
  
    from_number = request.values.get('From', None)

    
    message = "this is a response from the backend"

    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0")

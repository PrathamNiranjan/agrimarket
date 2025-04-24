from flask import Flask, render_template, request
import pickle
import os
from flask import Flask
app = Flask(__name__)

# Ensure this is the main file for Flask
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Use port set by Render
    app.run(host='0.0.0.0', port=port)

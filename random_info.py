"""
Module for generating random passwords and emails
"""
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonify import jsonify
import random, string

app = Flask(__random_info__)
api = Api(app)

class Email(Resource):

    def generate_address(self, length=16):
        """
        Generates a random prefix and attaches it to a loganon email address
        """
        tail = '@loganon.33mail.com'

        prefix = ''.join(random.choice(string.ascii_uppercase + 
                        string.ascii_lowercase + string.digits) for _ in range(length))
        email = {'email' : prefix + tail}
        return jsonify(email)

class Password(Resource):
        
    def generate_password(self, length=16):
        """
        Generates a random password, default length 16
        """
        password_text = ''.join(random.choice(string.ascii_uppercase + string.punctuation + 
                        string.ascii_lowercase + string.digits) for _ in range(length))
        
        password = {'password': password_text}

        return jsonify(password)

api.add_resource(Email, '/email')
api.add_resource(Password, '/password')

if __name__ == '__main__':
    app.run(port='5002')
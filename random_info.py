"""
Module for generating random passwords and emails
"""

# flast imports for creating webapp
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps

# secure password generation
import secrets, string

app = Flask(__name__)
api = Api(app)


class GenerateEmail(Resource):
    def get(self, length=16):
        """
        Generates a random prefix and attaches it to a loganon email address
        """
        tail = "@loganon.33mail.com"

        prefix = "".join(
            secrets.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(length)
        )
        email = {"email": prefix + tail}
        return jsonify(email)


class GeneratePassword(Resource):
    def get(self, length=16):
        """
        Generates a random password, default length 16
        """
        password_text = "".join(
            secrets.choice(
                string.ascii_uppercase
                + string.punctuation
                + string.ascii_lowercase
                + string.digits
            )
            for _ in range(length)
        )

        password = {"password": password_text}

        return jsonify(password)


api.add_resource(GenerateEmail, "/email")
api.add_resource(GeneratePassword, "/password")

if __name__ == "__main__":
    app.run(port="5002")

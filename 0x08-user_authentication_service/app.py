#!/usr/bin/env python3
"""Route module for the Flask app"""

from flask import Flask, jsonify, request, abort, redirect
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth
from typing import Union


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def bienvenue() -> str:
    """ GET /
    Return:
      - Bienvenue message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """Function to register a user from the Flask app"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify(
            {"email": "{}".format(email), "message": "user created"}
        )

    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Function to login a user from the Flask App"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        res = jsonify({"email": "{}".format(email), "message": "logged in"})
        res.set_cookie("session_id", session_id)
        return res
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Function to kill a session from the Flask App"""
    session_id = request.cookies.get("session_id")
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user is not None:
            AUTH.destroy_session(user.id)
            return redirect('/')
        else:
            return abort(403)
    return abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """Function to show profiles"""
    session_id = request.cookies.get("session_id")

    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({{"email": "{}".user.email}})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

#!/usr/bin/env python3
"""Module whichs handles all routes for the Session authentication
"""
from flask import jsonify, request
from models.user import User
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth() -> str:
    """Session Auth function to view the views"""
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400

    user = User()
    objs = user.search()
    obj = None

    for i in objs:
        if i.__dict__['email'] == email:
            obj = i

    if not obj:
        return jsonify({"error": "no user found for this email"}), 404

    if obj.is_valid_password(password) is False:
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    from os import getenv

    session = auth.create_session(obj.id)
    cookie_name = getenv("SESSION_NAME")

    res = jsonify(obj.to_json())
    res.set_cookie(cookie_name, session)

    return res

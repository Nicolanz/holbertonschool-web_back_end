#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)
print(auth.valid_login(email, password))

session_id = auth.create_session(email)
print(session_id)

user = auth.get_user_from_session_id(session_id)

print("\n", user.email)
print(user.id)
print(user.session_id)

#!/usr/bin/env python3
"""
Route module for the session auth
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from flask import request
from models.user import User


class SessionAuth(Auth):
    """ session class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id """
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a User ID based on a Session ID """
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ that returns a User instance based on a cookie value """
        session_cookie = self.session_cookie(request)
        session_id = self.user_id_for_session_id(session_cookie)
        return User.get(session_id)

    def destroy_session(self, request=None):
        """deletes the user session / logout"""
        if not request:
            return False
        session_cookie = self.session_cookie(request)

        if not session_cookie:
            return False

        user_id = self.user_id_for_session_id(session_cookie)

        if not user_id:
            return False
        self.user_id_by_session_id.pop(session_cookie)
        return True

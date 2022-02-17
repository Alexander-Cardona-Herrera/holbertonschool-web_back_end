#!/usr/bin/env python3
"""
Route module for the auth
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Validate the paths """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[len(path) - 1] != '/':
            path = path + '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ returns none """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns none """
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request """
        if request is None:
            return None

        _my_session_id = getenv('SESSION_NAME')
        cookie = request.cookies.get(_my_session_id)
        return cookie

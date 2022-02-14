#!/usr/bin/env python3
"""
Route module for the auth
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """ authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns false """
        return False
    
    def authorization_header(self, request=None) -> str:
        """ returns none """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns none """
        return None

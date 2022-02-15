#!/usr/bin/env python3
"""
Route module for the basic auth
"""
import base64

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ basic authentication class """
    pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization """
        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]

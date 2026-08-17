from __future__ import annotations

__all__ = (
    'Forbidden',
    'GamepassAlreadyOwned',
    'GamepassAlreadyRevoked',
    'GamepassNotForSale',
    'InternalServerError',
    'NoConnectionFound',
    'NotEnoughFunds',
    'NotFound',
    'PendingTransactionAlreadyExists',
    'Unauthorized',
    'UnknownStatus',
    'UnsupportedCreatorType',
    'UserNotFound',
    'WrongDataPassed',
)


class RobloxException(BaseException):
    pass


class HTTPException(RobloxException):
    pass


class ClientException(HTTPException):
    pass


class NoConnectionFound(ClientException):
    def __init__(self):
        super().__init__('No connection has been established.')


class Unauthorized(ClientException):
    def __init__(self):
        super().__init__('Invalid ROBLOSECURITY, or no authorization argument was passed.')


class NotFound(RobloxException):
    def __init__(self):
        super().__init__('Nothing was found.')


class UnknownStatus(HTTPException):
    def __init__(self, status: int):
        super().__init__(f'Unknown status given by the server: `{status}`.')


class InternalServerError(HTTPException):
    def __init__(self):
        super().__init__('An internal server error occurred.')


class Forbidden(HTTPException):
    def __init__(self, message: str):
        super().__init__(message)


class WrongDataPassed(RobloxException):
    def __init__(self):
        super().__init__('Content was not accepted by the Roblox API.')


class GamepassNotForSale(RobloxException):
    def __init__(self):
        super().__init__('Gamepass is not for sale.')


class GamepassAlreadyOwned(RobloxException):
    def __init__(self):
        super().__init__('Gamepass is already owned.')


class NotEnoughFunds(RobloxException):
    def __init__(self):
        super().__init__('Not enough funds.')


class GamepassAlreadyRevoked(RobloxException):
    def __init__(self):
        super().__init__('Gamepass has already been revoked.')


class PendingTransactionAlreadyExists(RobloxException):
    def __init__(self, *args):
        super().__init__('You have a pending transaction. Please wait 1 minute and try again.')


class UnsupportedCreatorType(RobloxException):
    def __init__(self, *args):
        super().__init__('Unsupported creator type.')


class UserNotFound(RobloxException):
    def __init__(self, *args):
        super().__init__('User was not found.')

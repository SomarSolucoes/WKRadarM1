"""Exceções personalizadas para a biblioteca WKRadarM1."""


class WKRadarError(Exception):
    """Exceção base para erros da API WK Radar."""
    pass


class AuthenticationError(WKRadarError):
    """Erro de autenticação (401)."""
    pass


class PermissionError(WKRadarError):
    """Erro de permissão (403)."""
    pass


class NotFoundError(WKRadarError):
    """Recurso não encontrado (404)."""
    pass


class RateLimitError(WKRadarError):
    """Limite de requisições excedido (429)."""
    pass


class ValidationError(WKRadarError):
    """Erro de validação (400)."""
    def __init__(self, message: str, invalid_keys: list = None, details: dict = None):
        super().__init__(message)
        self.invalid_keys = invalid_keys or []
        self.details = details or {}


class BusinessError(WKRadarError):
    """Erro de negócio/regra (422)."""
    pass

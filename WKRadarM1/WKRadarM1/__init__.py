"""
WK Radar API Client - Biblioteca WKRadarM1 para integração com API do WK Radar.

Esta biblioteca fornece uma interface Python completa para a API do WK Radar,
suportando todos os endpoints disponíveis nos módulos:
- Comercial
- Financeiro
- Folha de Pagamento
- Produção
- Empresarial
- Compras
- Contábil
- Estoque
- Gerenciador

Características:
- Suporte a autenticação Bearer Token
- Tratamento automático de rate limiting (429)
- Data shaping com parâmetro fields
- Suporte a filtros por IDs e Códigos Integrador
- Validação de campos obrigatórios
- Type hints completos
- Documentação em PTBR
"""

from .client import WKRadarClient
from .exceptions import (
    WKRadarError,
    AuthenticationError,
    PermissionError,
    NotFoundError,
    RateLimitError,
    ValidationError,
    BusinessError
)

__version__ = "1.0.0"
__author__ = "WK Radar Integration Team"
__all__ = [
    "WKRadarClient",
    "WKRadarError",
    "AuthenticationError",
    "PermissionError",
    "NotFoundError",
    "RateLimitError",
    "ValidationError",
    "BusinessError",
]

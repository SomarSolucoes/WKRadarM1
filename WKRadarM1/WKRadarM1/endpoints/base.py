"""Classe base para os módulos de endpoints."""

from typing import List, Optional, Dict, Any


class BaseEndpoint:
    """Classe base para todos os endpoints da API."""
    
    def __init__(self, client):
        self.client = client

    def _format_filters(self, **kwargs) -> Dict[str, Any]:
        """Formata os filtros para a query string."""
        filters = {}
        for key, value in kwargs.items():
            if value is not None:
                # Converte listas para formato que a API espera (geralmente repetindo o parâmetro ou CSV)
                # O WK Radar parece esperar arrays em query params
                filters[key] = value
        return filters

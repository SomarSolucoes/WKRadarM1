"""Módulo de autenticação para API WK Radar."""

import requests
from typing import Optional
from datetime import datetime
from .exceptions import AuthenticationError


class Authenticator:
    """Gerenciador de autenticação via Bearer Token."""
    
    TOKEN_ENDPOINT = "/api/v1/token"
    
    def __init__(self, base_url: str, empresa: str, username: str, password: str, 
                 id_integrador: Optional[str] = None):
        """
        Inicializa o autenticador.
        
        Args:
            base_url: URL base da API
            empresa: Código da empresa
            username: Nome do usuário
            password: Senha do usuário
            id_integrador: ID do integrador (opcional)
        """
        self.base_url = base_url.rstrip('/')
        self.empresa = empresa
        self.username = username
        self.password = password
        self.id_integrador = id_integrador
        self._token: Optional[str] = None
    
    def authenticate(self) -> str:
        """
        Realiza autenticação e retorna o token Bearer.
        """
        url = f"{self.base_url}{self.TOKEN_ENDPOINT}"
        
        payload = {
            "empresa": self.empresa,
            "nomeUsuario": self.username,
            "senha": self.password
        }
        
        if self.id_integrador:
            payload["idIntegrador"] = self.id_integrador
        
        try:
            response = requests.post(url, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            self._token = data.get("token")
            if not self._token:
                raise AuthenticationError("Token não encontrado na resposta")
            
            return self._token
        except requests.exceptions.RequestException as e:
            raise AuthenticationError(f"Erro na autenticação: {str(e)}")

    @property
    def token(self) -> str:
        """Retorna o token atual ou realiza nova autenticação."""
        if not self._token:
            return self.authenticate()
        return self._token

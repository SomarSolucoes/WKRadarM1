"""Cliente principal da biblioteca WKRadarM1."""

import requests
import time
from typing import Optional, Dict, Any, List
from .auth import Authenticator
from .exceptions import (
    WKRadarError,
    AuthenticationError,
    PermissionError,
    NotFoundError,
    RateLimitError,
    ValidationError,
    BusinessError
)
from .endpoints import (
    Comercial,
    Compras,
    Contabil,
    Empresarial,
    Estoque,
    Financeiro,
    Folha,
    Gerenciador,
    Producao
)


class WKRadarClient:
    """
    Cliente principal para integração com o WK Radar.
    """
    
    def __init__(self, base_url: str, empresa: str, username: str, password: str, 
                 id_integrador: Optional[str] = None, max_retries: int = 3):
        """
        Inicializa o cliente WK Radar.
        """
        self.base_url = base_url.rstrip('/')
        self.authenticator = Authenticator(
            base_url=self.base_url,
            empresa=empresa,
            username=username,
            password=password,
            id_integrador=id_integrador
        )
        self.max_retries = max_retries
        self.session = requests.Session()
        
        # Inicializa módulos
        self.comercial = Comercial(self)
        self.compras = Compras(self)
        self.contabil = Contabil(self)
        self.empresarial = Empresarial(self)
        self.estoque = Estoque(self)
        self.financeiro = Financeiro(self)
        self.folha = Folha(self)
        self.gerenciador = Gerenciador(self)
        self.producao = Producao(self)

    def _request(self, method: str, path: str, **kwargs) -> Any:
        """
        Realiza uma requisição HTTP para a API.
        """
        url = f"{self.base_url}{path}"
        headers = kwargs.pop('headers', {})
        headers['Authorization'] = f"Bearer {self.authenticator.token}"
        headers['Content-Type'] = 'application/json'
        
        retries = 0
        while retries <= self.max_retries:
            try:
                response = self.session.request(method, url, headers=headers, **kwargs)
                
                if response.status_code == 429:
                    # Rate limiting - aguarda 1 segundo e tenta novamente
                    time.sleep(1)
                    retries += 1
                    continue
                
                self._handle_response_errors(response)
                
                if response.status_code == 204:
                    return None
                
                return response.json()
            
            except requests.exceptions.RequestException as e:
                if retries == self.max_retries:
                    raise WKRadarError(f"Erro na requisição após {self.max_retries} tentativas: {str(e)}")
                retries += 1
                time.sleep(1)

    def _handle_response_errors(self, response: requests.Response):
        """Trata erros comuns da API."""
        if response.status_code >= 400:
            try:
                data = response.json()
                message = data.get('message', response.text)
            except:
                message = response.text

            if response.status_code == 400:
                raise ValidationError(message)
            elif response.status_code == 401:
                raise AuthenticationError(message)
            elif response.status_code == 403:
                raise PermissionError(message)
            elif response.status_code == 404:
                raise NotFoundError(message)
            elif response.status_code == 422:
                raise BusinessError(message)
            elif response.status_code == 429:
                raise RateLimitError(message)
            else:
                raise WKRadarError(f"Erro {response.status_code}: {message}")

    def get(self, path: str, params: Optional[Dict] = None, **kwargs):
        return self._request('GET', path, params=params, **kwargs)

    def post(self, path: str, json: Optional[Any] = None, **kwargs):
        return self._request('POST', path, json=json, **kwargs)

    def patch(self, path: str, json: Optional[Any] = None, **kwargs):
        return self._request('PATCH', path, json=json, **kwargs)

    def put(self, path: str, json: Optional[Any] = None, **kwargs):
        return self._request('PUT', path, json=json, **kwargs)

    def delete(self, path: str, **kwargs):
        return self._request('DELETE', path, **kwargs)

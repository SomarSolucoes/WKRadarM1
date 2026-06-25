"""Módulo Estoque da API WK Radar."""

from .base import BaseEndpoint
from typing import List, Optional, Dict, Any


class Estoque(BaseEndpoint):
    """Endpoints do módulo Estoque."""

    def obter_local_de_armazenagem(self, id: str) -> Any:
        """Leitura de Local de Armazenagem pelo ID"""
        params = {}
        return self.client.get(f"/api/estoque/v1/local-armazenagem/{id}", params=params)

    def buscar_locais_de_armazenagem(self, Codigo: Optional[str] = None, IdFilial: Optional[str] = None, Tipo: Optional[Any] = None, TipoEstocagem: Optional[List[Any]] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Locais de Armazenagem"""
        params = self._format_filters(Codigo=Codigo, IdFilial=IdFilial, Tipo=Tipo, TipoEstocagem=TipoEstocagem, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/estoque/v1/local-armazenagem", params=params)

    def criar_movimentos_de_estoque_transferencia_entre_locais(self, dados: Any, **kwargs) -> Any:
        """Gravação de Movimentos de Estoque - Transferência entre Locais"""
        return self.client.post(f"/api/estoque/v1/movimento-estoque/transferencia-locais", json=dados, **kwargs)

    def criar_movimentos_de_estoque_saida(self, dados: Any, **kwargs) -> Any:
        """Gravação de Movimentos de Estoque - Saída"""
        return self.client.post(f"/api/estoque/v1/movimento-estoque/saida", json=dados, **kwargs)

    def criar_movimentos_de_estoque_entrada(self, dados: Any, **kwargs) -> Any:
        """Gravação de Movimentos de Estoque - Entrada"""
        return self.client.post(f"/api/estoque/v1/movimento-estoque/entrada", json=dados, **kwargs)

    def criar_movimentos_de_estoque_ajuste_automatico_de_inventario(self, dados: Any, **kwargs) -> Any:
        """Gravação de Movimentos de Estoque - Ajuste Automático de Inventário"""
        return self.client.post(f"/api/estoque/v1/movimento-estoque/ajuste-inventario", json=dados, **kwargs)

    def obter_movimento_de_estoque(self, id: str) -> Any:
        """Leitura de Movimento de Estoque pelo ID"""
        params = {}
        return self.client.get(f"/api/estoque/v1/movimento-estoque/{id}", params=params)

    def buscar_movimentos_de_estoque(self, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, DataHoraBaseAlteracao: Optional[str] = None, TipoEstoque: Optional[List[Any]] = None, Origem: Optional[List[Any]] = None, Operacao: Optional[List[Any]] = None, IdFilial: Optional[str] = None, IdLocal: Optional[str] = None, IdLocalDestino: Optional[str] = None, NumeroDocumento: Optional[str] = None, Produtos: Optional[List[Any]] = None, NumeroLote: Optional[str] = None, Volume: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Movimentos de Estoque"""
        params = self._format_filters(DataInicial=DataInicial, DataFinal=DataFinal, DataHoraBaseAlteracao=DataHoraBaseAlteracao, TipoEstoque=TipoEstoque, Origem=Origem, Operacao=Operacao, IdFilial=IdFilial, IdLocal=IdLocal, IdLocalDestino=IdLocalDestino, NumeroDocumento=NumeroDocumento, Produtos=Produtos, NumeroLote=NumeroLote, Volume=Volume, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/estoque/v1/movimento-estoque", params=params)

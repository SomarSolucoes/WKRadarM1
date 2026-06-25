"""Módulo Contabil da API WK Radar."""

from .base import BaseEndpoint
from typing import List, Optional, Dict, Any


class Contabil(BaseEndpoint):
    """Endpoints do módulo Contabil."""

    def obter_lancamentos_contabeis(self, id: str) -> Any:
        """Leitura de Lançamentos Contábeis pelo ID"""
        params = {}
        return self.client.get(f"/api/contabil/v1/lancamento-contabil/{id}", params=params)

    def atualizar_lancamento_contabil(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de Lançamento Contábil"""
        return self.client.patch(f"/api/contabil/v1/lancamento-contabil/{id}", json=dados, **kwargs)

    def excluir_lancamento_contabil(self, id: str, **kwargs) -> Any:
        """Exclusão de Lançamento Contábil"""
        return self.client.delete(f"/api/contabil/v1/lancamento-contabil/{id}", **kwargs)

    def busca_dos_lancamentos_contabeis(self, IdInicial: Optional[str] = None, IdFinal: Optional[str] = None, IdFilial: Optional[str] = None, IdContaContabil: Optional[str] = None, IdHistorico: Optional[str] = None, Complemento: Optional[str] = None, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, DocumentoInicial: Optional[int] = None, DocumentoFinal: Optional[int] = None, GrupoHistorico: Optional[bool] = None, TipoConferido: Optional[Any] = None, OrigemLancamento: Optional[List[Any]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca dos Lançamentos Contábeis"""
        params = self._format_filters(IdInicial=IdInicial, IdFinal=IdFinal, IdFilial=IdFilial, IdContaContabil=IdContaContabil, IdHistorico=IdHistorico, Complemento=Complemento, DataInicial=DataInicial, DataFinal=DataFinal, DocumentoInicial=DocumentoInicial, DocumentoFinal=DocumentoFinal, GrupoHistorico=GrupoHistorico, TipoConferido=TipoConferido, OrigemLancamento=OrigemLancamento, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/contabil/v1/lancamento-contabil", params=params)

    def criar_lancamentos_contabeis(self, dados: Any, **kwargs) -> Any:
        """Gravação de Lançamentos Contábeis"""
        return self.client.post(f"/api/contabil/v1/lancamento-contabil", json=dados, **kwargs)

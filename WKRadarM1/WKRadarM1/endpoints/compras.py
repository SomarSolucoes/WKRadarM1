"""Módulo Compras da API WK Radar."""

from .base import BaseEndpoint
from typing import List, Optional, Dict, Any


class Compras(BaseEndpoint):
    """Endpoints do módulo Compras."""

    def criar_cotacoes(self, dados: Any, **kwargs) -> Any:
        """Gravação de Cotações"""
        return self.client.post(f"/api/compras/v1/cotacao", json=dados, **kwargs)

    def buscar_cotacoes(self, ChaveSolicitacao: Optional[str] = None, Codigo: Optional[str] = None, IdFornecedor: Optional[str] = None, IdFilial: Optional[str] = None, DataCotacaoInicial: Optional[str] = None, DataCotacaoFinal: Optional[str] = None, DataHoraBaseAlteracao: Optional[str] = None, ProdutosServicos: Optional[List[Any]] = None, IdClassificacao: Optional[str] = None, IdGerencial: Optional[str] = None, IdRequisitante: Optional[str] = None, IdDepartamento: Optional[str] = None, IdComprador: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Cotações"""
        params = self._format_filters(ChaveSolicitacao=ChaveSolicitacao, Codigo=Codigo, IdFornecedor=IdFornecedor, IdFilial=IdFilial, DataCotacaoInicial=DataCotacaoInicial, DataCotacaoFinal=DataCotacaoFinal, DataHoraBaseAlteracao=DataHoraBaseAlteracao, ProdutosServicos=ProdutosServicos, IdClassificacao=IdClassificacao, IdGerencial=IdGerencial, IdRequisitante=IdRequisitante, IdDepartamento=IdDepartamento, IdComprador=IdComprador, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/compras/v1/cotacao", params=params)

    def obter_cotacoes(self, id: str) -> Any:
        """Leitura de Cotações pelo ID"""
        params = {}
        return self.client.get(f"/api/compras/v1/cotacao/{id}", params=params)

    def excluir_cotacao(self, id: str, **kwargs) -> Any:
        """Exclusão de Cotação pelo ID"""
        return self.client.delete(f"/api/compras/v1/cotacao/{id}", **kwargs)

    def criar_ordens_de_compra(self, dados: Any, **kwargs) -> Any:
        """Gravação de Ordens de Compra"""
        return self.client.post(f"/api/compras/v1/ordem-compra", json=dados, **kwargs)

    def buscar_ordens_de_compra(self, IdFornecedorTransportador: Optional[str] = None, IdEmpresaFilialFaturamento: Optional[str] = None, DataEmissaoInicial: Optional[str] = None, DataEmissaoFinal: Optional[str] = None, DataHoraBaseAlteracao: Optional[str] = None, Codigo: Optional[str] = None, Produtos: Optional[List[Any]] = None, Servicos: Optional[List[Any]] = None, IdClassificacao: Optional[str] = None, IdGerencial: Optional[str] = None, IdRequisitante: Optional[str] = None, IdDepartamento: Optional[str] = None, IdComprador: Optional[str] = None, SituacaoAutorizacao: Optional[Any] = None, NaDataInformada: Optional[str] = None, SituacaoAtendimento: Optional[Any] = None, SituacaoIntegracao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Ordens de Compra"""
        params = self._format_filters(IdFornecedorTransportador=IdFornecedorTransportador, IdEmpresaFilialFaturamento=IdEmpresaFilialFaturamento, DataEmissaoInicial=DataEmissaoInicial, DataEmissaoFinal=DataEmissaoFinal, DataHoraBaseAlteracao=DataHoraBaseAlteracao, Codigo=Codigo, Produtos=Produtos, Servicos=Servicos, IdClassificacao=IdClassificacao, IdGerencial=IdGerencial, IdRequisitante=IdRequisitante, IdDepartamento=IdDepartamento, IdComprador=IdComprador, SituacaoAutorizacao=SituacaoAutorizacao, NaDataInformada=NaDataInformada, SituacaoAtendimento=SituacaoAtendimento, SituacaoIntegracao=SituacaoIntegracao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/compras/v1/ordem-compra", params=params)

    def obter_ordens_de_compra(self, id: str) -> Any:
        """Leitura de Ordens de Compra pelo ID"""
        params = {}
        return self.client.get(f"/api/compras/v1/ordem-compra/{id}", params=params)

    def excluir_ordem_de_compra(self, id: str, **kwargs) -> Any:
        """Exclusão de Ordem de Compra pelo ID"""
        return self.client.delete(f"/api/compras/v1/ordem-compra/{id}", **kwargs)

    def cancela_a_ordem_de_compra(self, id: str, dados: Any, **kwargs) -> Any:
        """Cancela a Ordem de Compra pelo ID"""
        return self.client.post(f"/api/compras/v1/ordem-compra/{id}/cancelar", json=dados, **kwargs)

    def desfaz_o_cancelamento_da_ordem_de_compra(self, id: str, **kwargs) -> Any:
        """Desfaz o cancelamento da Ordem de Compra pelo ID"""
        return self.client.post(f"/api/compras/v1/ordem-compra/{id}/desfazer-cancelamento", **kwargs)

    def obter_pre_registro_de_notas(self, id: str) -> Any:
        """Leitura de Pré-registro de Notas pelo ID"""
        params = {}
        return self.client.get(f"/api/compras/v1/pre-registro-notas/{id}", params=params)

    def buscar_pre_registros_de_notas(self, Codigo: Optional[str] = None, IdFilial: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Pré-registros de Notas"""
        params = self._format_filters(Codigo=Codigo, IdFilial=IdFilial, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/compras/v1/pre-registro-notas", params=params)

    def criar_registros_de_entrada(self, dados: Any, **kwargs) -> Any:
        """Gravação de registros de entrada"""
        return self.client.post(f"/api/compras/v1/registro-entrada", json=dados, **kwargs)

    def buscar_registros_de_entrada(self, IdFornecedor: Optional[str] = None, IdFilial: Optional[str] = None, IdOrdemCompra: Optional[str] = None, DataEmissaoInicial: Optional[str] = None, DataEmissaoFinal: Optional[str] = None, DataEntradaInicial: Optional[str] = None, DataEntradaFinal: Optional[str] = None, DataHoraBaseAlteracao: Optional[str] = None, NumeroDocumento: Optional[str] = None, Itens: Optional[List[Any]] = None, IdClassificacao: Optional[str] = None, IdGerencial: Optional[str] = None, IdRequisitante: Optional[str] = None, IdDepartamento: Optional[str] = None, IdComprador: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Registros de Entrada"""
        params = self._format_filters(IdFornecedor=IdFornecedor, IdFilial=IdFilial, IdOrdemCompra=IdOrdemCompra, DataEmissaoInicial=DataEmissaoInicial, DataEmissaoFinal=DataEmissaoFinal, DataEntradaInicial=DataEntradaInicial, DataEntradaFinal=DataEntradaFinal, DataHoraBaseAlteracao=DataHoraBaseAlteracao, NumeroDocumento=NumeroDocumento, Itens=Itens, IdClassificacao=IdClassificacao, IdGerencial=IdGerencial, IdRequisitante=IdRequisitante, IdDepartamento=IdDepartamento, IdComprador=IdComprador, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/compras/v1/registro-entrada", params=params)

    def obter_registros_de_entrada(self, id: str) -> Any:
        """Leitura de Registros de Entrada pelo ID"""
        params = {}
        return self.client.get(f"/api/compras/v1/registro-entrada/{id}", params=params)

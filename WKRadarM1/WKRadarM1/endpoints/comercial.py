"""Módulo Comercial da API WK Radar."""

from .base import BaseEndpoint
from typing import List, Optional, Dict, Any


class Comercial(BaseEndpoint):
    """Endpoints do módulo Comercial."""

    def leitura_do_acompanhamento_de_pedidos_fluxos(self, id: str) -> Any:
        """Leitura do Acompanhamento de Pedidos - Fluxos pelo ID"""
        params = {}
        return self.client.get(f"/api/comercial/v1/acompanhamento-pedido-fluxo/{id}", params=params)

    def buscar_acompanhamento_de_pedidos_fluxos(self, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Acompanhamento de Pedidos - Fluxos"""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/comercial/v1/acompanhamento-pedido-fluxo", params=params)

    def leitura_do_acompanhamento_de_pedidos_processos(self, id: str) -> Any:
        """Leitura do Acompanhamento de Pedidos - Processos pelo ID"""
        params = {}
        return self.client.get(f"/api/comercial/v1/acompanhamento-pedido-processo/{id}", params=params)

    def buscar_acompanhamento_de_pedidos_processos(self, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Acompanhamento de Pedidos - Processos"""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/comercial/v1/acompanhamento-pedido-processo", params=params)

    def leitura_do_acompanhamento_de_pedidos_situacoes(self, id: str) -> Any:
        """Leitura do Acompanhamento de Pedidos - Situações pelo ID"""
        params = {}
        return self.client.get(f"/api/comercial/v1/acompanhamento-pedido-situacao/{id}", params=params)

    def buscar_acompanhamento_de_pedidos_situacoes(self, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Acompanhamento de Pedidos - Situações"""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/comercial/v1/acompanhamento-pedido-situacao", params=params)

    def criar_notas_fiscais(self, dados: Any, **kwargs) -> Any:
        """Gravação de Notas Fiscais"""
        return self.client.post(f"/api/comercial/v1/nota-fiscal", json=dados, **kwargs)

    def buscar_notas_fiscais(self, DataEmissaoInicial: Optional[str] = None, DataEmissaoFinal: Optional[str] = None, NumeroInicial: Optional[int] = None, NumeroFinal: Optional[int] = None, ValorTotalInicial: Optional[float] = None, ValorTotalFinal: Optional[float] = None, NumeroNfseInicial: Optional[int] = None, NumeroNfseFinal: Optional[int] = None, ChaveAcessoNfse: Optional[str] = None, ChaveAcessoNfe: Optional[str] = None, CodigoPedido: Optional[str] = None, CodigoRastreio: Optional[str] = None, IdFilial: Optional[str] = None, IdClientesFornecedores: Optional[List[str]] = None, IdVendedores: Optional[List[str]] = None, IdRepresentantes: Optional[List[str]] = None, IdTransportadoras: Optional[List[str]] = None, Produtos: Optional[List[Any]] = None, IdServico: Optional[str] = None, IdNaturezaOperacaoProdutos: Optional[List[str]] = None, IdNaturezaOperacaoServicos: Optional[List[str]] = None, Tipos: Optional[List[Any]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Notas Fiscais"""
        params = self._format_filters(DataEmissaoInicial=DataEmissaoInicial, DataEmissaoFinal=DataEmissaoFinal, NumeroInicial=NumeroInicial, NumeroFinal=NumeroFinal, ValorTotalInicial=ValorTotalInicial, ValorTotalFinal=ValorTotalFinal, NumeroNfseInicial=NumeroNfseInicial, NumeroNfseFinal=NumeroNfseFinal, ChaveAcessoNfse=ChaveAcessoNfse, ChaveAcessoNfe=ChaveAcessoNfe, CodigoPedido=CodigoPedido, CodigoRastreio=CodigoRastreio, IdFilial=IdFilial, IdClientesFornecedores=IdClientesFornecedores, IdVendedores=IdVendedores, IdRepresentantes=IdRepresentantes, IdTransportadoras=IdTransportadoras, Produtos=Produtos, IdServico=IdServico, IdNaturezaOperacaoProdutos=IdNaturezaOperacaoProdutos, IdNaturezaOperacaoServicos=IdNaturezaOperacaoServicos, Tipos=Tipos, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/comercial/v1/nota-fiscal", params=params)

    def obter_notas_fiscais(self, id: str) -> Any:
        """Leitura de Notas Fiscais pelo ID"""
        params = {}
        return self.client.get(f"/api/comercial/v1/nota-fiscal/{id}", params=params)

    def criar_pedidos(self, dados: Any, **kwargs) -> Any:
        """Gravação de Pedidos"""
        return self.client.post(f"/api/comercial/v1/pedido", json=dados, **kwargs)

    def buscar_pedidos(self, IdFilial: Optional[str] = None, Numero: Optional[str] = None, Codigo: Optional[str] = None, Situacoes: Optional[List[Any]] = None, SituacoesProducao: Optional[List[Any]] = None, Origem: Optional[List[Any]] = None, DataPedidoInicial: Optional[str] = None, DataPedidoFinal: Optional[str] = None, DataPedidoEntregaInicial: Optional[str] = None, DataPedidoEntregaFinal: Optional[str] = None, DataHoraBaseAlteracao: Optional[str] = None, IdCliente: Optional[str] = None, IdClientes: Optional[List[str]] = None, IdRepresentantes: Optional[List[str]] = None, IdVendedores: Optional[List[str]] = None, IdTransportadoras: Optional[List[str]] = None, Produtos: Optional[List[Any]] = None, IdServicos: Optional[List[str]] = None, IdNaturezaOperacaoProdutos: Optional[List[str]] = None, IdNaturezaOperacaoServicos: Optional[List[str]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Pedidos"""
        params = self._format_filters(IdFilial=IdFilial, Numero=Numero, Codigo=Codigo, Situacoes=Situacoes, SituacoesProducao=SituacoesProducao, Origem=Origem, DataPedidoInicial=DataPedidoInicial, DataPedidoFinal=DataPedidoFinal, DataPedidoEntregaInicial=DataPedidoEntregaInicial, DataPedidoEntregaFinal=DataPedidoEntregaFinal, DataHoraBaseAlteracao=DataHoraBaseAlteracao, IdCliente=IdCliente, IdClientes=IdClientes, IdRepresentantes=IdRepresentantes, IdVendedores=IdVendedores, IdTransportadoras=IdTransportadoras, Produtos=Produtos, IdServicos=IdServicos, IdNaturezaOperacaoProdutos=IdNaturezaOperacaoProdutos, IdNaturezaOperacaoServicos=IdNaturezaOperacaoServicos, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/comercial/v1/pedido", params=params)

    def pre_calculo_de_pedidos(self, dados: Any, **kwargs) -> Any:
        """Pré-Cálculo de Pedidos"""
        return self.client.post(f"/api/comercial/v1/pedido/precalculo", json=dados, **kwargs)

    def obter_pedidos(self, id: str) -> Any:
        """Leitura de Pedidos pelo ID"""
        params = {}
        return self.client.get(f"/api/comercial/v1/pedido/{id}", params=params)

    def cancelamento_de_pedidos(self, id: str, dados: Any, **kwargs) -> Any:
        """Cancelamento de Pedidos pelo ID"""
        return self.client.post(f"/api/comercial/v1/pedido/{id}/cancelar", json=dados, **kwargs)

    def alteracao_de_apontamentos_de_acompanhamentos_de_pedidos(self, id: str, dados: Any, **kwargs) -> Any:
        """Alteração de Apontamentos de Acompanhamentos de Pedidos"""
        return self.client.patch(f"/api/comercial/v1/pedido/{id}/acompanhamento", json=dados, **kwargs)

"""Módulo Financeiro da API WK Radar."""

from .base import BaseEndpoint
from typing import List, Optional, Dict, Any


class Financeiro(BaseEndpoint):
    """Endpoints do módulo Financeiro."""

    def obter_adiantamento(self, id: str) -> Any:
        """Leitura de Adiantamento pelo ID"""
        params = {}
        return self.client.get(f"/api/financeiro/v1/adiantamento/{id}", params=params)

    def buscar_adiantamentos(self, IdTesouraria: Optional[str] = None, IdEstornoVinculado: Optional[str] = None, IdTituloVinculado: Optional[str] = None, IdBaixaVinculada: Optional[str] = None, IdCFRT: Optional[str] = None, ValorAberto: Optional[float] = None, MesAnoInicial: Optional[str] = None, MesAnoFinal: Optional[str] = None, SomenteEmAberto: Optional[bool] = None, PossuiVinculoEstorno: Optional[bool] = None, PossuiVinculoBaixa: Optional[bool] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Adiantamentos"""
        params = self._format_filters(IdTesouraria=IdTesouraria, IdEstornoVinculado=IdEstornoVinculado, IdTituloVinculado=IdTituloVinculado, IdBaixaVinculada=IdBaixaVinculada, IdCFRT=IdCFRT, ValorAberto=ValorAberto, MesAnoInicial=MesAnoInicial, MesAnoFinal=MesAnoFinal, SomenteEmAberto=SomenteEmAberto, PossuiVinculoEstorno=PossuiVinculoEstorno, PossuiVinculoBaixa=PossuiVinculoBaixa, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/financeiro/v1/adiantamento", params=params)

    def criar_baixas_de_contas_a_pagar(self, dados: Any, **kwargs) -> Any:
        """Gravação de Baixas de Contas a Pagar"""
        return self.client.post(f"/api/financeiro/v1/baixa-contas-pagar", json=dados, **kwargs)

    def buscar_baixas_de_contas_a_pagar(self, IdCedente: Optional[str] = None, IdTitulo: Optional[str] = None, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, TipoData: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Baixas de Contas a Pagar"""
        params = self._format_filters(IdCedente=IdCedente, IdTitulo=IdTitulo, DataInicial=DataInicial, DataFinal=DataFinal, TipoData=TipoData, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/financeiro/v1/baixa-contas-pagar", params=params)

    def obter_baixa_de_contas_a_pagar(self, id: str) -> Any:
        """Leitura de Baixa de Contas a Pagar pelo ID"""
        params = {}
        return self.client.get(f"/api/financeiro/v1/baixa-contas-pagar/{id}", params=params)

    def excluir_baixa_de_contas_a_pagar(self, id: str, **kwargs) -> Any:
        """Exclusão de Baixa de Contas a Pagar pelo ID"""
        return self.client.delete(f"/api/financeiro/v1/baixa-contas-pagar/{id}", **kwargs)

    def criar_baixas_de_substituicao_de_titulos_de_contas_a_pagar(self, dados: Any, **kwargs) -> Any:
        """Gravação de Baixas de Substituição de títulos de Contas a Pagar"""
        return self.client.post(f"/api/financeiro/v1/baixa-contas-pagar/substituicao", json=dados, **kwargs)

    def criar_baixas_de_contas_a_receber(self, dados: Any, **kwargs) -> Any:
        """Gravação de Baixas de Contas a Receber"""
        return self.client.post(f"/api/financeiro/v1/baixa-contas-receber", json=dados, **kwargs)

    def buscar_baixas_de_contas_a_receber(self, IdSacado: Optional[str] = None, IdTitulo: Optional[str] = None, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, TipoData: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Baixas de Contas a Receber"""
        params = self._format_filters(IdSacado=IdSacado, IdTitulo=IdTitulo, DataInicial=DataInicial, DataFinal=DataFinal, TipoData=TipoData, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/financeiro/v1/baixa-contas-receber", params=params)

    def obter_baixa_de_contas_a_receber(self, id: str) -> Any:
        """Leitura de Baixa de Contas a Receber pelo ID"""
        params = {}
        return self.client.get(f"/api/financeiro/v1/baixa-contas-receber/{id}", params=params)

    def excluir_baixa_de_contas_a_receber(self, id: str, **kwargs) -> Any:
        """Exclusão de Baixa de Contas a Receber pelo ID"""
        return self.client.delete(f"/api/financeiro/v1/baixa-contas-receber/{id}", **kwargs)

    def criar_baixas_de_substituicao_de_titulos_de_contas_a_receber(self, dados: Any, **kwargs) -> Any:
        """Gravação de Baixas de Substituição de títulos de Contas a Receber"""
        return self.client.post(f"/api/financeiro/v1/baixa-contas-receber/substituicao", json=dados, **kwargs)

    def obter_carteira_de_cobranca(self, id: str) -> Any:
        """Leitura de Carteira de Cobrança pelo ID"""
        params = {}
        return self.client.get(f"/api/financeiro/v1/carteira-cobranca/{id}", params=params)

    def buscar_carteiras_de_cobranca(self, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Carteiras de Cobrança"""
        params = self._format_filters(Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/financeiro/v1/carteira-cobranca", params=params)

    def obter_categoria_de_adiantamento(self, id: str) -> Any:
        """Leitura de Categoria de Adiantamento pelo ID"""
        params = {}
        return self.client.get(f"/api/financeiro/v1/categoria-adiantamento/{id}", params=params)

    def buscar_categorias_de_adiantamento(self, Codigo: Optional[str] = None, IdConta: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Categorias de Adiantamento"""
        params = self._format_filters(Codigo=Codigo, IdConta=IdConta, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/financeiro/v1/categoria-adiantamento", params=params)

    def criar_cobranca(self, dados: Any, **kwargs) -> Any:
        """Gravação de Cobrança"""
        return self.client.post(f"/api/financeiro/v1/cobranca", json=dados, **kwargs)

    def consulta_boleto_de_cobranca__do_titulo(self, IdTitulo: Optional[str] = None, FormatoNomePdf: Optional[str] = None, **outros_filtros) -> Any:
        """Consulta boleto de Cobrança pelo ID do Título."""
        params = self._format_filters(IdTitulo=IdTitulo, FormatoNomePdf=FormatoNomePdf, **outros_filtros)
        return self.client.get(f"/api/financeiro/v1/cobranca", params=params)

    def cancelamento_de_boleto_de_cobranca_online__do_titulo(self, id: str, **kwargs) -> Any:
        """Cancelamento de boleto de Cobrança Online pelo ID do Título"""
        return self.client.delete(f"/api/financeiro/v1/cobranca/{id}", **kwargs)

    def obter_instrucao_bancaria(self, id: str) -> Any:
        """Leitura de Instrução Bancária pelo ID"""
        params = {}
        return self.client.get(f"/api/financeiro/v1/instrucao-bancaria/{id}", params=params)

    def buscar_instrucoes_bancarias(self, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Instruções Bancárias"""
        params = self._format_filters(Codigo=Codigo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/financeiro/v1/instrucao-bancaria", params=params)

    def criar_instrucoes_bancarias(self, dados: Any, **kwargs) -> Any:
        """Gravação de Instruções Bancárias"""
        return self.client.post(f"/api/financeiro/v1/instrucao-bancaria", json=dados, **kwargs)

    def criar_lancamentos_de_tesourarias(self, dados: Any, **kwargs) -> Any:
        """Gravação de Lançamentos de Tesourarias"""
        return self.client.post(f"/api/financeiro/v1/tesouraria", json=dados, **kwargs)

    def buscar_lancamentos_de_tesouraria(self, Numero: Optional[str] = None, IdFormaPagamento: Optional[str] = None, IdContaEntradaSaida: Optional[str] = None, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, TipoData: Optional[Any] = None, TipoTransacao: Optional[Any] = None, ValorInicial: Optional[float] = None, ValorFinal: Optional[float] = None, IdClientesFornecedores: Optional[List[str]] = None, NFeEmitida: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Lançamentos de Tesouraria"""
        params = self._format_filters(Numero=Numero, IdFormaPagamento=IdFormaPagamento, IdContaEntradaSaida=IdContaEntradaSaida, DataInicial=DataInicial, DataFinal=DataFinal, TipoData=TipoData, TipoTransacao=TipoTransacao, ValorInicial=ValorInicial, ValorFinal=ValorFinal, IdClientesFornecedores=IdClientesFornecedores, NFeEmitida=NFeEmitida, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/financeiro/v1/tesouraria", params=params)

    def obter_lancamento_de_tesouraria(self, id: str) -> Any:
        """Leitura de Lançamento de Tesouraria pelo ID"""
        params = {}
        return self.client.get(f"/api/financeiro/v1/tesouraria/{id}", params=params)

    def atualizar_lancamentos_de_tesouraria(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de Lançamentos de Tesouraria"""
        return self.client.patch(f"/api/financeiro/v1/tesouraria/{id}", json=dados, **kwargs)

    def excluir_lancamento_de_tesouraria(self, id: str, **kwargs) -> Any:
        """Exclusão de Lançamento de Tesouraria"""
        return self.client.delete(f"/api/financeiro/v1/tesouraria/{id}", **kwargs)

    def criar_titulos_de_contas_a_pagar(self, dados: Any, **kwargs) -> Any:
        """Gravação de Títulos de Contas a Pagar"""
        return self.client.post(f"/api/financeiro/v1/titulo-contas-pagar", json=dados, **kwargs)

    def buscar_titulos_de_contas_a_pagar(self, IdCedente: Optional[str] = None, NumeroDocumento: Optional[str] = None, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, ValorInicial: Optional[float] = None, ValorFinal: Optional[float] = None, Situacao: Optional[List[Any]] = None, TipoData: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Títulos de Contas a Pagar"""
        params = self._format_filters(IdCedente=IdCedente, NumeroDocumento=NumeroDocumento, DataInicial=DataInicial, DataFinal=DataFinal, ValorInicial=ValorInicial, ValorFinal=ValorFinal, Situacao=Situacao, TipoData=TipoData, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/financeiro/v1/titulo-contas-pagar", params=params)

    def obter_titulo_de_contas_a_pagar(self, id: str) -> Any:
        """Leitura de Título de Contas a Pagar pelo ID"""
        params = {}
        return self.client.get(f"/api/financeiro/v1/titulo-contas-pagar/{id}", params=params)

    def atualizar_titulos_de_contas_a_pagar(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de Títulos de Contas a Pagar"""
        return self.client.patch(f"/api/financeiro/v1/titulo-contas-pagar/{id}", json=dados, **kwargs)

    def excluir_titulo_de_contas_a_pagar(self, id: str, **kwargs) -> Any:
        """Exclusão de Título de Contas a Pagar pelo ID"""
        return self.client.delete(f"/api/financeiro/v1/titulo-contas-pagar/{id}", **kwargs)

    def criar_titulos_de_contas_a_receber(self, dados: Any, **kwargs) -> Any:
        """Gravação de Títulos de Contas a Receber"""
        return self.client.post(f"/api/financeiro/v1/titulo-contas-receber", json=dados, **kwargs)

    def buscar_titulos_de_contas_a_receber(self, IdSacado: Optional[str] = None, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, NumeroDocumento: Optional[str] = None, ValorInicial: Optional[float] = None, ValorFinal: Optional[float] = None, Situacao: Optional[List[Any]] = None, TipoData: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Títulos de Contas a Receber"""
        params = self._format_filters(IdSacado=IdSacado, DataInicial=DataInicial, DataFinal=DataFinal, NumeroDocumento=NumeroDocumento, ValorInicial=ValorInicial, ValorFinal=ValorFinal, Situacao=Situacao, TipoData=TipoData, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/financeiro/v1/titulo-contas-receber", params=params)

    def obter_titulo_de_contas_a_receber(self, id: str) -> Any:
        """Leitura de Título de Contas a Receber pelo ID"""
        params = {}
        return self.client.get(f"/api/financeiro/v1/titulo-contas-receber/{id}", params=params)

    def atualizar_titulos_de_contas_a_receber(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de Títulos de Contas a Receber"""
        return self.client.patch(f"/api/financeiro/v1/titulo-contas-receber/{id}", json=dados, **kwargs)

    def excluir_titulo_de_contas_a_receber(self, id: str, **kwargs) -> Any:
        """Exclusão de Título de Contas a Receber pelo ID"""
        return self.client.delete(f"/api/financeiro/v1/titulo-contas-receber/{id}", **kwargs)

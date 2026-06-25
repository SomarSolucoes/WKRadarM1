"""Módulo Gerenciador da API WK Radar."""

from .base import BaseEndpoint
from typing import List, Optional, Dict, Any


class Gerenciador(BaseEndpoint):
    """Endpoints do módulo Gerenciador."""

    def criar_contratos(self, dados: Any, **kwargs) -> Any:
        """Gravação de Contratos"""
        return self.client.post(f"/api/gerenciador/v1/contrato", json=dados, **kwargs)

    def buscar_contratos(self, Codigo: Optional[str] = None, Numero: Optional[str] = None, TipoContrato: Optional[Any] = None, SituacaoContrato: Optional[Any] = None, TipoRenovacao: Optional[Any] = None, DataContratoInicial: Optional[str] = None, DataContratoFinal: Optional[str] = None, DataAssinaturaInicial: Optional[str] = None, DataAssinaturaFinal: Optional[str] = None, DataSituacaoInicial: Optional[str] = None, DataSituacaoFinal: Optional[str] = None, DataFaturamentoInicial: Optional[str] = None, DataFaturamentoFinal: Optional[str] = None, Descricao: Optional[str] = None, ContratoOriginal: Optional[str] = None, IdFilial: Optional[str] = None, IdIndice: Optional[str] = None, IdCliente: Optional[str] = None, IdCliente2: Optional[str] = None, IdClassificacao: Optional[str] = None, IdGerencial: Optional[str] = None, IdServico: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Contratos"""
        params = self._format_filters(Codigo=Codigo, Numero=Numero, TipoContrato=TipoContrato, SituacaoContrato=SituacaoContrato, TipoRenovacao=TipoRenovacao, DataContratoInicial=DataContratoInicial, DataContratoFinal=DataContratoFinal, DataAssinaturaInicial=DataAssinaturaInicial, DataAssinaturaFinal=DataAssinaturaFinal, DataSituacaoInicial=DataSituacaoInicial, DataSituacaoFinal=DataSituacaoFinal, DataFaturamentoInicial=DataFaturamentoInicial, DataFaturamentoFinal=DataFaturamentoFinal, Descricao=Descricao, ContratoOriginal=ContratoOriginal, IdFilial=IdFilial, IdIndice=IdIndice, IdCliente=IdCliente, IdCliente2=IdCliente2, IdClassificacao=IdClassificacao, IdGerencial=IdGerencial, IdServico=IdServico, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/contrato", params=params)

    def obter_contrato(self, id: str) -> Any:
        """Leitura de Contrato pelo ID"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/contrato/{id}", params=params)

    def atualizar_contrato(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de Contrato"""
        return self.client.patch(f"/api/gerenciador/v1/contrato/{id}", json=dados, **kwargs)

    def excluir_contrato(self, id: str, **kwargs) -> Any:
        """Exclusão de Contrato pelo ID"""
        return self.client.delete(f"/api/gerenciador/v1/contrato/{id}", **kwargs)

    def criar_defeitos(self, dados: Any, **kwargs) -> Any:
        """Gravação de Defeitos"""
        return self.client.post(f"/api/gerenciador/v1/defeito", json=dados, **kwargs)

    def buscar_defeitos(self, Codigo: Optional[str] = None, Defeito: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Defeitos"""
        params = self._format_filters(Codigo=Codigo, Defeito=Defeito, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/defeito", params=params)

    def obter_defeito(self, id: str) -> Any:
        """Leitura de Defeito pelo ID"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/defeito/{id}", params=params)

    def criar_equipamentos(self, dados: Any, **kwargs) -> Any:
        """Gravação de Equipamentos"""
        return self.client.post(f"/api/gerenciador/v1/equipamento", json=dados, **kwargs)

    def buscar_equipamentos(self, Codigo: Optional[str] = None, Nome: Optional[str] = None, IdMarca: Optional[str] = None, IdModelo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Equipamentos"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, IdMarca=IdMarca, IdModelo=IdModelo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/equipamento", params=params)

    def obter_equipamento(self, id: str) -> Any:
        """Leitura de Equipamento pelo ID"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/equipamento/{id}", params=params)

    def buscar_eventos_do_contrato(self, IdContrato: Optional[str] = None, Descricao: Optional[str] = None, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, Origem: Optional[List[Any]] = None, IdsUsuario: Optional[List[str]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Eventos do Contrato"""
        params = self._format_filters(IdContrato=IdContrato, Descricao=Descricao, DataInicial=DataInicial, DataFinal=DataFinal, Origem=Origem, IdsUsuario=IdsUsuario, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/evento-contrato", params=params)

    def criar_faixas(self, dados: Any, **kwargs) -> Any:
        """Gravação de Faixas"""
        return self.client.post(f"/api/gerenciador/v1/faixa", json=dados, **kwargs)

    def buscar_faixas(self, Codigo: Optional[str] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Faixas"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/faixa", params=params)

    def obter_faixa(self, id: str) -> Any:
        """Leitura de Faixa pelo ID"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/faixa/{id}", params=params)

    def gerenciador_v1_incidencia_id(self, id: str) -> Any:
        """/api/gerenciador/v1/incidencia/{id}"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/incidencia/{id}", params=params)

    def gerenciador_v1_incidencia(self, Codigo: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """/api/gerenciador/v1/incidencia"""
        params = self._format_filters(Codigo=Codigo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/incidencia", params=params)

    def criar_marcas(self, dados: Any, **kwargs) -> Any:
        """Gravação de Marcas"""
        return self.client.post(f"/api/gerenciador/v1/marca", json=dados, **kwargs)

    def buscar_marcas(self, Codigo: Optional[str] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Marcas"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/marca", params=params)

    def obter_marca(self, id: str) -> Any:
        """Leitura de Marca pelo ID"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/marca/{id}", params=params)

    def criar_medicoes(self, dados: Any, **kwargs) -> Any:
        """Gravação de Medições"""
        return self.client.post(f"/api/gerenciador/v1/medicao", json=dados, **kwargs)

    def buscar_medicoes(self, MesAnoInicial: Optional[str] = None, MesAnoFinal: Optional[str] = None, DataMedicaoInicial: Optional[str] = None, DataMedicaoFinal: Optional[str] = None, IdFilial: Optional[str] = None, IdCliente: Optional[str] = None, IdContrato: Optional[str] = None, Numero: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Medições"""
        params = self._format_filters(MesAnoInicial=MesAnoInicial, MesAnoFinal=MesAnoFinal, DataMedicaoInicial=DataMedicaoInicial, DataMedicaoFinal=DataMedicaoFinal, IdFilial=IdFilial, IdCliente=IdCliente, IdContrato=IdContrato, Numero=Numero, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/medicao", params=params)

    def obter_medicao(self, id: str) -> Any:
        """Leitura de Medição pelo ID"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/medicao/{id}", params=params)

    def criar_modelos(self, dados: Any, **kwargs) -> Any:
        """Gravação de Modelos"""
        return self.client.post(f"/api/gerenciador/v1/modelo", json=dados, **kwargs)

    def buscar_modelos(self, Codigo: Optional[str] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Modelos"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/modelo", params=params)

    def obter_modelo(self, id: str) -> Any:
        """Leitura de Modelo pelo ID"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/modelo/{id}", params=params)

    def obter_projeto(self, id: str) -> Any:
        """Leitura de Projeto pelo ID"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/projeto/{id}", params=params)

    def buscar_projetos(self, Nome: Optional[str] = None, Codigo: Optional[str] = None, IdsCliente: Optional[List[str]] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Projetos"""
        params = self._format_filters(Nome=Nome, Codigo=Codigo, IdsCliente=IdsCliente, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/projeto", params=params)

    def criar_situacao_do_equipamento(self, dados: Any, **kwargs) -> Any:
        """Gravação de Situação do Equipamento"""
        return self.client.post(f"/api/gerenciador/v1/situacao-equipamento", json=dados, **kwargs)

    def buscar_situacoes_do_equipamento(self, Codigo: Optional[str] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Situações do Equipamento"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/situacao-equipamento", params=params)

    def obter_situacao_do_equipamento(self, id: str) -> Any:
        """Leitura de Situação do Equipamento pelo ID"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/situacao-equipamento/{id}", params=params)

    def criar_tipo(self, dados: Any, **kwargs) -> Any:
        """Gravação de Tipo"""
        return self.client.post(f"/api/gerenciador/v1/tipo", json=dados, **kwargs)

    def buscar_tipos(self, Codigo: Optional[str] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Tipos"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/gerenciador/v1/tipo", params=params)

    def obter_tipo(self, id: str) -> Any:
        """Leitura de Tipo pelo ID"""
        params = {}
        return self.client.get(f"/api/gerenciador/v1/tipo/{id}", params=params)

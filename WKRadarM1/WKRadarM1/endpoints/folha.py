"""Módulo Folha da API WK Radar."""

from .base import BaseEndpoint
from typing import List, Optional, Dict, Any


class Folha(BaseEndpoint):
    """Endpoints do módulo Folha."""

    def criar_admissoes_preliminares(self, dados: Any, **kwargs) -> Any:
        """Gravação de Admissões Preliminares"""
        return self.client.post(f"/api/folha/v1/admissao-preliminar", json=dados, **kwargs)

    def buscar_admissoes_preliminares(self, Codigo: Optional[int] = None, IdFilial: Optional[str] = None, DataAdmissaoInicial: Optional[str] = None, DataAdmissaoFinal: Optional[str] = None, CategoriaEsocial: Optional[Any] = None, TipoContrato: Optional[Any] = None, TipoExcluido: Optional[Any] = None, CPF: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Admissões Preliminares"""
        params = self._format_filters(Codigo=Codigo, IdFilial=IdFilial, DataAdmissaoInicial=DataAdmissaoInicial, DataAdmissaoFinal=DataAdmissaoFinal, CategoriaEsocial=CategoriaEsocial, TipoContrato=TipoContrato, TipoExcluido=TipoExcluido, CPF=CPF, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/admissao-preliminar", params=params)

    def obter_admissao_preliminar(self, id: str) -> Any:
        """Leitura de Admissão Preliminar pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/admissao-preliminar/{id}", params=params)

    def atualizar_admissao_preliminar(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de Admissão Preliminar"""
        return self.client.patch(f"/api/folha/v1/admissao-preliminar/{id}", json=dados, **kwargs)

    def exclusao_da_admissao_preliminar(self, id: str, **kwargs) -> Any:
        """Exclusão da Admissão Preliminar pelo ID"""
        return self.client.delete(f"/api/folha/v1/admissao-preliminar/{id}", **kwargs)

    def criar_afastamentos(self, dados: Any, **kwargs) -> Any:
        """Gravação de Afastamentos"""
        return self.client.post(f"/api/folha/v1/afastamento", json=dados, **kwargs)

    def buscar_afastamentos(self, IdEmpregado: Optional[str] = None, VigenciaInicio: Optional[str] = None, VigenciaTermino: Optional[str] = None, Situacoes: Optional[List[str]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Afastamentos"""
        params = self._format_filters(IdEmpregado=IdEmpregado, VigenciaInicio=VigenciaInicio, VigenciaTermino=VigenciaTermino, Situacoes=Situacoes, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/afastamento", params=params)

    def obter_afastamentos(self, id: str) -> Any:
        """Leitura de Afastamentos pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/afastamento/{id}", params=params)

    def exclusao_do_afastamento(self, id: str) -> Any:
        """Exclusão do Afastamento pelo ID"""
        return self.client.delete(f"/api/folha/v1/afastamento/{id}")

    def buscar_afastamentos_2(self, IdEmpregado: Optional[str] = None, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, TipoPeriodo: Optional[Any] = None, Situacao: Optional[Any] = None, Situacoes: Optional[List[str]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Afastamentos"""
        params = self._format_filters(IdEmpregado=IdEmpregado, DataInicial=DataInicial, DataFinal=DataFinal, TipoPeriodo=TipoPeriodo, Situacao=Situacao, Situacoes=Situacoes, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v2/afastamento", params=params)

    def obter_cargos_do_tipo_cargo(self, id: str) -> Any:
        """Leitura de Cargos do tipo cargo pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/cargo/{id}", params=params)

    def buscar_cargos_do_tipo_cargo(self, Codigo: Optional[str] = None, IdCbo: Optional[str] = None, Descricao: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Cargos do tipo cargo"""
        params = self._format_filters(Codigo=Codigo, IdCbo=IdCbo, Descricao=Descricao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/cargo", params=params)

    def obter_cbo(self, id: str) -> Any:
        """Leitura de CBO pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/cbo/{id}", params=params)

    def buscar_cbos(self, Codigo: Optional[str] = None, Tipo: Optional[Any] = None, Descricao: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de CBOs"""
        params = self._format_filters(Codigo=Codigo, Tipo=Tipo, Descricao=Descricao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/cbo", params=params)

    def obter_centro_de_custo_analitico(self, id: str) -> Any:
        """Leitura de Centro de Custo Analítico pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/centro-custo/{id}", params=params)

    def buscar_centros_de_custos_analiticos(self, Codigo: Optional[str] = None, Caracteristica: Optional[Any] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Centros de Custos Analíticos"""
        params = self._format_filters(Codigo=Codigo, Caracteristica=Caracteristica, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/centro-custo", params=params)

    def criar_conselhos(self, dados: Any, **kwargs) -> Any:
        """Gravação de Conselhos"""
        return self.client.post(f"/api/folha/v1/conselho", json=dados, **kwargs)

    def buscar_conselhos(self, Codigo: Optional[int] = None, Sigla: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Conselhos"""
        params = self._format_filters(Codigo=Codigo, Sigla=Sigla, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/conselho", params=params)

    def obter_conselho(self, id: str) -> Any:
        """Leitura de Conselho pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/conselho/{id}", params=params)

    def atualizar_conselho(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de Conselho"""
        return self.client.patch(f"/api/folha/v1/conselho/{id}", json=dados, **kwargs)

    def obter_departamentos(self, id: str) -> Any:
        """Leitura de Departamentos pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/departamento-folha/{id}", params=params)

    def buscar_departamento(self, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Departamento"""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/departamento-folha", params=params)

    def obter_empregado(self, id: str) -> Any:
        """Leitura de Empregado pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/empregado/{id}", params=params)

    def buscar_empregados(self, Nome: Optional[str] = None, Codigo: Optional[int] = None, IdFilial: Optional[str] = None, Cpf: Optional[str] = None, DataAdmissaoInicial: Optional[str] = None, DataAdmissaoFinal: Optional[str] = None, DataDemissaoInicial: Optional[str] = None, DataDemissaoFinal: Optional[str] = None, IdCargo: Optional[str] = None, IdDepartamento: Optional[str] = None, IdCentroCusto: Optional[str] = None, IdEscala: Optional[str] = None, IdSindicato: Optional[str] = None, TipoContrato: Optional[Any] = None, TipoExcluido: Optional[Any] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Empregados"""
        params = self._format_filters(Nome=Nome, Codigo=Codigo, IdFilial=IdFilial, Cpf=Cpf, DataAdmissaoInicial=DataAdmissaoInicial, DataAdmissaoFinal=DataAdmissaoFinal, DataDemissaoInicial=DataDemissaoInicial, DataDemissaoFinal=DataDemissaoFinal, IdCargo=IdCargo, IdDepartamento=IdDepartamento, IdCentroCusto=IdCentroCusto, IdEscala=IdEscala, IdSindicato=IdSindicato, TipoContrato=TipoContrato, TipoExcluido=TipoExcluido, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/empregado", params=params)

    def obter_escala(self, id: str) -> Any:
        """Leitura de Escala pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/escala-trabalho/{id}", params=params)

    def buscar_escalas(self, Codigo: Optional[int] = None, Descricao: Optional[str] = None, Turno: Optional[Any] = None, HorasMes: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Escalas"""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Turno=Turno, HorasMes=HorasMes, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/escala-trabalho", params=params)

    def obter_cargos_do_tipo_grupo(self, id: str) -> Any:
        """Leitura de cargos do tipo grupo pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/grupo-cargo/{id}", params=params)

    def buscar_cargos_do_tipo_grupo(self, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Cargos do tipo Grupo"""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/grupo-cargo", params=params)

    def obter_grupo_de_terceiro(self, id: str) -> Any:
        """Leitura de Grupo de Terceiro pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/grupo-terceiro/{id}", params=params)

    def buscar_grupo_de_terceiros(self, Codigo: Optional[int] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Grupo de Terceiros"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/grupo-terceiro", params=params)

    def obter_horario(self, id: str) -> Any:
        """Leitura de Horário pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/horario-trabalho/{id}", params=params)

    def buscar_horarios(self, Codigo: Optional[int] = None, Descricao: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Horários"""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/horario-trabalho", params=params)

    def obter_indice_fgts(self, id: str) -> Any:
        """Leitura de Índice FGTS pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/indice-fgts/{id}", params=params)

    def buscar_indices_fgts(self, CompetenciaInicial: Optional[str] = None, CompetenciaFinal: Optional[str] = None, Valor: Optional[float] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Índices FGTS"""
        params = self._format_filters(CompetenciaInicial=CompetenciaInicial, CompetenciaFinal=CompetenciaFinal, Valor=Valor, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/indice-fgts", params=params)

    def obter_rubrica(self, id: str) -> Any:
        """Leitura de Rubrica pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/rubrica/{id}", params=params)

    def buscar_rubricas(self, Codigo: Optional[int] = None, Descricao: Optional[str] = None, Situacao: Optional[Any] = None, Tipo: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Rubricas"""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Situacao=Situacao, Tipo=Tipo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/rubrica", params=params)

    def criar_rubricas_programadas(self, dados: Any, **kwargs) -> Any:
        """Gravação de Rubricas Programadas"""
        return self.client.post(f"/api/folha/v1/rubrica-programada", json=dados, **kwargs)

    def buscar_rubricas_programadas(self, VigenciaInicial: Optional[str] = None, VigenciaFinal: Optional[str] = None, IdEmpregado: Optional[str] = None, IdRubrica: Optional[str] = None, TipoFolha: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Rubricas Programadas"""
        params = self._format_filters(VigenciaInicial=VigenciaInicial, VigenciaFinal=VigenciaFinal, IdEmpregado=IdEmpregado, IdRubrica=IdRubrica, TipoFolha=TipoFolha, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/rubrica-programada", params=params)

    def obter_rubrica_programada(self, id: str) -> Any:
        """Leitura de Rubrica Programada pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/rubrica-programada/{id}", params=params)

    def exclusao_da_rubrica_programada(self, id: str, **kwargs) -> Any:
        """Exclusão da Rubrica Programada pelo ID"""
        return self.client.delete(f"/api/folha/v1/rubrica-programada/{id}", **kwargs)

    def leitura_do_salario_atual(self, id: str) -> Any:
        """Leitura do Salário Atual pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/salario-atual/{id}", params=params)

    def buscar_salarios_atuais(self, MotivoReajuste: Optional[Any] = None, TipoSalario: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Salários Atuais"""
        params = self._format_filters(MotivoReajuste=MotivoReajuste, TipoSalario=TipoSalario, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/salario-atual", params=params)

    def obter_sindicato_de_empregado(self, id: str) -> Any:
        """Leitura de Sindicato de Empregado pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/sindicato-empregado/{id}", params=params)

    def buscar_sindicatos_de_empregados(self, Nome: Optional[str] = None, Codigo: Optional[int] = None, EntidadeSindical: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Sindicatos de Empregados"""
        params = self._format_filters(Nome=Nome, Codigo=Codigo, EntidadeSindical=EntidadeSindical, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/sindicato-empregado", params=params)

    def obter_situacoes(self, id: str) -> Any:
        """Leitura de Situações pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/situacao/{id}", params=params)

    def buscar_situacoes(self, Codigo: Optional[int] = None, Descricao: Optional[str] = None, Tipos: Optional[List[Any]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Situações"""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Tipos=Tipos, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/situacao", params=params)

    def obter_terceiro(self, id: str) -> Any:
        """Leitura de Terceiro pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/terceiro/{id}", params=params)

    def buscar_terceiros(self, Codigo: Optional[int] = None, Caracteristica: Optional[Any] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Terceiros"""
        params = self._format_filters(Codigo=Codigo, Caracteristica=Caracteristica, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/terceiro", params=params)

    def obter_centro_de_custo_titulo(self, id: str) -> Any:
        """Leitura de Centro de Custo Título pelo ID"""
        params = {}
        return self.client.get(f"/api/folha/v1/titulo-centro-custo/{id}", params=params)

    def buscar_centros_de_custos_titulos(self, Codigo: Optional[str] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Centros de Custos Títulos"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/folha/v1/titulo-centro-custo", params=params)

"""Módulo Producao da API WK Radar."""

from .base import BaseEndpoint
from typing import List, Optional, Dict, Any


class Producao(BaseEndpoint):
    """Endpoints do módulo Producao."""

    def criar_apontamento_de_processo_final(self, dados: Any, **kwargs) -> Any:
        """Gravação de Apontamento de Processo Final"""
        return self.client.post(f"/api/producao/v1/apontamento/produto/processo-final", json=dados, **kwargs)

    def criar_apontamento_de_processo_intermediario(self, dados: Any, **kwargs) -> Any:
        """Gravação de Apontamento de Processo Intermediário"""
        return self.client.post(f"/api/producao/v1/apontamento/produto/processo-intermediario", json=dados, **kwargs)

    def obter_apontamento_efetuado(self, id: str) -> Any:
        """Leitura de Apontamento Efetuado pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/apontamento-efetuado/produto/{id}", params=params)

    def buscar_apontamentos_efetuados(self, InicioPeriodo: Optional[str] = None, FinalPeriodo: Optional[str] = None, Produtos: Optional[List[Any]] = None, IdsFilial: Optional[List[str]] = None, IdsHorario: Optional[List[str]] = None, IdsTipoOP: Optional[List[str]] = None, IdsFluxo: Optional[List[str]] = None, IdsProcesso: Optional[List[str]] = None, IdsOperacao: Optional[List[str]] = None, IdInfoSuplementar1: Optional[str] = None, IdInfoSuplementar2: Optional[str] = None, IdInfoSuplementar3: Optional[str] = None, IntegracaoPendente: Optional[bool] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Apontamentos Efetuados"""
        params = self._format_filters(InicioPeriodo=InicioPeriodo, FinalPeriodo=FinalPeriodo, Produtos=Produtos, IdsFilial=IdsFilial, IdsHorario=IdsHorario, IdsTipoOP=IdsTipoOP, IdsFluxo=IdsFluxo, IdsProcesso=IdsProcesso, IdsOperacao=IdsOperacao, IdInfoSuplementar1=IdInfoSuplementar1, IdInfoSuplementar2=IdInfoSuplementar2, IdInfoSuplementar3=IdInfoSuplementar3, IntegracaoPendente=IntegracaoPendente, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/apontamento-efetuado/produto", params=params)

    def leitura_do_cadastro_de_campos_personalizados_de_desenvolvimento_de_produtos_registro(self, id: str) -> Any:
        """Leitura do cadastro de Campos Personalizados de Desenvolvimento de Produtos - Registro pelo ID."""
        params = {}
        return self.client.get(f"/api/producao/v1/campos-personalizados/desenvolvimento-produto/registro/{id}", params=params)

    def buscar_campos_personalizados_de_desenvolvimento_de_produtos_registro(self, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Campos Personalizados de Desenvolvimento de Produtos - Registro."""
        params = self._format_filters(Codigo=Codigo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/campos-personalizados/desenvolvimento-produto/registro", params=params)

    def criar_desenvolvimentos_de_produto(self, dados: Any, **kwargs) -> Any:
        """Gravação de Desenvolvimentos de Produto"""
        return self.client.post(f"/api/producao/v1/desenvolvimento-produto", json=dados, **kwargs)

    def buscar_desenvolvimentos_de_produto(self, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, DataEntregaInicial: Optional[str] = None, DataEntregaFinal: Optional[str] = None, DataHoraAlteracaoEnsaiosSubmetidos: Optional[str] = None, DataHoraSituacaoSubmetido: Optional[str] = None, IdDesenvolvimentoPrincipal: Optional[str] = None, IdsCliente: Optional[List[str]] = None, IdsVendedor: Optional[List[str]] = None, IdsRepresentante: Optional[List[str]] = None, IdsEmpresasFilial: Optional[List[str]] = None, IdsProjetos: Optional[List[str]] = None, Produtos: Optional[List[Any]] = None, DesconsiderarProdutosSubordinados: Optional[bool] = None, Situacoes: Optional[List[Any]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Desenvolvimentos de Produto"""
        params = self._format_filters(DataInicial=DataInicial, DataFinal=DataFinal, DataEntregaInicial=DataEntregaInicial, DataEntregaFinal=DataEntregaFinal, DataHoraAlteracaoEnsaiosSubmetidos=DataHoraAlteracaoEnsaiosSubmetidos, DataHoraSituacaoSubmetido=DataHoraSituacaoSubmetido, IdDesenvolvimentoPrincipal=IdDesenvolvimentoPrincipal, IdsCliente=IdsCliente, IdsVendedor=IdsVendedor, IdsRepresentante=IdsRepresentante, IdsEmpresasFilial=IdsEmpresasFilial, IdsProjetos=IdsProjetos, Produtos=Produtos, DesconsiderarProdutosSubordinados=DesconsiderarProdutosSubordinados, Situacoes=Situacoes, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/desenvolvimento-produto", params=params)

    def obter_desenvolvimento_de_produto(self, id: str) -> Any:
        """Leitura de Desenvolvimento de Produto pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/desenvolvimento-produto/{id}", params=params)

    def obter_ensaio_de_produto(self, id: str) -> Any:
        """Leitura de Ensaio de Produto pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/ensaio-produto/{id}", params=params)

    def buscar_ensaios_de_produto(self, DataInicial: Optional[str] = None, DataFinal: Optional[str] = None, Situacoes: Optional[List[Any]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Ensaios de Produto"""
        params = self._format_filters(DataInicial=DataInicial, DataFinal=DataFinal, Situacoes=Situacoes, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/ensaio-produto", params=params)

    def obter_escala(self, id: str) -> Any:
        """Leitura de Escala pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/escala/{id}", params=params)

    def buscar_escalas(self, IdHorario: Optional[str] = None, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Escalas"""
        params = self._format_filters(IdHorario=IdHorario, Codigo=Codigo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/escala", params=params)

    def obter_fluxo_de_processo(self, id: str) -> Any:
        """Leitura de Fluxo de Processo pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/fluxo-processo/{id}", params=params)

    def buscar_fluxos_de_processo(self, Codigo: Optional[str] = None, IdTipoOrdemProducao: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Fluxos de Processo"""
        params = self._format_filters(Codigo=Codigo, IdTipoOrdemProducao=IdTipoOrdemProducao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/fluxo-processo", params=params)

    def obter_grupo_de_escala(self, id: str) -> Any:
        """Leitura de Grupo de Escala pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/grupo-escala/{id}", params=params)

    def buscar_grupos_de_escala(self, Codigo: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Grupos de Escala"""
        params = self._format_filters(Codigo=Codigo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/grupo-escala", params=params)

    def obter_grupo_de_horario(self, id: str) -> Any:
        """Leitura de Grupo de Horário pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/grupo-horario/{id}", params=params)

    def buscar_grupos_de_horario(self, Codigo: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Grupos de Horário"""
        params = self._format_filters(Codigo=Codigo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/grupo-horario", params=params)

    def leitura_do_grupo_de_motivos_de_perdas_ou_defeitos(self, id: str) -> Any:
        """Leitura do Grupo de Motivos de Perdas ou Defeitos pelo ID."""
        params = {}
        return self.client.get(f"/api/producao/v1/grupo-motivo-perda-defeito/{id}", params=params)

    def buscar_grupo_de_motivos_de_perdas_ou_defeitos(self, Codigo: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Grupo de Motivos de Perdas ou Defeitos."""
        params = self._format_filters(Codigo=Codigo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/grupo-motivo-perda-defeito", params=params)

    def obter_grupo_de_projeto(self, id: str) -> Any:
        """Leitura de Grupo de Projeto pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/grupo-projeto/{id}", params=params)

    def buscar_grupos_de_projeto(self, Codigo: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Grupos de Projeto"""
        params = self._format_filters(Codigo=Codigo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/grupo-projeto", params=params)

    def obter_horario(self, id: str) -> Any:
        """Leitura de Horário pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/horario/{id}", params=params)

    def buscar_horarios(self, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Horários"""
        params = self._format_filters(Codigo=Codigo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/horario", params=params)

    def obter_informacao_suplementar(self, id: str) -> Any:
        """Leitura de Informação Suplementar pelo ID."""
        params = {}
        return self.client.get(f"/api/producao/v1/informacao-suplementar/{id}", params=params)

    def buscar_informacao_suplementar(self, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Grupo: Optional[Any] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Informação Suplementar."""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Grupo=Grupo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/informacao-suplementar", params=params)

    def obter_motivos_de_perdas_ou_defeitos(self, id: str) -> Any:
        """Leitura de Motivos de Perdas ou Defeitos pelo ID."""
        params = {}
        return self.client.get(f"/api/producao/v1/motivo-perda-defeito/{id}", params=params)

    def busca_do_motivo_de_perdas_ou_defeitos(self, Codigo: Optional[str] = None, IdsProcesso: Optional[List[str]] = None, Situacao: Optional[Any] = None, Especie: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca do Motivo de Perdas ou Defeitos."""
        params = self._format_filters(Codigo=Codigo, IdsProcesso=IdsProcesso, Situacao=Situacao, Especie=Especie, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/motivo-perda-defeito", params=params)

    def obter_necessidade_de_producao(self, id: str) -> Any:
        """Leitura de Necessidade de Produção pelo ID."""
        params = {}
        return self.client.get(f"/api/producao/v1/necessidade-producao/{id}", params=params)

    def buscar_necessidades_de_producao(self, DataEmissaoInicial: Optional[str] = None, DataEmissaoFinal: Optional[str] = None, PrevisaoNecessidadeInicial: Optional[str] = None, PrevisaoNecessidadeFinal: Optional[str] = None, Origem: Optional[List[Any]] = None, Situacao: Optional[List[Any]] = None, Produtos: Optional[List[Any]] = None, DesconsiderarSubordinados: Optional[bool] = None, IdsEmpresaFilial: Optional[List[str]] = None, IdsProjeto: Optional[List[str]] = None, IdsCliente: Optional[List[str]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Necessidades de Produção."""
        params = self._format_filters(DataEmissaoInicial=DataEmissaoInicial, DataEmissaoFinal=DataEmissaoFinal, PrevisaoNecessidadeInicial=PrevisaoNecessidadeInicial, PrevisaoNecessidadeFinal=PrevisaoNecessidadeFinal, Origem=Origem, Situacao=Situacao, Produtos=Produtos, DesconsiderarSubordinados=DesconsiderarSubordinados, IdsEmpresaFilial=IdsEmpresaFilial, IdsProjeto=IdsProjeto, IdsCliente=IdsCliente, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/necessidade-producao", params=params)

    def obter_operacao_da_producao(self, id: str) -> Any:
        """Leitura de Operação da Produção pelo ID."""
        params = {}
        return self.client.get(f"/api/producao/v1/operacao-producao/{id}", params=params)

    def buscar_operacao_da_producao(self, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Operação da Produção."""
        params = self._format_filters(Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/operacao-producao", params=params)

    def criar_ordens_de_producao(self, dados: Any, **kwargs) -> Any:
        """Gravação de Ordens de Produção"""
        return self.client.post(f"/api/producao/v1/ordem-producao/produto", json=dados, **kwargs)

    def buscar_ordens_de_producao(self, TipoPeriodo: Optional[Any] = None, PeriodoDataInicial: Optional[str] = None, PeriodoDataFinal: Optional[str] = None, NumeroInicial: Optional[int] = None, NumeroFinal: Optional[int] = None, ChaveOrdemProducaoInicial: Optional[str] = None, ChaveOrdemProducaoFinal: Optional[str] = None, Produtos: Optional[List[Any]] = None, DesconsiderarProdutosSubordinados: Optional[bool] = None, Insumos: Optional[List[Any]] = None, DesconsiderarInsumosSubordinados: Optional[bool] = None, IdsFilial: Optional[List[str]] = None, IdsProjeto: Optional[List[str]] = None, IdsTipoOrdemProducao: Optional[List[str]] = None, IdsFluxo: Optional[List[str]] = None, IdsIndustrializador: Optional[List[str]] = None, IdsPedido: Optional[List[str]] = None, IdsCliente: Optional[List[str]] = None, Situacoes: Optional[List[Any]] = None, SituacoesImpressao: Optional[List[Any]] = None, TiposItemAtendimento: Optional[List[Any]] = None, IndustrializacaoParaTerceiro: Optional[bool] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Ordens de Produção"""
        params = self._format_filters(TipoPeriodo=TipoPeriodo, PeriodoDataInicial=PeriodoDataInicial, PeriodoDataFinal=PeriodoDataFinal, NumeroInicial=NumeroInicial, NumeroFinal=NumeroFinal, ChaveOrdemProducaoInicial=ChaveOrdemProducaoInicial, ChaveOrdemProducaoFinal=ChaveOrdemProducaoFinal, Produtos=Produtos, DesconsiderarProdutosSubordinados=DesconsiderarProdutosSubordinados, Insumos=Insumos, DesconsiderarInsumosSubordinados=DesconsiderarInsumosSubordinados, IdsFilial=IdsFilial, IdsProjeto=IdsProjeto, IdsTipoOrdemProducao=IdsTipoOrdemProducao, IdsFluxo=IdsFluxo, IdsIndustrializador=IdsIndustrializador, IdsPedido=IdsPedido, IdsCliente=IdsCliente, Situacoes=Situacoes, SituacoesImpressao=SituacoesImpressao, TiposItemAtendimento=TiposItemAtendimento, IndustrializacaoParaTerceiro=IndustrializacaoParaTerceiro, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/ordem-producao/produto", params=params)

    def obter_ordem_de_producao(self, id: str) -> Any:
        """Leitura de Ordem de Produção pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/ordem-producao/produto/{id}", params=params)

    def obter_processo(self, id: str) -> Any:
        """Leitura de Processo pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/processo/{id}", params=params)

    def buscar_processos(self, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Processos"""
        params = self._format_filters(Codigo=Codigo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/processo", params=params)

    def obter_projeto(self, id: str) -> Any:
        """Leitura de Projeto pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/projeto-producao/{id}", params=params)

    def buscar_projetos(self, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Projetos"""
        params = self._format_filters(Codigo=Codigo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/projeto-producao", params=params)

    def obter_tipo_de_ordem_de_producao(self, id: str) -> Any:
        """Leitura de Tipo de Ordem de Produção pelo ID"""
        params = {}
        return self.client.get(f"/api/producao/v1/tipo-ordem-producao/{id}", params=params)

    def buscar_tipos_de_ordem_de_producao(self, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Tipos de Ordem de Produção"""
        params = self._format_filters(Codigo=Codigo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/producao/v1/tipo-ordem-producao", params=params)

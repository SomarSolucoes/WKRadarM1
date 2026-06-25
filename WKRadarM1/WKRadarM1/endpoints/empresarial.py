"""Módulo Empresarial da API WK Radar."""

from .base import BaseEndpoint
from typing import List, Optional, Dict, Any


class Empresarial(BaseEndpoint):
    """Endpoints do módulo Empresarial."""

    def leitura_do_cadastro_de_info_plus(self, id: str) -> Any:
        """Leitura do cadastro de Info Plus pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/cadastro-info-plus/{id}", params=params)

    def busca_do_cadastro_de_info_plus(self, Processo: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca do cadastro de Info Plus"""
        params = self._format_filters(Processo=Processo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/cadastro-info-plus", params=params)

    def leitura_do_cadastro_de_categorias_de_cfrt(self, id: str) -> Any:
        """Leitura do cadastro de Categorias de CFRT pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/categoria-cfrt/{id}", params=params)

    def busca_do_cadastro_de_categorias_de_cfrt(self, Grupo: Optional[Any] = None, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca do cadastro de Categorias de CFRT"""
        params = self._format_filters(Grupo=Grupo, Codigo=Codigo, Descricao=Descricao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/categoria-cfrt", params=params)

    def leitura_do_cadastro_de_categorias_de_produto(self, id: str) -> Any:
        """Leitura do cadastro de Categorias de Produto pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/categoria-produto/{id}", params=params)

    def busca_do_cadastro_de_categorias_de_produto(self, Grupo: Optional[Any] = None, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca do cadastro de Categorias de Produto"""
        params = self._format_filters(Grupo=Grupo, Codigo=Codigo, Descricao=Descricao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/categoria-produto", params=params)

    def criar_clientes(self, dados: Any, **kwargs) -> Any:
        """Gravação de Clientes"""
        return self.client.post(f"/api/empresarial/v1/cliente", json=dados, **kwargs)

    def buscar_clientes(self, TipoPessoa: Optional[Any] = None, Situacao: Optional[Any] = None, RazaoSocial: Optional[str] = None, NomeFantasia: Optional[str] = None, Codigo: Optional[str] = None, IdVendedor: Optional[str] = None, IdRepresentante: Optional[str] = None, IdMunicipio: Optional[str] = None, UF: Optional[str] = None, DataHoraGravacaoInicial: Optional[str] = None, DataHoraGravacaoFinal: Optional[str] = None, CpfCnpj: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Clientes"""
        params = self._format_filters(TipoPessoa=TipoPessoa, Situacao=Situacao, RazaoSocial=RazaoSocial, NomeFantasia=NomeFantasia, Codigo=Codigo, IdVendedor=IdVendedor, IdRepresentante=IdRepresentante, IdMunicipio=IdMunicipio, UF=UF, DataHoraGravacaoInicial=DataHoraGravacaoInicial, DataHoraGravacaoFinal=DataHoraGravacaoFinal, CpfCnpj=CpfCnpj, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/cliente", params=params)

    def obter_cliente(self, id: str) -> Any:
        """Leitura de Cliente pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/cliente/{id}", params=params)

    def obter_comprador(self, id: str) -> Any:
        """Leitura de Comprador pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/comprador/{id}", params=params)

    def buscar_compradores(self, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, IdUsuario: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Compradores"""
        params = self._format_filters(Codigo=Codigo, Situacao=Situacao, IdUsuario=IdUsuario, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/comprador", params=params)

    def obter_condicao_de_pagamento(self, id: str) -> Any:
        """Leitura de Condição de Pagamento pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/condicao-pagamento/{id}", params=params)

    def buscar_condicoes_de_pagamento(self, Modulos: Optional[List[Any]] = None, Codigo: Optional[str] = None, Nome: Optional[str] = None, ValidadeInicial: Optional[str] = None, ValidadeFinal: Optional[str] = None, IdTipoPeriodo: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Condições de Pagamento"""
        params = self._format_filters(Modulos=Modulos, Codigo=Codigo, Nome=Nome, ValidadeInicial=ValidadeInicial, ValidadeFinal=ValidadeFinal, IdTipoPeriodo=IdTipoPeriodo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/condicao-pagamento", params=params)

    def obter_contato(self, id: str) -> Any:
        """Leitura de Contato pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/contato/{id}", params=params)

    def buscar_contatos(self, IdCFRT: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Contatos"""
        params = self._format_filters(IdCFRT=IdCFRT, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/contato", params=params)

    def obter_departamento(self, id: str) -> Any:
        """Leitura de Departamento pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/departamento/{id}", params=params)

    def buscar_departamentos(self, Nome: Optional[str] = None, IdFilial: Optional[str] = None, IdUsuario: Optional[str] = None, Ativo: Optional[bool] = None, ApenasFilialZero: Optional[bool] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Departamentos"""
        params = self._format_filters(Nome=Nome, IdFilial=IdFilial, IdUsuario=IdUsuario, Ativo=Ativo, ApenasFilialZero=ApenasFilialZero, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/departamento", params=params)

    def obter_documento(self, id: str) -> Any:
        """Leitura de Documento pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/documento/{id}", params=params)

    def buscar_documentos(self, Modulos: Optional[List[Any]] = None, IdFilial: Optional[str] = None, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Especie: Optional[str] = None, Serie: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Documentos"""
        params = self._format_filters(Modulos=Modulos, IdFilial=IdFilial, Codigo=Codigo, Descricao=Descricao, Especie=Especie, Serie=Serie, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/documento", params=params)

    def criar_estados(self, dados: Any, **kwargs) -> Any:
        """Gravação de Estados"""
        return self.client.post(f"/api/empresarial/v1/estado", json=dados, **kwargs)

    def buscar_estados(self, Nome: Optional[str] = None, SiglaUF: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Estados"""
        params = self._format_filters(Nome=Nome, SiglaUF=SiglaUF, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/estado", params=params)

    def obter_estado(self, id: str) -> Any:
        """Leitura de Estado pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/estado/{id}", params=params)

    def atualizar_estado(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de Estado"""
        return self.client.patch(f"/api/empresarial/v1/estado/{id}", json=dados, **kwargs)

    def obter_empresa_filial(self, id: str) -> Any:
        """Leitura de Empresa/Filial pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/filial/{id}", params=params)

    def buscar_empresas_filiais(self, CodigoInicial: Optional[int] = None, CodigoFinal: Optional[int] = None, Identificacao: Optional[str] = None, RazaoSocial: Optional[str] = None, CpfCnpj: Optional[str] = None, UF: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Empresas/Filiais"""
        params = self._format_filters(CodigoInicial=CodigoInicial, CodigoFinal=CodigoFinal, Identificacao=Identificacao, RazaoSocial=RazaoSocial, CpfCnpj=CpfCnpj, UF=UF, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/filial", params=params)

    def obter_forma_de_pagamento(self, id: str) -> Any:
        """Leitura de Forma de Pagamento pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/forma-pagamento/{id}", params=params)

    def buscar_formas_de_pagamento(self, Codigo: Optional[str] = None, BuscarApenasNFCe: Optional[bool] = None, Situacao: Optional[Any] = None, MeioPagamento: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Formas de Pagamento"""
        params = self._format_filters(Codigo=Codigo, BuscarApenasNFCe=BuscarApenasNFCe, Situacao=Situacao, MeioPagamento=MeioPagamento, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/forma-pagamento", params=params)

    def obter_fornecedor(self, id: str) -> Any:
        """Leitura de Fornecedor pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/fornecedor/{id}", params=params)

    def buscar_fornecedores(self, TipoPessoa: Optional[Any] = None, Situacao: Optional[Any] = None, RazaoSocial: Optional[str] = None, NomeFantasia: Optional[str] = None, Codigo: Optional[str] = None, IdMunicipio: Optional[str] = None, UF: Optional[str] = None, DataHoraGravacaoInicial: Optional[str] = None, DataHoraGravacaoFinal: Optional[str] = None, CpfCnpj: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Fornecedores"""
        params = self._format_filters(TipoPessoa=TipoPessoa, Situacao=Situacao, RazaoSocial=RazaoSocial, NomeFantasia=NomeFantasia, Codigo=Codigo, IdMunicipio=IdMunicipio, UF=UF, DataHoraGravacaoInicial=DataHoraGravacaoInicial, DataHoraGravacaoFinal=DataHoraGravacaoFinal, CpfCnpj=CpfCnpj, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/fornecedor", params=params)

    def obter_grade(self, id: str) -> Any:
        """Leitura de Grade pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/grade/{id}", params=params)

    def buscar_grades(self, Codigo: Optional[int] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Grades"""
        params = self._format_filters(Codigo=Codigo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/grade", params=params)

    def obter_grade_contabil(self, id: str) -> Any:
        """Leitura de grade contábil pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/grade-contabil/{id}", params=params)

    def buscar_grades_contabeis(self, Processo: Optional[Any] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de grades contábeis"""
        params = self._format_filters(Processo=Processo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/grade-contabil", params=params)

    def obter_grupo_de_natureza_efd_reinf(self, id: str) -> Any:
        """Leitura de Grupo de Natureza EFD Reinf pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/grupo-natureza-efd-reinf/{id}", params=params)

    def buscar_grupos_de_naturezas_efd_reinf(self, Codigo: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Grupos de Naturezas EFD Reinf"""
        params = self._format_filters(Codigo=Codigo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/grupo-natureza-efd-reinf", params=params)

    def obter_grupo_de_recurso(self, id: str) -> Any:
        """Leitura de Grupo de Recurso pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/grupo-recurso/{id}", params=params)

    def buscar_grupos_de_recursos(self, Codigo: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Grupos de Recursos"""
        params = self._format_filters(Codigo=Codigo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/grupo-recurso", params=params)

    def criar_historicos(self, dados: Any, **kwargs) -> Any:
        """Gravação de históricos"""
        return self.client.post(f"/api/empresarial/v1/historico", json=dados, **kwargs)

    def buscar_historicos(self, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Históricos"""
        params = self._format_filters(Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/historico", params=params)

    def obter_historico(self, id: str) -> Any:
        """Leitura de Histórico pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/historico/{id}", params=params)

    def importacao_de_cadastros_por(self, dados: Dict[str, Any], files: Optional[Dict[str, Any]] = None, **kwargs) -> Any:
        """Importação de cadastros por API"""
        return self.client._request("POST", f"/api/empresarial/v1/importacao", data=dados, files=files, **kwargs)

    def buscar_importacoes(self, IdImportacao: Optional[str] = None, NomeArquivo: Optional[str] = None, TipoImportacao: Optional[Any] = None, StatusImportacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Importações API"""
        params = self._format_filters(IdImportacao=IdImportacao, NomeArquivo=NomeArquivo, TipoImportacao=TipoImportacao, StatusImportacao=StatusImportacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/importacao", params=params)

    def obter_importacao(self, id: str) -> Any:
        """Leitura de Importação API pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/importacao/{id}", params=params)

    def criar_indices(self, dados: Any, **kwargs) -> Any:
        """Gravação de índices"""
        return self.client.post(f"/api/empresarial/v1/indice", json=dados, **kwargs)

    def buscar_indices(self, Nome: Optional[str] = None, DataValor: Optional[str] = None, Formato: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Índices"""
        params = self._format_filters(Nome=Nome, DataValor=DataValor, Formato=Formato, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/indice", params=params)

    def obter_indice(self, id: str) -> Any:
        """Leitura de Índice pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/indice/{id}", params=params)

    def atualizar_indice(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de índice"""
        return self.client.patch(f"/api/empresarial/v1/indice/{id}", json=dados, **kwargs)

    def leitura_do_cadastro_de_informacoes_bancarias_do_tipo_conta_bancaria(self, id: str) -> Any:
        """Leitura do cadastro de Informações Bancárias do tipo Conta Bancária pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/informacao-bancaria/{id}", params=params)

    def busca_do_cadastro_de_informacoes_bancarias_do_tipo_conta_bancaria(self, Codigo: Optional[str] = None, IdCFRT: Optional[str] = None, IdPortador: Optional[str] = None, TipoConta: Optional[Any] = None, ApenasContaPadrao: Optional[bool] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca do cadastro de Informações Bancárias do tipo Conta Bancária"""
        params = self._format_filters(Codigo=Codigo, IdCFRT=IdCFRT, IdPortador=IdPortador, TipoConta=TipoConta, ApenasContaPadrao=ApenasContaPadrao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/informacao-bancaria", params=params)

    def leitura_do_cadastro_de_informacoes_bancarias_do_tipo_pix(self, id: str) -> Any:
        """Leitura do cadastro de Informações Bancárias do tipo Pix pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/informacao-bancaria-pix/{id}", params=params)

    def busca_do_cadastro_de_informacoes_bancarias_do_tipo_pix(self, Codigo: Optional[str] = None, IdCFRT: Optional[str] = None, TipoChaveEnderecamento: Optional[Any] = None, ApenasContaPadrao: Optional[bool] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca do cadastro de Informações Bancárias do tipo Pix"""
        params = self._format_filters(Codigo=Codigo, IdCFRT=IdCFRT, TipoChaveEnderecamento=TipoChaveEnderecamento, ApenasContaPadrao=ApenasContaPadrao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/informacao-bancaria-pix", params=params)

    def leitura_do_cadastro_de_informacoes_complementares(self, id: str) -> Any:
        """Leitura do cadastro de Informações Complementares pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/informacao-complementar/{id}", params=params)

    def busca_do_cadastro_de_informacoes_complementares(self, Grupo: Optional[Any] = None, Situacao: Optional[Any] = None, Descricao: Optional[str] = None, Codigo: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca do cadastro de Informações Complementares"""
        params = self._format_filters(Grupo=Grupo, Situacao=Situacao, Descricao=Descricao, Codigo=Codigo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/informacao-complementar", params=params)

    def obter_itens_de_uma_grade(self, IdGrade: Optional[str] = None, SomenteInativos: Optional[bool] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Leitura de Itens de uma Grade"""
        params = self._format_filters(IdGrade=IdGrade, SomenteInativos=SomenteInativos, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/item-grade/grade", params=params)

    def obter_itens_de_grade_relacionados_a_um_produto(self, ProdutosItensGrade: Optional[List[Any]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Leitura de Itens de Grade relacionados a um Produto"""
        params = self._format_filters(ProdutosItensGrade=ProdutosItensGrade, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/item-grade/produto", params=params)

    def criar_mensagens(self, dados: Any, **kwargs) -> Any:
        """Gravação de Mensagens"""
        return self.client.post(f"/api/empresarial/v1/mensagem", json=dados, **kwargs)

    def buscar_mensagens(self, Codigo: Optional[str] = None, Modulo: Optional[Any] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Mensagens"""
        params = self._format_filters(Codigo=Codigo, Modulo=Modulo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/mensagem", params=params)

    def obter_mensagem(self, id: str) -> Any:
        """Leitura de Mensagem pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/mensagem/{id}", params=params)

    def atualizar_mensagem(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de Mensagem"""
        return self.client.patch(f"/api/empresarial/v1/mensagem/{id}", json=dados, **kwargs)

    def obter_motorista(self, id: str) -> Any:
        """Leitura de Motorista pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/motorista/{id}", params=params)

    def buscar_motoristas(self, Nome: Optional[str] = None, Cpf: Optional[str] = None, Rg: Optional[str] = None, Habilitacao: Optional[str] = None, Cnh: Optional[str] = None, IdVeiculo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Motoristas"""
        params = self._format_filters(Nome=Nome, Cpf=Cpf, Rg=Rg, Habilitacao=Habilitacao, Cnh=Cnh, IdVeiculo=IdVeiculo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/motorista", params=params)

    def criar_municipios(self, dados: Any, **kwargs) -> Any:
        """Gravação de Municípios"""
        return self.client.post(f"/api/empresarial/v1/municipio", json=dados, **kwargs)

    def buscar_municipios(self, CodigoIBGE: Optional[int] = None, CodigoMunicipio: Optional[int] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Municípios"""
        params = self._format_filters(CodigoIBGE=CodigoIBGE, CodigoMunicipio=CodigoMunicipio, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/municipio", params=params)

    def obter_municipio(self, id: str) -> Any:
        """Leitura de Município pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/municipio/{id}", params=params)

    def atualizar_municipio(self, id: str, dados: Any, **kwargs) -> Any:
        """Atualização de Município"""
        return self.client.patch(f"/api/empresarial/v1/municipio/{id}", json=dados, **kwargs)

    def obter_natureza_efd_reinf(self, id: str) -> Any:
        """Leitura de Natureza EFD Reinf pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/natureza-efd-reinf/{id}", params=params)

    def buscar_naturezas_efd_reinf(self, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Naturezas EFD Reinf"""
        params = self._format_filters(Codigo=Codigo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/natureza-efd-reinf", params=params)

    def obter_natureza_de_operacao(self, id: str) -> Any:
        """Leitura de Natureza De Operação pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/natureza-operacao/{id}", params=params)

    def buscar_naturezas_de_operacao(self, Modulos: Optional[List[Any]] = None, IdFilial: Optional[str] = None, Classificacao: Optional[str] = None, Nome: Optional[str] = None, DescricaoLegal: Optional[str] = None, CFOP: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Naturezas De Operação"""
        params = self._format_filters(Modulos=Modulos, IdFilial=IdFilial, Classificacao=Classificacao, Nome=Nome, DescricaoLegal=DescricaoLegal, CFOP=CFOP, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/natureza-operacao", params=params)

    def obter_operacao_comercial(self, id: str) -> Any:
        """Leitura de Operação Comercial pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/operacao-comercial/{id}", params=params)

    def buscar_operacoes_comerciais(self, IdFilial: Optional[str] = None, TipoNf: Optional[Any] = None, Descricao: Optional[str] = None, ClasseProduto: Optional[Any] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Operações Comerciais"""
        params = self._format_filters(IdFilial=IdFilial, TipoNf=TipoNf, Descricao=Descricao, ClasseProduto=ClasseProduto, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/operacao-comercial", params=params)

    def criar_pessoas(self, dados: Any, **kwargs) -> Any:
        """Gravação de Pessoas"""
        return self.client.post(f"/api/empresarial/v1/pessoa", json=dados, **kwargs)

    def buscar_pessoas(self, Nome: Optional[str] = None, Apelido: Optional[str] = None, Email: Optional[str] = None, IdUsuario: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Pessoas"""
        params = self._format_filters(Nome=Nome, Apelido=Apelido, Email=Email, IdUsuario=IdUsuario, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/pessoa", params=params)

    def obter_pessoa(self, id: str) -> Any:
        """Leitura de Pessoa pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/pessoa/{id}", params=params)

    def obter_plano_de_conta_contabil(self, id: str) -> Any:
        """Leitura de Plano de Conta Contábil pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/plano-contabil/{id}", params=params)

    def buscar_planos_de_conta_contabil(self, Codigo: Optional[str] = None, Tipo: Optional[Any] = None, Classificacao: Optional[str] = None, Caracteristicas: Optional[List[Any]] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Planos de Conta Contábil"""
        params = self._format_filters(Codigo=Codigo, Tipo=Tipo, Classificacao=Classificacao, Caracteristicas=Caracteristicas, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/plano-contabil", params=params)

    def obter_plano_de_conta_gerencial(self, id: str) -> Any:
        """Leitura de Plano de Conta Gerencial pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/plano-gerencial/{id}", params=params)

    def buscar_planos_de_conta_gerencial(self, Codigo: Optional[str] = None, Tipo: Optional[Any] = None, Classificacao: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Planos de Conta Gerencial"""
        params = self._format_filters(Codigo=Codigo, Tipo=Tipo, Classificacao=Classificacao, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/plano-gerencial", params=params)

    def obter_portador(self, id: str) -> Any:
        """Leitura de Portador pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/portador/{id}", params=params)

    def buscar_portadores(self, Numero: Optional[str] = None, NomeFantasia: Optional[str] = None, CodigoISPB: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Portadores"""
        params = self._format_filters(Numero=Numero, NomeFantasia=NomeFantasia, CodigoISPB=CodigoISPB, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/portador", params=params)

    def obter_produto(self, id: str) -> Any:
        """Leitura de Produto pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/produto/{id}", params=params)

    def buscar_produtos(self, Tipo: Optional[List[Any]] = None, Situacao: Optional[Any] = None, Codigo: Optional[str] = None, Nome: Optional[str] = None, Descricao: Optional[str] = None, GTIN: Optional[str] = None, Referencia: Optional[str] = None, ReferenciaGrade: Optional[str] = None, DataHoraAlteracao: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Produtos"""
        params = self._format_filters(Tipo=Tipo, Situacao=Situacao, Codigo=Codigo, Nome=Nome, Descricao=Descricao, GTIN=GTIN, Referencia=Referencia, ReferenciaGrade=ReferenciaGrade, DataHoraAlteracao=DataHoraAlteracao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/produto", params=params)

    def obter_recurso(self, id: str) -> Any:
        """Leitura de Recurso pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/recurso/{id}", params=params)

    def buscar_recursos(self, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Recursos"""
        params = self._format_filters(Codigo=Codigo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/recurso", params=params)

    def obter_representante(self, id: str) -> Any:
        """Leitura de Representante pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/representante/{id}", params=params)

    def buscar_representantes(self, TipoPessoa: Optional[Any] = None, Situacao: Optional[Any] = None, RazaoSocial: Optional[str] = None, NomeFantasia: Optional[str] = None, Codigo: Optional[str] = None, IdMunicipio: Optional[str] = None, UF: Optional[str] = None, DataHoraGravacaoInicial: Optional[str] = None, DataHoraGravacaoFinal: Optional[str] = None, CpfCnpj: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Representantes"""
        params = self._format_filters(TipoPessoa=TipoPessoa, Situacao=Situacao, RazaoSocial=RazaoSocial, NomeFantasia=NomeFantasia, Codigo=Codigo, IdMunicipio=IdMunicipio, UF=UF, DataHoraGravacaoInicial=DataHoraGravacaoInicial, DataHoraGravacaoFinal=DataHoraGravacaoFinal, CpfCnpj=CpfCnpj, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/representante", params=params)

    def leitura_do_cadastro_de_requisitantes(self, id: str) -> Any:
        """Leitura do cadastro de Requisitantes pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/requisitante/{id}", params=params)

    def busca_do_cadastro_de_requisitantes(self, Codigo: Optional[str] = None, IdFilial: Optional[str] = None, IdDepartamento: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca do cadastro de Requisitantes"""
        params = self._format_filters(Codigo=Codigo, IdFilial=IdFilial, IdDepartamento=IdDepartamento, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/requisitante", params=params)

    def obter_servico(self, id: str) -> Any:
        """Leitura de Serviço pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/servico/{id}", params=params)

    def buscar_servicos(self, Codigo: Optional[str] = None, Nome: Optional[str] = None, Descricao: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Serviços"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, Descricao=Descricao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/servico", params=params)

    def obter_tabela_de_preco_de_venda_de_produto(self, id: str) -> Any:
        """Leitura de Tabela de Preço de Venda de Produto pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/tabela-preco-venda-produto/{id}", params=params)

    def buscar_tabelas_de_preco_de_venda_de_produto(self, Codigo: Optional[str] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Tabelas de Preço de Venda de Produto"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/tabela-preco-venda-produto", params=params)

    def obter_tabela_de_preco_de_venda_de_servico(self, id: str) -> Any:
        """Leitura de Tabela de Preço de Venda de Serviço pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/tabela-preco-venda-servico/{id}", params=params)

    def buscar_tabelas_de_preco_de_venda_de_servico(self, Codigo: Optional[str] = None, Nome: Optional[str] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Tabelas de Preço de Venda de Serviço"""
        params = self._format_filters(Codigo=Codigo, Nome=Nome, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/tabela-preco-venda-servico", params=params)

    def criar_tipos_de_cobranca(self, dados: Any, **kwargs) -> Any:
        """Gravação de Tipos de Cobrança"""
        return self.client.post(f"/api/empresarial/v1/tipo-cobranca", json=dados, **kwargs)

    def buscar_tipos_de_cobranca(self, Codigo: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Tipos de Cobrança"""
        params = self._format_filters(Codigo=Codigo, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/tipo-cobranca", params=params)

    def obter_tipo_de_cobranca(self, id: str) -> Any:
        """Leitura de Tipo de Cobrança pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/tipo-cobranca/{id}", params=params)

    def obter_tipo_de_periodo(self, id: str) -> Any:
        """Leitura de Tipo de Período pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/tipo-periodo/{id}", params=params)

    def buscar_tipos_de_periodo(self, Modulos: Optional[List[Any]] = None, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Tipos de Período"""
        params = self._format_filters(Modulos=Modulos, Codigo=Codigo, Descricao=Descricao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/tipo-periodo", params=params)

    def obter_tipo_de_recolhimento(self, id: str) -> Any:
        """Leitura de Tipo de Recolhimento pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/tipo-recolhimento/{id}", params=params)

    def buscar_tipos_de_recolhimento(self, Tipo: Optional[str] = None, Descricao: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Tipos de Recolhimento"""
        params = self._format_filters(Tipo=Tipo, Descricao=Descricao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/tipo-recolhimento", params=params)

    def obter_tipo_de_recurso(self, id: str) -> Any:
        """Leitura de Tipo de Recurso pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/tipo-recurso/{id}", params=params)

    def buscar_tipos_de_recurso(self, Codigo: Optional[str] = None, Tipo: Optional[Any] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Tipos de Recurso"""
        params = self._format_filters(Codigo=Codigo, Tipo=Tipo, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/tipo-recurso", params=params)

    def obter_tipo_de_vencimento(self, id: str) -> Any:
        """Leitura de Tipo de Vencimento pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/tipo-vencimento/{id}", params=params)

    def buscar_tipos_de_vencimentos(self, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Tipos de Vencimentos"""
        params = self._format_filters(Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/tipo-vencimento", params=params)

    def obter_transportadora(self, id: str) -> Any:
        """Leitura de Transportadora pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/transportadora/{id}", params=params)

    def buscar_transportadoras(self, TipoPessoa: Optional[Any] = None, Situacao: Optional[Any] = None, RazaoSocial: Optional[str] = None, NomeFantasia: Optional[str] = None, Codigo: Optional[str] = None, IdMunicipio: Optional[str] = None, UF: Optional[str] = None, DataHoraGravacaoInicial: Optional[str] = None, DataHoraGravacaoFinal: Optional[str] = None, CpfCnpj: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Transportadoras"""
        params = self._format_filters(TipoPessoa=TipoPessoa, Situacao=Situacao, RazaoSocial=RazaoSocial, NomeFantasia=NomeFantasia, Codigo=Codigo, IdMunicipio=IdMunicipio, UF=UF, DataHoraGravacaoInicial=DataHoraGravacaoInicial, DataHoraGravacaoFinal=DataHoraGravacaoFinal, CpfCnpj=CpfCnpj, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/transportadora", params=params)

    def obter_unidades_logisticas(self, id: str) -> Any:
        """Leitura de Unidades Logísticas pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/unidade-logistica/{id}", params=params)

    def buscar_unidades_logisticas(self, Codigo: Optional[str] = None, Descricao: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Unidades Logísticas"""
        params = self._format_filters(Codigo=Codigo, Descricao=Descricao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/unidade-logistica", params=params)

    def obter_unidade_de_medida(self, id: str) -> Any:
        """Leitura de Unidade de Medida pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/unidade-medida-produto/{id}", params=params)

    def buscar_unidades_de_medida(self, Abreviatura: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Unidades de Medida"""
        params = self._format_filters(Abreviatura=Abreviatura, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/unidade-medida-produto", params=params)

    def obter_unidade_de_medida_2(self, id: str) -> Any:
        """Leitura de Unidade de Medida pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/unidade-medida-servico/{id}", params=params)

    def buscar_unidades_de_medida_2(self, Abreviatura: Optional[str] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Unidades de Medida"""
        params = self._format_filters(Abreviatura=Abreviatura, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/unidade-medida-servico", params=params)

    def obter_usuario(self, id: str) -> Any:
        """Leitura de Usuário pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/usuario/{id}", params=params)

    def buscar_usuarios(self, Nome: Optional[str] = None, Apelido: Optional[str] = None, Supervisor: Optional[Any] = None, Situacao: Optional[Any] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Usuários"""
        params = self._format_filters(Nome=Nome, Apelido=Apelido, Supervisor=Supervisor, Situacao=Situacao, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/usuario", params=params)

    def obter_veiculo(self, id: str) -> Any:
        """Leitura de Veículo pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/veiculo/{id}", params=params)

    def buscar_veiculos(self, TaraInicial: Optional[float] = None, TaraFinal: Optional[float] = None, CapacidadeQuilogramaInicial: Optional[float] = None, CapacidadeQuilogramaFinal: Optional[float] = None, CapacidadeMetroCubicoInicial: Optional[float] = None, CapacidadeMetroCubicoFinal: Optional[float] = None, AnoInicial: Optional[int] = None, AnoFinal: Optional[int] = None, IdCliente: Optional[str] = None, Descricao: Optional[str] = None, CodigoANTT: Optional[str] = None, Codigo: Optional[str] = None, RENAVAM: Optional[str] = None, Placa: Optional[str] = None, UF: Optional[str] = None, Situacao: Optional[Any] = None, TiposCarroceria: Optional[List[Any]] = None, TiposRodado: Optional[List[Any]] = None, TiposVeiculo: Optional[List[Any]] = None, TiposTransporte: Optional[List[Any]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Veículos"""
        params = self._format_filters(TaraInicial=TaraInicial, TaraFinal=TaraFinal, CapacidadeQuilogramaInicial=CapacidadeQuilogramaInicial, CapacidadeQuilogramaFinal=CapacidadeQuilogramaFinal, CapacidadeMetroCubicoInicial=CapacidadeMetroCubicoInicial, CapacidadeMetroCubicoFinal=CapacidadeMetroCubicoFinal, AnoInicial=AnoInicial, AnoFinal=AnoFinal, IdCliente=IdCliente, Descricao=Descricao, CodigoANTT=CodigoANTT, Codigo=Codigo, RENAVAM=RENAVAM, Placa=Placa, UF=UF, Situacao=Situacao, TiposCarroceria=TiposCarroceria, TiposRodado=TiposRodado, TiposVeiculo=TiposVeiculo, TiposTransporte=TiposTransporte, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/veiculo", params=params)

    def obter_vendedor(self, id: str) -> Any:
        """Leitura de Vendedor pelo ID"""
        params = {}
        return self.client.get(f"/api/empresarial/v1/vendedor/{id}", params=params)

    def buscar_vendedores(self, Nome: Optional[str] = None, Email: Optional[str] = None, PercentualComissaoFaturamentoInicial: Optional[float] = None, PercentualComissaoFaturamentoFinal: Optional[float] = None, PercentualComissaoRecebimentoInicial: Optional[float] = None, PercentualComissaoRecebimentoFinal: Optional[float] = None, Codigo: Optional[str] = None, Situacao: Optional[Any] = None, PagamentoComissao: Optional[Any] = None, ListaIDFilial: Optional[List[str]] = None, Ids: Optional[List[str]] = None, CodigosIntegrador: Optional[List[str]] = None, Fields: Optional[List[str]] = None, **outros_filtros) -> Any:
        """Busca de Vendedores"""
        params = self._format_filters(Nome=Nome, Email=Email, PercentualComissaoFaturamentoInicial=PercentualComissaoFaturamentoInicial, PercentualComissaoFaturamentoFinal=PercentualComissaoFaturamentoFinal, PercentualComissaoRecebimentoInicial=PercentualComissaoRecebimentoInicial, PercentualComissaoRecebimentoFinal=PercentualComissaoRecebimentoFinal, Codigo=Codigo, Situacao=Situacao, PagamentoComissao=PagamentoComissao, ListaIDFilial=ListaIDFilial, Ids=Ids, CodigosIntegrador=CodigosIntegrador, Fields=Fields, **outros_filtros)
        return self.client.get(f"/api/empresarial/v1/vendedor", params=params)

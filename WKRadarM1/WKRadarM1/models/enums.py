"""Modelos e constantes para filtros da API WK Radar."""

from enum import Enum

class Situacao(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"
    AMBOS = "Ambos"

class TipoContrato(Enum):
    CLT = "CLT"
    PJ = "PJ"
    ESTAGIO = "Estagio"

class TipoPeriodo(Enum):
    MENSAL = "Mensal"
    DIARIO = "Diario"
    ANUAL = "Anual"

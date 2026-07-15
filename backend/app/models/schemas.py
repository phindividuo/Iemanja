"""Schemas Pydantic: o contrato da API."""

from datetime import datetime
from pydantic import BaseModel, Field

class Estacao(BaseModel):
    """Ponto de monitoramento na costa."""

    id: int
    nome: str
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

class CondicoesAtuais(BaseModel):
    """Condições do mar mais recentes em uma estação."""

    estacao_id: int
    timestamp: datetime
    altura_onda_m: float = Field(..., description="Altura significativa de onda (m)")
    direcao_onda_graus: float | None = None
    temperatura_agua_c: float | None = Field(
        None, description="Temperatura da superfície do mar (°C)"
    )

class PontoPrevisao(BaseModel):
    """Um instante da série temporal de previsão."""

    timestamp: datetime
    altura_onda_m: float
    temperatura_agua_c: float | None = None


class ResumoPrevisao(BaseModel):
    """Estatísticas agregadas da janela de previsão (calculadas com Pandas)."""

    altura_onda_maxima_m: float
    altura_onda_media_m: float
    pior_momento: datetime = Field(..., description="Instante da maior onda prevista")


class Previsao(BaseModel):
    """Previsão completa."""

    estacao_id: int
    horas: int
    resumo: ResumoPrevisao
    serie: list[PontoPrevisao]

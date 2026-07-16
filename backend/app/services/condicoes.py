"""Transformação dos dados brutos da Open-Meteo em respostas da API."""

import pandas as pd

from app.models.schemas import (
    CondicoesAtuais,
    Estacao,
    PontoPrevisao,
    Previsao,
    ResumoPrevisao,
)
from app.repositories import open_meteo

def _montar_dataframe(dados_brutos: dict) -> pd.DataFrame:
    """Converte o JSON horário da Open-Meteo em DataFrame indexado por tempo."""
    hourly = dados_brutos["hourly"]
    df = pd.DataFrame(
        {
            "altura_onda_m": hourly["wave_height"],
            "direcao_onda_graus": hourly["wave_direction"],
            "temperatura_agua_c": hourly["sea_surface_temperature"],
        },
        index=pd.to_datetime(hourly["time"], utc=True),
    )
    return df

async def condicoes_atuais(estacao: Estacao) -> CondicoesAtuais:
    """Condições mais recentes: a última linha passada da série horária."""
    dados = await open_meteo.buscar_dados_marinhos(
        estacao.latitude, estacao.longitude, horas=24
    )
    df = _montar_dataframe(dados)
    agora = pd.Timestamp.now(tz="UTC")
    passado = df[df.index <= agora]
    linha = passado.iloc[-1] if not passado.empty else df.iloc[0]

    return CondicoesAtuais(
        estacao_id=estacao.id,
        timestamp=linha.name,
        altura_onda_m=float(linha["altura_onda_m"]),
        direcao_onda_graus=_ou_none(linha["direcao_onda_graus"]),
        temperatura_agua_c=_ou_none(linha["temperatura_agua_c"]),
    )

async def previsao(estacao: Estacao, horas: int = 48) -> Previsao:
    """Previsão com resumo estatístico calculado via Pandas."""
    dados = await open_meteo.buscar_dados_marinhos(
        estacao.latitude, estacao.longitude, horas=horas
    )
    df = _montar_dataframe(dados)

    agora = pd.Timestamp.now(tz="UTC")
    janela = df[(df.index >= agora) & (df.index <= agora + pd.Timedelta(hours=horas))]
    if janela.empty:
        janela = df.head(horas)

    janela = janela.assign(
        altura_suavizada=janela["altura_onda_m"].rolling(window=3, min_periods=1).mean()
    )

    resumo = ResumoPrevisao(
        altura_onda_maxima_m=float(janela["altura_onda_m"].max()),
        altura_onda_media_m=round(float(janela["altura_onda_m"].mean()), 2),
        pior_momento=janela["altura_onda_m"].idxmax(),
    )

    serie = [
        PontoPrevisao(
            timestamp=ts,
            altura_onda_m=float(linha["altura_suavizada"]),
            temperatura_agua_c=_ou_none(linha["temperatura_agua_c"]),
        )
        for ts, linha in janela.iterrows()
    ]

    return Previsao(estacao_id=estacao.id, horas=horas, resumo=resumo, serie=serie)

def _ou_none(valor) -> float | None:
    """NaN do Pandas vira None do Python (e null no JSON)."""
    return None if pd.isna(valor) else float(valor)

"""Cliente da Open-Meteo Marine API."""

import httpx

BASE_URL = "https://marine-api.open-meteo.com/v1/marine"
VARIAVEIS = "wave_height,wave_direction,sea_surface_temperature"

async def buscar_dados_marinhos(
    latitude: float, longitude: float, horas: int = 48
) -> dict:

    """Busca série horária de condições do mar para um ponto.

    Levanta httpx.HTTPStatusError se a API externa responder erro.
    """

    parametros = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": VARIAVEIS,
        "forecast_days": max(1, -(-horas // 24)),
        "timezone": "UTC",
    }

    async with httpx.AsyncClient(timeout=10.0) as client:

        resposta = await client.get(BASE_URL, params=parametros)
        resposta.raise_for_status()
        return resposta.json()

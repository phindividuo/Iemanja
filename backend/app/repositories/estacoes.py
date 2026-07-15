"""Catálogo de estações monitoradas.

Em um cenário real, esses dados viriam de um banco de dados. Para esse protótipo, utilizo dados mockados para maior simplicidade. Caso venha a evoluir para um sistema, essa interface deve ser adaptada.

"""

from app.models.schemas import Estacao

_ESTACOES: dict[int, Estacao] = {
    1: Estacao(id=1, nome="Copacabana", latitude=-22.985, longitude=-43.19),
    2: Estacao(id=2, nome="Barra da Tijuca", latitude=-23.02, longitude=-43.37),
    3: Estacao(id=3, nome="Itacoatiara", latitude=-22.972, longitude=-43.03),
    4: Estacao(id=4, nome="Arraial do Cabo", latitude=-22.98, longitude=-42.02),
    5: Estacao(id=5, nome="Baía de Guanabara (entrada)", latitude=-22.93, longitude=-43.13),
}

def listar() -> list[Estacao]:
    return list(_ESTACOES.values())

def obter(estacao_id: int) -> Estacao | None:
    return _ESTACOES.get(estacao_id)

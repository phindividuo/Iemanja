# Iemanjá 🌊
Projeto de **Plataforma Web/PWA**, construído em **Python** e **React**, para coletar e **processar** dados oceânicos (tempo real e previstos), **calcular** indicadores das condições do mar e **exibir** em um mapa interativo da costa fluminense.
---
## 🎯 Objetivo do Projeto
Operações marítimas — resposta a emergências, navegação, pesquisa ambiental — dependem de uma pergunta crítica: **"Quais são as condições do mar agora, e como estarão nas próximas horas, em cada ponto da costa?"**
Este projeto foi desenvolvido para responder a essa pergunta de forma visual e quantitativa. O objetivo é construir uma **API REST** que coleta dados marítimos, processa indicadores oceânicos e disponibiliza os insights através de um **Mapa Interativo** instalável como **PWA**.
> **Iemanjá**, a rainha dos mares — nome em homenagem à orixá protetora dos que vivem do oceano.
---
## 📊 Insights
A análise é feita com base nas condições do mar em **estações da costa do Rio de Janeiro** (Copacabana, Itacoatiara, Arraial do Cabo, entre outras). Como resultado, são fornecidos a **Altura Máxima e Média de Onda** prevista para as próximas 48h, o **Pior Momento** — aquele com a **maior onda prevista na janela**, e a **Climatologia Histórica** — temperatura média do mar por região, servida a partir de dados **NetCDF** via **Xarray**.
---
## 🛠️ Arquitetura e Tecnologias
O projeto segue uma **arquitetura em camadas** no back-end e componentização no front-end, separando **contrato**, **negócio** e **acesso a dados**.
| Etapa | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **1. Coleta** | `httpx` | Consumo assíncrono da API pública **Open-Meteo Marine** para dados de ondas e temperatura. |
| **2. Processamento** | `Pandas` & `Xarray` | Agregações de séries temporais e fatiamento de dados multidimensionais (NetCDF). |
| **3. API REST** | `FastAPI` & `Pydantic` | Endpoints versionados (`/api/v1`), validação automática e documentação Swagger. |
| **4. Visualização** | `React` & `Leaflet` | Mapa interativo com estações, popups de condições e gráfico de previsão. |
| **5. PWA** | `Vite` & `vite-plugin-pwa` | Manifest e service worker para instalação e uso offline. |
| **Testes** | `pytest` & `TestClient` | Testes unitários (service) e de integração (endpoints). |
| **Infraestrutura** | `Docker` & `GitHub Actions` | Conteinerização do back-end e pipeline de CI a cada push. |
| **Versionamento** | `Git` & `GitHub` | Controle de versão com Conventional Commits. |
---
## 📂 Estrutura do Projeto
* `backend/app/main.py`: Aplicação principal (instância FastAPI e healthcheck).
* `backend/app/routers/`: Camada HTTP — recebe requisições, delega e responde.
* `backend/app/services/`: Regra de negócio e processamento de dados (Pandas/Xarray).
* `backend/app/repositories/`: Acesso a fontes de dados (Open-Meteo, catálogo de estações).
* `backend/app/models/`: Schemas Pydantic — o contrato público da API.
* `backend/tests/`: Testes unitários e de integração.
* `frontend/`: Aplicação React (Vite) com mapa Leaflet e configuração PWA.
---
## 🚀 Como Executar o Projeto
Siga os passos abaixo para rodar a plataforma na sua máquina:
### 1. Preparação do Ambiente (Back-end)
Clone o repositório, crie um ambiente virtual e instale as dependências:
```bash
git clone https://github.com/SEU_USUARIO/Iemanja.git
cd Iemanja/backend
# Cria e ativa o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate
# Instala os pacotes necessários
pip install -r requirements.txt
```
### 2. Execução da API
Suba o servidor de desenvolvimento:
```bash
uvicorn app.main:app --reload
```
A documentação interativa (Swagger) fica disponível em `http://localhost:8000/docs`.
### 3. Execução do Front-end
Em outro terminal, instale as dependências e suba o mapa:
```bash
cd frontend
npm install
npm run dev
```
---
## 🧭 Status
Protótipo em **desenvolvimento ativo**.

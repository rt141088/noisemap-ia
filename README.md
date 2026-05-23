# 🔊 Noisemap IA — Previsão Inteligente de Ruído com Inteligência Artificial

## 📌 Sobre o Projeto

O **Noisemap IA** é uma aplicação desenvolvida para prever níveis de ruído utilizando técnicas de **Machine Learning** integradas a uma aplicação web.

O sistema foi criado como parte da disciplina:

**Disruptive Architectures: IoT, IoB & Generative IA**

O projeto utiliza um modelo de Inteligência Artificial treinado com dados simulados de ruído ao longo do dia, permitindo prever o nível de ruído com base na hora informada pelo usuário.

---

# 🎯 Objetivo

Desenvolver uma solução inteligente capaz de:

* Aplicar conceitos de Inteligência Artificial;
* Realizar previsões utilizando Machine Learning;
* Integrar IA com aplicações web;
* Criar uma API REST consumível;
* Integrar o sistema com Oracle APEX;
* Demonstrar integração entre frontend, backend e IA;
* Simular um cenário de cidades inteligentes (Smart Cities).

---

# 🧠 Inteligência Artificial Utilizada

O projeto utiliza um modelo de **Regressão Linear** desenvolvido com a biblioteca:

* Scikit-learn

O modelo foi treinado utilizando dados históricos simulados de níveis de ruído.

## 📊 Variáveis utilizadas

| Entrada     | Saída                   |
| ----------- | ----------------------- |
| Hora do dia | Nível de ruído previsto |

---

# ⚙️ Tecnologias Utilizadas

## 🖥️ Backend

* Python
* Flask
* Pandas
* Scikit-learn
* NumPy

## 🌐 Frontend

* HTML5
* CSS3

## ☁️ Integração

* Oracle APEX
* ngrok
* REST API

## 🧰 Ferramentas

* VSCode
* GitHub
* Postman / API Testing

---

# 🏗️ Arquitetura da Solução

```text
Usuário
   ↓
Interface Web (HTML/CSS)
   ↓
Flask API
   ↓
Modelo IA (Scikit-learn)
   ↓
Previsão Inteligente
```

## 🌐 Arquitetura com Oracle APEX

```text
Oracle APEX
      ↓ REST API
ngrok
      ↓
Flask API
      ↓
Modelo de IA
      ↓
Resultado da previsão
```

---

# 📂 Estrutura do Projeto

```text
noisemap-ia/
│
├── app.py
├── treino_modelo.py
├── dados.csv
├── modelo.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── prints/
```

---

# 📊 Base de Dados

Os dados utilizados são simulados e representam níveis médios de ruído ao longo do dia.

## Exemplo dos dados utilizados

| Hora | Ruído |
| ---- | ----- |
| 1    | 30    |
| 5    | 35    |
| 8    | 50    |
| 12   | 65    |
| 18   | 80    |
| 22   | 90    |

---

# 🧪 Funcionamento do Modelo

O modelo é treinado utilizando:

```python
LinearRegression()
```

Após o treinamento, o modelo é salvo em:

```text
modelo.pkl
```

A aplicação Flask carrega esse modelo treinado para realizar previsões em tempo real.

---

# 🚀 Como Executar o Projeto

## 1️⃣ Clonar repositório

```bash
git clone https://github.com/rt141088/noisemap-ia.git
```

---

## 2️⃣ Acessar pasta

```bash
cd noisemap-ia
```

---

## 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Treinar modelo

```bash
python treino_modelo.py
```

Resultado esperado:

```text
Modelo treinado!
```

---

## 5️⃣ Executar aplicação

```bash
python app.py
```

Resultado esperado:

```text
Running on http://127.0.0.1:5000
```

---

# 🌐 Executando via Navegador

Abra:

```text
http://127.0.0.1:5000
```

O sistema exibirá a interface web do projeto.

---

# 📈 Exemplo de Previsão

## Entrada

```text
Hora: 22
```

## Resultado

```text
Ruído previsto: 89.86 dB
```

---

# 🔌 API REST

A aplicação disponibiliza uma API REST para integração externa.

## Endpoint

```text
POST /prever
```

## Exemplo de JSON enviado

```json
{
  "hora": 22
}
```

## Exemplo de resposta

```json
{
  "ruido_previsto": 89.86
}
```

---

# ☁️ Integração com ngrok

O projeto utiliza ngrok para disponibilizar a API Flask publicamente.

## Executar ngrok

```bash
ngrok http 5000
```

Resultado esperado:

```text
https://xxxxx.ngrok-free.dev
```

Essa URL permite integração com Oracle APEX e testes externos.

---

# 🧩 Integração com Oracle APEX

O Oracle APEX consome a API REST desenvolvida em Flask utilizando o pacote:

```sql
APEX_WEB_SERVICE.MAKE_REST_REQUEST
```

Fluxo da integração:

```text
Usuário → Oracle APEX → API Flask → IA → Resultado
```

---

# 🧪 Testes Realizados

## ✔️ Testes executados

* Execução da aplicação Flask;
* Treinamento do modelo IA;
* Predição de ruído;
* Comunicação REST API;
* Integração via ngrok;
* Integração Oracle APEX;
* Testes de resposta JSON.

---

# 📸 Evidências

## Interface do Sistema funcionando

### Previsão para hora 5 → 27.04 dB
![Previsão hora 5](prints/tela-hora5.png)

### Previsão para hora 10 → 41.32 dB
![Previsão hora 10](prints/tela-hora10.png)

### Previsão resultado → 55.59 dB
![Previsão resultado](prints/tela-hora-resultado.png)

# 🎥 Vídeo Pitch

O vídeo demonstra:

* Objetivo do projeto;
* Funcionamento da IA;
* Demonstração da aplicação;
* Integração Oracle APEX;
* API REST;
* Previsões em tempo real.

## 🔗 Link do vídeo

```text
ADICIONAR LINK DO YOUTUBE AQUI
```

---

# 💻 Repositório GitHub

## 🔗 Link do repositório

```text
https://github.com/rt141088/noisemap-ia
```

---

# 📚 Conceitos Aplicados

* Inteligência Artificial;
* Machine Learning;
* Regressão Linear;
* APIs REST;
* Integração de Sistemas;
* Cloud Tunneling;
* Desenvolvimento Web;
* Oracle APEX;
* Arquitetura de Software.

---

# 🔒 Melhorias Futuras

* Utilização de banco de dados real;
* Mais dados para treinamento;
* Dashboard analítico;
* Deploy em nuvem;
* Modelos mais avançados de IA;
* Integração com sensores IoT.

---

# 👨‍💻 Integrantes do Projeto

| Integrante              | RM       |
| ----------------------- | -------- |
| Rafael Terra Teodoro    | 560955 |
| Enzo Elia Tarraga       | 560901 |
| Otoniel Arantes Barbado | 560112 |

---

# 🎓 Instituição

FIAP — Faculdade de Informática e Administração Paulista

Disciplina:

**Disruptive Architectures: IoT, IoB & Generative IA**

Sprint 4

---

# 📌 Projeto Acadêmico

Projeto acadêmico desenvolvido para fins educacionais e demonstração prática de integração entre Inteligência Artificial, Machine Learning, APIs REST e Oracle APEX.

---

# ✅ Conclusão

O projeto Noisemap IA demonstra na prática a integração entre Inteligência Artificial, APIs REST e Oracle APEX.

A solução foi capaz de:

* Criar um modelo funcional de Machine Learning;
* Integrar IA em aplicações web;
* Disponibilizar serviços REST;
* Realizar previsões em tempo real;
* Demonstrar integração entre frontend, backend e IA.

O projeto atende aos requisitos propostos na Sprint 4, incluindo desenvolvimento da IA, integração com Oracle APEX, testes e documentação técnica.

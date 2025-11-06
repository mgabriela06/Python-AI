# 🤖 Python AI — Chat Integrado com a API do Gemini

Projeto desenvolvido em **Python** para consumir a **API do Gemini**, permitindo a integração e utilização dos recursos de inteligência artificial do modelo de forma simples e eficiente.

---

## Estrutura do Projeto

- **main.py** — Arquivo principal contendo o código do chat e a lógica de interação com o modelo.

---

## Funcionamento:

O programa:

1. Cria um cliente para a **API do Gemini** usando a chave de API fornecida pelo usuário.  
2. Exibe um menu para o usuário escolher entre **enviar uma pergunta à IA** ou **encerrar o programa**.  
3. Envia a pergunta para o modelo `gemini-2.5-flash` e retorna uma resposta curta (limitada a 250 caracteres).  

---

## Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- **Python 3.x**  
- **Ambiente virtual (venv)**  
- Biblioteca oficial do Gemini:

```bash
pip install google-genai

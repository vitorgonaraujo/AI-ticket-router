# AI Ticket Router

Projeto criado com foco em estudo e aprendizado sobre integração de aplicações Python com modelos de linguagem.

A ideia é simples: receber mensagens de suporte e usar IA para classificar cada uma em uma categoria.

## Categorias

Atualmente as mensagens podem ser classificadas como:

* `FINANCEIRO`
* `SUPORTE_TECNICO`
* `VENDAS`
* `SAUDACAO`
* `OUTROS`

Exemplo:

```text
Mensagem:
"Meu boleto venceu, como faço para pagar?"

Categoria:
FINANCEIRO
```

## Tecnologias

* Python
* Cohere API
* Poetry
* python-dotenv

## Como rodar

Clone o repositório:

```bash
git clone https://github.com/vitorgonaraujo/AI-ticket-router.git
cd AI-ticket-router
```

Instale as dependências:

```bash
poetry install
```

Crie um arquivo `.env` na raiz do projeto e adicione sua chave da Cohere:

```env
COHERE_API_KEY=sua_chave_aqui
```

Depois execute:

```bash
poetry run python -m ai_ticket_router
```

## Sobre o projeto

Este projeto não tem como objetivo ser uma solução completa de atendimento ou roteamento de tickets.

Ele foi desenvolvido principalmente para praticar:

* uso de APIs de modelos de linguagem;
* criação de prompts para classificação;
* organização de um projeto Python;
* gerenciamento de dependências com Poetry;
* uso de variáveis de ambiente.

## Estrutura

```text
src/
└── ai_ticket_router/
    ├── __init__.py
    ├── __main__.py
    └── suport_agent.py
```

## Observação

É necessário possuir uma chave válida da API da Cohere para executar o projeto.

## Autor


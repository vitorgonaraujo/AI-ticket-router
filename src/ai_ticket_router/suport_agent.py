import os
import cohere
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(api_key=api_key)

support_messages = [
    "Meu boleto venceu e não consegui pagar, tem como reemitir?",  # FINANCEIRO
    "O app fecha sozinho toda vez que tento abrir o histórico.",  # SUPORTE_TECNICO
    "Quero comprar o plano premium para a minha equipe.",  # VENDAS
    "Oi, boa tarde! Tem alguém online para me ajudar?",  # SAUDACAO
    "Vocês abrem aos sábados? Qual o horário de funcionamento?",  # OUTROS
    "asdfghjk teste",  # OUTROS
    "Quero mudar a minha senha mas não chega o e-mail de código.",  # SUPORTE_TECNICO
]

SYSTEM_CONTEXT = """
Você é um agente automatizado de triagem de suporte. 
Sua única tarefa é ler a mensagem do cliente e categorizá-la em uma das opções abaixo:

- FINANCEIRO: Questões sobre pagamentos, boletos, reembolsos, Pix ou cobranças.
- SUPORTE_TECNICO: Bugs, erros no aplicativo, problemas de login, senha ou travamentos.
- VENDAS: Interesse em comprar, planos, preços ou novos serviços.
- SAUDACAO: Cumprimentos iniciais, como 'Oi', 'Olá', 'Bom dia', 'Boa tarde', sem nenhuma dúvida junto.
- OUTROS: Dúvidas gerais, elogios, endereço da empresa ou textos confusos/sem sentido que não se encaixam nos anteriores.

Regra estrita: Você deve responder APENAS com uma das cinco palavras acima em letras maiúsculas (FINANCEIRO, SUPORTE_TECNICO, VENDAS, SAUDACAO ou OUTROS). 
Não adicione pontos finais, saudações, explicações ou qualquer outro texto. Apenas a palavra correspondente.
"""

print("\n" + "=" * 50)
print("  INICIANDO A TRIAGEM DE TICKETS")
print("=" * 50 + "\n")

answered_list = []

for index, message in enumerate(support_messages, start=1):
    response = co.chat(
        model="command-a-plus-05-2026",
        messages=[
            {
                "role": "system",
                "content": [{"type": "text", "text": SYSTEM_CONTEXT}],
            },
            {"role": "user", "content": [{"type": "text", "text": message}]},
        ],
    )

    clean_response = "".join(
        [block.text for block in response.message.content if hasattr(block, "text")]
    )
    answered_list.append({"support_message": message, "response": clean_response})

    print(f" Ticket #{index}")
    print(f" ┌ Mensagem: {message}")
    print(f" └ Categoria: {clean_response}")
    print("-" * 50)

print("\n" + "=" * 50)
print("  RESUMO FINAL DOS DADOS ESTRUTURADOS")
print("=" * 50)
print(json.dumps(answered_list, ensure_ascii=False, indent=4))
print("=" * 50 + "\n")

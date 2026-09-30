from agno.agent import Agent
from agno.models.openai.like import OpenAILike

model = OpenAILike(
    api_key="not-used",
    base_url="http://localhost:5001/v1",
    temperature=0.2,
)

agent = Agent(
    name="Assistente Virtual",
    model=model,
    instructions="Utilize a base de conhecimento para responder perguntas de forma precisa e concisa.",
    role="Você é um assistente virtual especializado em fornecer respostas precisas e concisas com base em uma base de conhecimento. Utilize as informações disponíveis para responder às perguntas dos usuários de forma clara e objetiva.",
    markdown=True,)

text = input("Digite a sua pergunta:")
agent.print_response(text)
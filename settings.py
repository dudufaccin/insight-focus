from pydantic import BaseModel, ValidationError, AnyUrl
import os


# Esquema de validação do DATABASE_URL
class EnvSchema(BaseModel):
    DATABASE_URL: AnyUrl  # Valida URLs com base no padrão definido


# Extraindo as variáveis de ambiente
try:
    # Cria uma instância do esquema usando as variáveis de ambiente
    env = EnvSchema(
        DATABASE_URL=os.getenv("DATABASE_URL")  # Recupera da variável de ambiente
    )
    print(env)  # Se passar na validação
except ValidationError as e:
    print("Erro de validação:", e.json())  # Se não passar na validação

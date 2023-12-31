from dotenv import load_dotenv, find_dotenv

"""
Загрузка переменных окружения.
'.env' имеет больший приоритет, чем 'enviroments.yml'

"""

env_file = find_dotenv(filename=".env",
                       raise_error_if_not_found=True)
load_dotenv(env_file)
print("Load .env file")

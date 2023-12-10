# Use a imagem oficial do Python como base
FROM python:3.10-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /usr/src/app

# Copie os arquivos necessários para o contêiner
COPY teste.py .
COPY input.txt .

# Instale as dependências (no nosso caso, apenas o Apache Beam)
RUN pip install apache-beam[gcp]

# Comando padrão para executar o pipeline
CMD ["python", "teste.py"]

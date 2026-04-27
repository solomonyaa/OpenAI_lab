FROM python:3.13-slim

WORKDIR /app

COPY openAI_API.py .

RUN pip install flask openai

EXPOSE 5000

CMD ["python", "openAI_API.py"]
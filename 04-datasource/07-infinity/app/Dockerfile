FROM python:3.12.5

RUN pip install uv

WORKDIR /app
COPY ./ ./
RUN uv pip install --no-cache --system -r requirements.lock

EXPOSE 8000

CMD python main.py

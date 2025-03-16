FROM python:3.12.5

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


WORKDIR /app
COPY ./ ./
RUN uv sync --frozen

EXPOSE 8000

CMD ["uv", "run", "main.py"]

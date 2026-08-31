FROM mcr.microsoft.com/playwright/python:v1.62.0-noble

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY . .
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 2020
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "2020"]

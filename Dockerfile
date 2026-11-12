FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY src/ ./src/
COPY datasets/bank_marketing.zip ./datasets/bank_marketing.zip
COPY .streamlit/ ./.streamlit/

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8501

CMD ["streamlit", "run", "src/ai_mlops_hands_on_exercise/app.py", "--server.address=0.0.0.0"]
FROM python:3.12-slim

WORKDIR /app

# install uv
RUN pip install uv

COPY . .

RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
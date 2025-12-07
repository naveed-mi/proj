FROM python:3.11-slim

RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

COPY app.py /app/app.py

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

ENV PORT=8080

CMD ["python", "app.py"]

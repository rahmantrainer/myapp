FROM python:3.12-slim
RUN useradd -u 10001 -m appuser
WORKDIR /app
COPY app/main.py .
USER 10001
ENV APP_VERSION=v1
EXPOSE 8080
CMD ["python", "main.py"]

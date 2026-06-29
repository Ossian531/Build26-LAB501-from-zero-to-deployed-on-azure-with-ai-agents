FROM python:3.13-slim

# AWS Lambda Web Adapter: lets this standard gunicorn/Flask web server run as a
# Lambda container image behind API Gateway, with no code changes to the app.
# It registers as a Lambda extension and proxies invocations to the web server
# listening on AWS_LWA_PORT (8080).
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.9.0 /lambda-adapter /opt/extensions/lambda-adapter
ENV AWS_LWA_PORT=8080
ENV READINESS_CHECK_PATH=/

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
# Single worker: Lambda scales by spinning up more execution environments, not
# more workers per container. --timeout 0 disables gunicorn's worker-timeout
# watchdog, which otherwise trips spuriously because Lambda freezes the sandbox
# between invocations (the real request timeout is enforced by Lambda itself).
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--timeout", "0", "app:app"]

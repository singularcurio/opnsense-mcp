FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY opnsense_mcp/ ./opnsense_mcp/

RUN pip install uv && \
    UV_NO_SOURCES=1 uv pip install --system --no-cache .

ENV OPNSENSE_MCP_TRANSPORT=sse
ENV OPNSENSE_MCP_HOST=0.0.0.0
ENV OPNSENSE_MCP_PORT=8000

EXPOSE 8000

CMD ["opnsense-mcp"]

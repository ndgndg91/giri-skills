# Logging Strategy & Cost Optimization

## 1. Log Collection & Aggregation
- **Collection**: Use **Fluent Bit** as the lightweight log processor.
- **Aggregator Selection**:
  - **Standard (Cost-Optimized)**: Use **Grafana Loki**.
    - **Why**: Loki only indexes metadata (labels) and stores logs in S3, providing massive cost savings (up to 90%) compared to full-text indexing platforms.
    - **Tip**: Keep labels lean (low cardinality) to maintain index performance.
  - **Alternative**: Use **Datadog Logs** only for critical debugging where deep APM correlation and full-text search are indispensable.
- **Structured Logging**: All logs MUST be in **JSON format**.

## 2. Storage Tiering (Everything as S3)
- **Active Logs**: Keep logs indexed for 7-14 days in Loki/Datadog for troubleshooting.
- **Archive Logs**: Store logs in **Amazon S3** with **Glacier Deep Archive** for long-term compliance (90+ days).
- **TTL**: Define retention policies per application criticality.

## 3. Cost Reduction Tactics
- **Drop Success Logs**: Consider dropping high-volume 200 OK logs for internal health checks.
- **Sampling**: Apply sampling to high-throughput, non-critical log streams.
- **Source Filtering**: Use Fluent Bit to filter out unnecessary fields or log lines before they leave the node.

## 4. Observability Integration
- **Label Alignment**: Use identical labels (e.g., `app`, `env`, `region`) across Prometheus metrics and Loki logs to enable one-click navigation in Grafana.
- **Correlation**: Ensure `traceId` is present in every log for Trace-to-Log correlation.

## 5. Privacy & Compliance
- **Masking**: Mask PII (emails, tokens, SSNs) during log processing.
- **Audit Logs**: Maintain high-durability audit logs separately from system debug logs.

# Logging Strategy & Cost Optimization

## 1. Log Collection Architecture
- **Standard**: Use **Fluent Bit** as a lightweight log processor for EKS/Container environments. It consumes fewer resources than Fluentd.
- **Structured Logging**: All logs MUST be in **JSON format** for efficient parsing and indexing.
- **Aggregation**: Ship logs to a central platform (**Datadog**, ELK, or Grafana Loki).

## 2. Storage Tiering (Cost Optimization)
- **Hot Storage (0-15 days)**: High-speed indexing for active troubleshooting. Keep only the most recent logs in expensive platforms like Datadog or Elasticsearch.
- **Warm/Cold Storage (15-90+ days)**: Use cost-effective storage like **Amazon S3** for long-term retention and compliance. 
- **Log Archiving**: Configure automatic archiving from the active platform to S3. Restore logs to the active platform only when needed for historical analysis.

## 3. Cost Reduction Tactics
- **Log Level Management**: Ensure only `INFO` and above are logged in production. Use dynamic log level adjustment for temporary debugging.
- **Sampling & Filtering**: 
  - Filter out high-volume, low-value logs (e.g., frequent health checks, repeated success logs).
  - Use sampling for high-throughput non-critical services.
- **Drop at Source**: Drop unnecessary logs at the Fluent Bit (source) level to save network and ingestion costs.
- **TTL (Time To Live)**: Set strict TTL policies based on business and legal requirements. Do not keep logs indefinitely in indexed storage.

## 4. Privacy & Compliance
- **Masking**: Automatically mask PII (Personal Identifiable Information) at the logger level or during collection (Fluent Bit) before it reaches the storage.
- **Audit Logs**: Separate business audit logs (e.g., money transfer, permission changes) from system logs to ensure longer retention and higher durability.

## 5. Observability Integration
- **Correlation**: Ensure every log contains the **`traceId`** to allow seamless transition between Traces and Logs in Datadog.
- **Log-to-Metric**: Generate metrics from log patterns (e.g., count of specific error strings) to monitor trends without indexing every log line.

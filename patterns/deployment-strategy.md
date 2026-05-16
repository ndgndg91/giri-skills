# Deployment Strategy & Backward Compatibility

## 1. No-Downtime Deployment Types
- **Rolling Update**: Gradual replacement of instances. Requires backward compatibility during the overlap period.
- **Canary**: Traffic shifting to a small subset (e.g., 5%). Monitor metrics before full rollout.
- **Blue-Green**: Two identical environments. Instant switch and rollback.

## 2. Serialization & Backward Compatibility
During deployment, old and new versions of the application often coexist. Ensuring they can communicate is critical.

### 2.1. Caching (Redis)
- **Standard**: Use **JSON serialization** instead of Java Serialization to avoid `SerialVersionUID` mismatches.
- **Rule**: When adding a field, make it optional/nullable. When removing a field, ensure the new code can handle its absence.
- **Class Path**: Changing the package or class name of cached objects will break compatibility. Keep paths stable.

### 2.2. Messaging (Kafka)
- **Schema Evolution**: Use **Avro** or **Protobuf** with a Schema Registry for strict evolution rules, or use flexible JSON.
- **Forward/Backward**: Ensure the new consumer can read old messages, and the old consumer can read new messages (during rolling updates).

## 3. Rollback Strategy
- **Prerequisite**: Every deployment must have a pre-defined rollback plan.
- **Automated Rollback**: Trigger rollback if the error rate (5xx) or p99 latency exceeds a threshold during the deployment window.
- **Database Hook**: If a schema change (Expand phase) has occurred, ensure the rollback doesn't break the expanded schema.

## 4. Zero-Downtime Checklist
- [ ] No breaking changes in DB schema (Expand phase completed).
- [ ] Redis/Kafka models are backward compatible.
- [ ] Graceful shutdown and Warm-up are configured.
- [ ] Health check endpoints (/liveness, /readiness) are active.

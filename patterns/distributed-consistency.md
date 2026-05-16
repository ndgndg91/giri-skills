# Distributed Data Consistency Guide (MSA)

## 1. Beyond Distributed Transactions (Anti-2PC)
- **Problem with 2PC**: Two-Phase Commit causes blocking, high latency, and single points of failure.
- **Principle**: Embrace **Eventual Consistency** instead of strong consistency for high scalability and availability.

## 2. Saga Pattern
Manage long-running business processes across multiple services using compensation logic.

### 2.1. Choreography-Based Saga
- **Mechanism**: Each service publishes events and reacts to events from other services.
- **Pros**: Loose coupling, no central point of failure.
- **Cons**: Difficult to track the global state; high risk of cyclic dependencies.

### 2.2. Orchestration-Based Saga
- **Mechanism**: A central **Orchestrator** service tells participants which local transactions to execute.
- **Pros**: Centralized control and visibility of the workflow; easier to handle complex logic.
- **Cons**: Orchestrator can become a "God Class" or a central point of coupling.

### 2.3. Compensating Transactions
- Every step in a Saga must have a corresponding "undo" action (Compensating Transaction) to restore consistency if a subsequent step fails.

## 3. TCC (Try-Confirm-Cancel)
Use for scenarios requiring immediate resource reservation (e.g., payment, booking).
- **Try**: Reserve necessary resources (e.g., block the balance).
- **Confirm**: Permanently apply the changes.
- **Cancel**: Release the reserved resources if failure occurs.

## 4. Crucial Implementation Patterns
- **Transactional Outbox**: Use an Outbox table to guarantee that the database update and event publishing happen atomically.
- **Idempotent Consumers**: Ensure that processing the same event multiple times has no side effects.
- **Dead Letter Queues (DLQ)**: Handle messages that cannot be processed after multiple retries.

## 5. Decision Matrix
- **Strict, Real-time Consistency**: Use **TCC**.
- **Loose Coupling, High Throughput**: Use **Choreography Saga**.
- **Complex Workflows, Better Monitoring**: Use **Orchestration Saga**.

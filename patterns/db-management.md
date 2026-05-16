# Database Schema Management & No-Downtime Strategy

## 1. Code-Based Schema Migration (Flyway)
- **Standard**: All database schema changes must be managed via **Flyway** (or Liquibase) migration scripts versioned in Git.
- **Rule**: Once a migration script is merged, it must NEVER be modified. Create a new migration script for any further changes.
- **Verification**: Run migrations against a Testcontainer during the CI process to ensure SQL validity.

## 2. No-Downtime Schema Change (Expand-Contract Pattern)
To avoid downtime during deployment when modifying the schema, follow these phases:

### Phase 1: Expand (Additive Change)
- Add new columns or tables.
- Keep old columns/tables intact.
- Application: Start writing to both old and new columns, but still read from the old.

### Phase 2: Migrate (Data Sync)
- Migrate existing data from old columns to new columns (via background job or script).
- Application: Switch to reading from the new column, but continue writing to both.

### Phase 3: Contract (Cleanup)
- Application: Stop using the old column entirely (stop writing).
- DB: Drop the old column/table after confirming safety in production.

## 3. Indexing Strategy
- **Design**: Indexes must be designed based on actual query patterns (Explain Plan analysis).
- **Online Indexing**: Use `CREATE INDEX CONCURRENTLY` (PostgreSQL) or similar online options to prevent table locking during production.
- **Redundancy**: Periodically audit and remove unused or redundant indexes to improve write performance.

## 4. Performance & Safety
- **Avoid Large Transactions**: Split large data migrations into smaller chunks to avoid long-held locks.
- **Constraints**: Be cautious when adding NOT NULL constraints to existing columns; provide a default value first or handle it in the Expand phase.

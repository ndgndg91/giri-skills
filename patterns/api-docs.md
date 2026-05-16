# API Documentation & Contract Testing

## 1. Spring REST Docs
- **Standard**: Use **Spring REST Docs** instead of Swagger for reliable documentation.
- **Benefit**: Ensures that documentation is only generated if the tests pass, preventing out-of-date docs.
- **Usage**: Integrate with JUnit 5 to generate snippets during the build process.

## 2. Consumer-Driven Contract Testing (Pact)
- **Problem**: In MSA, changes in the Provider (Server) can break the Consumer (Client) without warning.
- **Solution**: Use **Pact** to define contracts from the Consumer's perspective.
- **Process**:
  1. Consumer defines requirements in a Pact file.
  2. Provider verifies its implementation against the Pact file.
  3. Prevents integration failures before deployment.

## 3. API Catalog
- Maintain a central catalog (or portal) where all service APIs and their Pact status are visible.

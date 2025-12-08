# PRODUCT DISSECTION OF UBER: RIDE-HAILING PLATFORM

This project provides an in-depth analysis of Uber’s transformative approach to urban mobility, focusing on how technology-driven innovation addresses key challenges in reliability, transparency, safety, and efficiency.

## Objectives
1. Analyze Uber’s core product features and their impact on solving real-world problems.
2. Present a case study highlighting an operational challenge faced by Uber.
3. Design a robust database schema to support Uber’s primary business flows.
4. Justify schema design decisions with clear, evidence-based rationale.
5. Visualize the schema using an Entity-Relationship (ER) Diagram.
6. Summarize findings for effective stakeholder communication.

## Approach
Uber’s unique strategy and advanced technology are examined to understand how the company solves complex urban transportation problems. The analysis of Uber’s top features forms the foundation for the database schema design.

### Conceptual Model
The conceptual model captures the essential entities and data flows within Uber’s business. This model is the first step in database design, focusing on seven main entities and their cardinality relationships.

### Logical Model
Each entity from the conceptual model is expanded into a logical model, detailing attributes and relationships. The schema adheres to third normal form (3NF) for optimal data integrity and efficiency. Key entities include: User, Driver, Ride, Payment, Fare & Pricing, Rating & Review, and Support Ticket. Primary and foreign keys are defined to ensure relational consistency.

### Physical Model
The physical model is represented by an ER Diagram, illustrating entities, attributes, data flows, and cardinality. The design prioritizes efficiency, integrity, and scalability, aligning with Uber’s commitment to a seamless and reliable ride-sharing experience.

## AWS RDS Integration
The second phase involves connecting to Amazon Web Services (AWS) Relational Database Service (RDS):
- A PostgreSQL database instance is provisioned via the AWS console.
- The local environment connects to the instance using the `psycopg2` library, with appropriate inbound rules and public accessibility configured.
- Database creation is automated in Python, including logic to check for existing databases and handle naming conflicts. The database is named `uber_db` upon successful creation.
- Tables are created according to the ER Diagram, and sample data is inserted for validation.

This end-to-end solution delivers a scalable, cloud-based database architecture ready for further analysis and operational use.
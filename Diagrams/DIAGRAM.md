# Architectural Design: UML Diagrams

## 1. UML Package Diagram (Logical Architecture)

The Package Diagram illustrates the high-level organization of the codebase into distinct, functional modules (packages) and their dependencies. This confirms the separation of concerns across core features.

![UML Package Diagram](screenshots/package.png)


## 2. UML Class Diagram (Database Schema)

The Class Diagram focuses on the **Model** layer, showing the primary data entities and their **One-to-Many** relationship as defined by Flask-SQLAlchemy.

![UML Class Diagram](screenshots/umldiagram.png)
# Rule Engine with AST

## Project Overview

The project implements a 3-tier rule engine that evaluates user eligibility based on dynamic rules. The rules are represented using an Abstract Syntax Tree (AST), allowing for flexible creation, modification, and evaluation.

Code Structure

src/: Contains the core logic, including rule creation, evaluation, and AST management.

app.py: The main Flask API for handling HTTP requests.

rule_engine.py: Contains logic for AST generation, rule evaluation, and combination.

requirements.txt: Lists Python dependencies.

docker-compose.yml: Defines Docker containers for Flask and MongoDB.

tests/: Contains unit tests for the rule engine.

## Installation Instructions

1. **Clone the repository:**
    ```bash
    git clone [https://github.com/yourhandle/rule-engine-with-ast.git](https://github.com/jatinraj2407/Rule-Engine-with-AST)
    cd Rule-Engine-with-AST
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```bash
    python src/rule_engine.py
    ```

4. **Alternatively, run the application using Docker:**
    ```bash
    docker-compose up
    ```

## API Endpoints

- **`POST /create_rule`**
  - **Input:**
    ```json
    {
      "rule_name": "rule1",
      "rule": "(age > 30 AND department == 'Sales')"
    }
    ```
  - **Output:**
    ```json
    {
      "rule_name": "rule1",
      "ast": "AST Representation"
    }
    ```

- **`POST /evaluate_rule`**
  - **Input:**
    ```json
    {
      "rule_name": "rule1",
      "data": {
        "age": 35,
        "department": "Sales",
        "salary": 60000
      }
    }
    ```
  - **Output:**
    ```json
    {
      "result": true
    }
    ```

## Design Choices

- **AST Representation:** The Abstract Syntax Tree (AST) allows dynamic parsing and manipulation of rules.
- **Error Handling:** Invalid rule strings or malformed data result in meaningful error responses.
- **Rule Modification:** Existing rules can be modified by updating their corresponding ASTs using the `/modify_rule` endpoint.

## Dependencies

- Python 3.9
- Flask (for the API)
- MongoDB (optional, for persistent rule storage)
- Docker & Docker Compose (for containerized environments)

## Testing

The project includes test cases for rule creation, combination, and evaluation. To run the tests, use the following command:

python -m unittest src/tests.py

## Docker Setup

To run the application using Docker (with MongoDB for rule persistence):

Build and run the containers:

docker-compose up

Access the API on http://localhost:5000


The Docker setup includes:

Flask API running in a web container.

MongoDB for rule storage (if desired).

## Conclusion
This project provides a fully functional rule engine with the ability to create, evaluate, and modify rules using an AST structure. It is containerized for easy deployment using Docker and includes comprehensive error handling and test coverage.


### Key Improvements:
1. **Clear structure** for installation, API endpoints, and Docker setup.
2. **Test instructions** provided for running unit tests.
3. **Modular description** for both Python and Docker environments.
4. **Well-organized** content and formatting for ease of use.

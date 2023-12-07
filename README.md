# Microservice

[![Install Dependencies](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/install.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Lint Code](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/lint.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Run Tests](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/test.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Format Code](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/format.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)



## Description

Our microservice leverages Flask to provide a responsive and scalable web interface. This microservice is designed as a core component of a larger distributed system, specifically focused on handling product order processing. It acts independently but is seamlessly integrated with the overall data pipeline, offering high responsiveness and efficiency. It's engineered to handle user inputs such as product selections and shipping details. Once an order is placed, it's processed and stored in a SQL database. The service then performs data transformations to provide valuable insights like the top three popular products in a customer's state, enhancing the user experience. 

## Architecture

![Alt text](<architecture.png>)

The provided architectural diagram visually represents our system's components: the web interface, Flask server, database, and data processing modules. These components interact to offer a streamlined order handling process, from user input through data storage and analysis.

## Usage

The app is cloud hosted using Azure at https://shopnozama.azurewebsites.net/. Here users will be able to place orders for any product in the drop down menu which display an image and price. From there after submitting the form, users will be redirected to their confirmation page base on their unique order number. 
"/orders/<order_num>"

Locally, you can also run the app by either building the Docker file or installing requirements.txt manually and running ```python src/main.py```. Here the same application will be hosted at localhost:5000 in development mode. 
- Note: in order to use the application locally, need to create a .env file with the DB username and password to connect to the cloudhosted DB.

### Makefile
`make install` to install, `make lint` to lint, `make format` to format, `make test` to perform tests

## Load Testing

Our load testing, achievable via make load_test commands, ensures the microservice can handle up to 10,000 requests per second, demonstrating its capability to perform under high-traffic conditions.

`make load_test` to perform load test, `make load_test_gui` to load test the GUI.

## Data Engineering 

We utilize pyodbc for its robust SQL Server connectivity, facilitating efficient data transactions and storage. This choice enhances our system's ability to handle large volumes of data with high reliability.

## Infrastructure as Code (IaC)

Our project employs ____ for infrastructure management, allowing us to define and deploy all necessary infrastructure resources programmatically and reliably.

## Continuous Integration and Continuous Delivery (CI/CD)

Our CI/CD pipeline, built with GitHub Actions, automates our development lifecycle processes. The workflows in .github/workflows – namely format.yml, install.yml, lint.yml, main.yml, and test.yml – ensure consistent code quality and streamlined deployment.

## Dockerization

We used Distroless Docker images to containerize the microservice, focusing on security and minimalism. The Dockerfile provided in the repository guides you through building and running the Docker container, encapsulating all dependencies.

## Limitations and Improvements

Currently, the microservice is optimized for SQL databases, which might limit integration with other types of databases. Future iterations could include broader database support and enhanced data analytics features.

## Teamwork Reflection

Our teamwork journey highlights the collaborative efforts, challenges overcome, and key learnings acquired during the project development.

[Team Feedback Summary Session](https://docs.google.com/document/d/1FhYV9NSEcUmWtFA6TKe7yPiDxYkE_7HvlgDf3IihQFo/edit?usp=sharing)

[Mike Keohane Team Reflection](https://docs.google.com/document/d/1ixz9MsmHOmnCAyjcn5keo54dAh_d98hUWenSYfierVU/edit?usp=sharing)

[Daniel Medina Team Reflection](https://docs.google.com/document/d/1ViY7u3oRpLIyjkn9Te6N8OfZiC_zlpbdrlPW3Pj0jus/edit?usp=sharing)

[Nick Strauch Team Reflection](https://docs.google.com/document/d/11x82q40JyLOvZKL-fGyUzPQr8a5qsNOlg0JN-oE_UN0/edit?usp=sharing)

[Nick Conterno Team Reflection](https://docs.google.com/document/d/1jnJnaYOIGLPxsWdKwUis8FfXEBNhDxDolO_yqYPvaAE/edit?usp=sharing)

[Tommy McGuire Team Reflection](https://docs.google.com/document/d/1VeugUnDxT4jfaOQPQwAEz4hCPmvNAvmbmUhytG7h_2Y/edit?usp=sharing)

# Microservice

[![Install Dependencies](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/install.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Lint Code](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/lint.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Run Tests](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/test.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Format Code](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/format.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)

[![Python Autoactions](https://github.com/mkeohane01/python_template/actions/workflows/main.yml/badge.svg)](https://github.com/mkeohane01/python_template/actions/workflows/main.yml)


## Description

Our microservice leverages Flask to provide a responsive and scalable web interface. This microservice is designed as a core component of a larger distributed system, specifically focused on handling product order processing. It acts independently but is seamlessly integrated with the overall data pipeline, offering high responsiveness and efficiency. It's engineered to handle user inputs such as product selections and shipping details. Once an order is placed, it's processed and stored in a SQL database. The service then performs data transformations to provide valuable insights like the top three popular products in a customer's state, enhancing the user experience. 

## Architecture

![Alt text](<architecture.png>)

The provided architectural diagram visually represents our system's components: the web interface, Flask server, database, and data processing modules. These components interact to offer a streamlined order handling process, from user input through data storage and analysis.

## Usage

After setting up your environment and installing dependencies, you can interact with the microservice through a simple web interface. Fill out the product order form, and upon submission, you will receive an order confirmation. For detailed order information, navigate to http://127.0.0.1:5000/orders/<order_num>.

- Set up a virtual environment 
    - run "python -m venv 'name of virtual environment'
    - "source 'name'/bin/activate

- Install dependencies
 
- Open index.html in browser

-  to run flask server
```bash
cd src
python main.py
```
- Should be able to fill out form in html
    - get order confirmation in browser

- Visit http://127.0.0.1:5000/orders/<order_num> to view order

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

Our teamwork journey, documented "here" (provide link), highlights the collaborative efforts, challenges overcome, and key learnings acquired during the project development.

## To Use

- Load requirements and make venv ofc

- Open index.html in browser

-  to run flask server
```bash
cd src
python main.py
```
- Should be able to fill out form in html
    - get order confirmation in browser

- Visit http://127.0.0.1:5000/orders/<order_num> to view order

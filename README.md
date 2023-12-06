# Microservice

[![Install Dependencies](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/install.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Lint Code](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/lint.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Run Tests](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/test.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Format Code](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/format.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)

[![Python Autoactions](https://github.com/mkeohane01/python_template/actions/workflows/main.yml/badge.svg)](https://github.com/mkeohane01/python_template/actions/workflows/main.yml)


## Description

This project utilizes the `Flask` framework to build a microservice that interfaces with a data pipeline. The front end includes a user interface where individuals can place product orders for the product of their choose. They input the desired product, quantity, and shipping location. This data is stored in a database, undergoes data transformation, and relevant information is passed back to the user such as the top 3 products ordered in their state. 

## Architecture

![Alt text](<Screenshot 2023-12-06 at 1.05.36 AM.png>)

## Usage

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
`make load_test` to perform load test, `make load_test_gui` to load test the GUI.

## Data Engineering 

This project uses pyodbc to allow open database connectivity, in this case SQL Server. 

## Infrastructure as Code (IaC)

## Continuous Integration and Continuous Delivery (CI/CD)

This project employs continuous integration and continuous delivery through the use of GitHub Actions.

## Dockerization

- How it was built and run

## Limitations and Improvements

## Teamwork Reflection

(Link)

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

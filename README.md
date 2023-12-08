# Microservice

[![Install Dependencies](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/install.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Lint Code](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/lint.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Run Tests](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/test.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Format Code](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/format.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/workflow-name.yml)
[![Continous Deployment](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/continuousdelivery.yml/badge.svg)](https://github.com/mkeohane01/IDS706-Microservice/actions/workflows/continuousdelivery.yml)



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

### Example

<img width="1438" alt="Screenshot 2023-12-07 at 10 57 10 PM" src="https://github.com/mkeohane01/IDS706-Microservice/assets/141086024/1e16aa74-462d-4d6b-b5f4-57b38104f478">


<img width="472" alt="Screenshot 2023-12-07 at 10 54 18 PM" src="https://github.com/mkeohane01/IDS706-Microservice/assets/141086024/86b2e8ae-c2e0-404f-bbbc-8e64e8a1d3f4">


### Makefile
`make install` to install, `make lint` to lint, `make format` to format, `make test` to perform tests

### Database
We host our database on Azure, using a general purpose V5 instance with 2 cores. Our database has two tables, one which stores all of the products, and one which keeps track of all of the orders that are placed. 

## Load Testing

### Objective: Achieving 10,000 Requests Per Second

Through our streamlined load testing process, accessible via `make` commands, we've rigorously evaluated our service's performance under high-traffic scenarios. Here's what we discovered:

- Flask Server Health Check: Using `make load_test`, we can push over 5,000 requests per second, showcasing robust responsiveness.
- Full Data Pipeline Performance: With `make load_test_datapipe_gui`, we observed a throughput of 200 requests per second. This is primarily constrained by the database's capacity for data storage and retrieval and spending limits.

- We were able to get to about 4600 requests per second by using 18 instances of a premium azure web app, while implementing some load management strategies. Unfortunately, this costs quite a bit of money, and therefore we have since scaled back to manage the cost. With access to more instances, and perhaps a more expensive instance type, we may be able to reach 10,000, but at the momenet we lack the funds to accomplish this task. A graph of the performance using locust at our peak is shown below:
![Alt text](total_requests_per_second_1701983455.png) 


### Interactive Testing Tools:

- `make load_test_gui`: Launches an intuitive, locally-hosted interface for real-time load testing and analysis of the Flask server.
- `make load_test_datapipe_gui`: Extends this capability to the entire data pipeline, offering a hands-on, visual approach to performance assessment.

Each tool is designed to give us a comprehensive understanding of our system's limits and areas for improvement, guiding us toward our ultimate goal of 10,000 requests per second.

## Data Engineering 

We utilize pyodbc for its robust SQL Server connectivity, facilitating efficient data transactions and storage. This choice enhances our system's ability to handle large volumes of data with high reliability. This also requires an extra download of msodbcsql18 which cannot be installed via pip. This is automatically downloaded via the docker image on linux, however.

## Infrastructure as Code (IaC)

Our project employs Azure Resource Manager (ARM) for infrastructure management, allowing us to define and deploy all necessary infrastructure resources programmatically and reliably.

## Continuous Integration and Continuous Delivery (CI/CD)

Our CI/CD pipeline, built with GitHub Actions, automates our development lifecycle processes. The workflows in .github/workflows – namely format.yml, install.yml, lint.yml, continuousdelivery.yml, and test.yml – ensure consistent code quality and streamlined deployment.

Our web application automatically detects changes in dockerhub, and because we continuously deliver to docker, we thereby continuously deliver to our web app on Azure.

## Dockerization

We used Distroless Docker images to containerize the microservice, focusing on security and minimalism. The Dockerfile provided in the repository guides you through building and running the Docker container, encapsulating all dependencies.

## Limitations and Improvements

At present, our microservice is tailored for optimal performance with SQL databases. This specialization, while efficient, narrows our compatibility with diverse database systems. Looking ahead, we are focusing on two pivotal enhancements:

1. Broader Database Integration: Future updates will introduce support for a variety of database types, including NoSQL databases like MongoDB and Cassandra, and NewSQL databases like Google Spanner. This expansion will not only diversify our data management capabilities but also cater to a wider range of application requirements.

2. Advanced Data Analytics Features: Alongside broader database support, we aim to incorporate sophisticated data analytics functionalities. This could involve integrating with databases designed for large-scale data processing, such as Apache Hadoop or Google BigQuery, enhancing our ability to handle complex data sets and deliver deeper insights.

These advancements will position our microservice as a more versatile and powerful tool, capable of seamlessly integrating with a range of database ecosystems and addressing more complex data analysis needs.

## Teamwork Reflection

Our teamwork journey highlights the collaborative efforts, challenges overcome, and key learnings acquired during the project development.

[Team Feedback Summary Session](https://docs.google.com/document/d/1FhYV9NSEcUmWtFA6TKe7yPiDxYkE_7HvlgDf3IihQFo/edit?usp=sharing)

[Mike Keohane Team Reflection](https://docs.google.com/document/d/1ixz9MsmHOmnCAyjcn5keo54dAh_d98hUWenSYfierVU/edit?usp=sharing)

[Daniel Medina Team Reflection](https://docs.google.com/document/d/1ViY7u3oRpLIyjkn9Te6N8OfZiC_zlpbdrlPW3Pj0jus/edit?usp=sharing)

[Nick Strauch Team Reflection](https://docs.google.com/document/d/11x82q40JyLOvZKL-fGyUzPQr8a5qsNOlg0JN-oE_UN0/edit?usp=sharing)

[Nick Conterno Team Reflection](https://docs.google.com/document/d/1jnJnaYOIGLPxsWdKwUis8FfXEBNhDxDolO_yqYPvaAE/edit?usp=sharing)

[Tommy McGuire Team Reflection](https://docs.google.com/document/d/1VeugUnDxT4jfaOQPQwAEz4hCPmvNAvmbmUhytG7h_2Y/edit?usp=sharing)

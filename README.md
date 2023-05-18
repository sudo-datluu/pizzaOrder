# Pizza Ordering App - Project Structure

This repository contains the source code for the Pizza Ordering App.
This app help handle request from client web base and give response as json data for each request.
Below you will find an overview of the project structure and organization.

## Project Structure

The project structure is organized as follows:

pizzaOrder/
├── api/ # The backend application 
│ ├── models/ # Module contain the data type of the objects
│ ├── serializers # Module help to connect the database to the desired structure to request
│ └── views/ # Functions handle api request
├── urls.py # File defines url pattern for api 
├── pizzaOrdering/ # Main project application
│ ├── settings # Setting of the project
│ ├── urls # Construct pattern for all application in the project
├── .gitignore 
├── README.md
└── manage.py # File manage the project
└── requirements.txt # Requirement package
└── vercel.json # Config file for vercel deployment 
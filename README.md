# Pizza Ordering App - Project Structure

This repository contains the source code for the Pizza Ordering App.
This app help handle request from client web base and give response as json data for each request.
Below you will find an overview of the project structure and organization.

## Project Structure

The project structure is organized as follows:

pizzaOrder/
├── api/ # The backend application  <br>
│ ├── models/ # Module contain the data type of the objects  <br>
│ ├── serializers # Module help to connect the database to the desired structure to request  <br>
│ └── views/ # Functions handle api request  <br>
├── urls.py # File defines url pattern for api  <br>
├── pizzaOrdering/ # Main project application  <br>
│ ├── settings # Setting of the project  <br>
│ ├── urls # Construct pattern for all application in the project  <br>
├── .gitignore  <br>
├── README.md <br>
└── manage.py # File manage the project <br>
└── requirements.txt # Requirement package <br>
└── vercel.json # Config file for vercel deployment  <br>

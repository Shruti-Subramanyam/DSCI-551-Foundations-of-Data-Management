# Local Food Exchange Network Application

## Overview

The Local Food Exchange Network is a web-based application designed to connect local farmers with customers to facilitate the discovery and purchase of locally sourced food products. Developed as part of the DSCI551 Spring 2024 coursework at USC, this project implements a distributed database that stores data across two NoSQL systems, managed by a hash function.

## Team Contributions

- **Shruti Subramanyam**: Focused on frontend development using Streamlit, crafting the user interfaces for the web application and connecting them to backend service.
- **Kyosuke Chikamatsu**: Concentrated on backend development, including database management and ensuring data integrity across the distributed system.

## Getting Started

### Prerequisites
- Docker Desktop must have been installed and run previously (Please refer to https://docs.docker.com/desktop/install/mac-install/).
  Windows users need to install Linux distribution by using WSL as well (Please refer to https://learn.microsoft.com/ja-jp/windows/wsl/install).
  In addition, Windows users need to have docker enable integration with the Linux distribution (Please check Settings/Resources/WSL integration on your Docker Desktop).
  Windows users will execute Docker commands in your Linux distribution terminal. Mac users will execute Docker commands in your terminal.

### Installation and Setup
1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Execute the following command to start the application:

    ```sh
    docker-compose up -d
    ```

### Accessing the Application
Once the application is running, open your web browser and go to the following URL to access the web interface:

- Web application for end users (user and farmer) - http://localhost:8501
- User itnerface for database managers (administrator) - http://localhost/docs

### Importing Sample Data
Once the application is running, you can load sample data with the following command:

```sh
./import_data.sh
```

If you need, you can delete all data with the following command:

```sh
./clear_data.sh
```

To execute `clear_data.sh`, you may need to install jq with the following command:

```sh
sudo apt-get update
sudo apt-get install jq
```

## Uniqueness:
- `features`: Unique feature that we added in our application.
  - Contact Us Page:  Users can contact us if they have any issues/queries, the database manager will get an email regrading the query.
- `Edge cases`: We have handled below mentioned edge cases in our application.
  - Empty information is not acceptable for all the buttons e.g. if the button is clicked without any data it gives an error message.
  - In the farmer page: The farmer cannot add duplicate products.
  - In the user page: The user can not add products more than inventory to cart or add negative product quantity, if they do an error message will be displayed in such cases.
  - All the buttons will be locked unless the user finishes the current task e.g. only after check out user can write a review.

## Application Structure

- `fastapi/`: Contains FastAPI backend logic with CRUD operations for the database manager.
  - `app/`: The main directory for FastAPI application.
    - `crud.py`: Functions for creating, reading, updating, and deleting database entries.
    - `main.py`: Entry point for the FastAPI application, defining the API endpoints.
    - `routes_farmer.py`: API routes specific to farmer operations.
    - `routes_user.py`: API routes specific to user operations.
    - `schema.py`: Pydantic schemas for data validation.
  - `Dockerfile`: Docker configuration for FastAPI application.
  - `requirements.txt`: List of Python dependencies for FastAPI.

- `streamlit/`: Holds the Streamlit frontend interface.
  - `pages/`: The main directory for Streamlit application.
    - `1_Farmer.py`: Contains frontend code for the farmer page.
    - `2_User.py`: Contains frontend code for the User page.
    - `3_Products.py`: Contains frontend code to display list of all the products.
    - `4_Contact_Us.py`: Contains frontend code for Contact Us page.
  - `Welcome.py`: Contains frontend of the main page of the local food exchange application.
  - `Dockerfile`: Docker configuration for Streamlit application.
  - `requirements.txt`: List of Python dependencies for Streamlit.
  - `style.css`: Custom CSS styles for the Streamlit interface.
  - `logo.png`: Image of the logo which is displayed in the frontend.
  - `vegepic.jpg`: Image of vegetables which is displayed in the frontend.

- `env/`: Environment variables and configuration files.

- `README.md`: Documentation and instructions for setting up and running the application (this file).

- `compose.yaml`: Docker Compose file to orchestrate the multi-container setup.

- `import_data.sh`: Loading sample data for testing the application.

- `clear_data.sh`: Removing all data from the database.

## Future Work

Further development can include features such as payment integration, extended user profiles, and a more detailed analytics dashboard for farmers to track sales and product performance.

## Contact

For any inquiries regarding the Local Food Exchange Network application, please reach out to the contributors:

- Shruti Subramanyam - shrutisu@usc.edu 
- Kyosuke Chikamatsu - chikamat@usc.edu

We appreciate your interest in our project and welcome any feedback or contributions!

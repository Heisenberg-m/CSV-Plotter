# xVectorlabs
xVectorlabs project submission

# CSVUploader Web Application

The CSVUploader is a web application built using Django that allows users to upload CSV files, visualize data through plots, and perform calculations on the data columns. This README provides an overview of the project structure, functionalities, and how to set up and run the application.

## Features

- Upload CSV files.
- Visualize data through scatter plots using Plotly.js.
- Perform calculations on selected columns (min, max, sum).
- User-friendly interface for selecting files, columns, and functions.
- Backend data processing using Pandas.
- API endpoints for retrieving data and calculation results.

## Project Structure

The project is structured as follows:

- `csvuploader/`: Django project root directory.
  - `csvapp/`: Django app containing application-specific code.
    - `models.py`: Defines the `UploadedFile` model for storing uploaded CSV files.
    - `views.py`: Contains views for rendering HTML templates and handling requests.
    - `api.py`: Defines API views for data retrieval and calculations.
    - `urls.py`: Defines URL routing for views and API endpoints.
    - `templates/`: Contains HTML templates for rendering pages.
      - `csvapp/`: Templates for the `csvapp` app.
    - `static/`: Contains static assets (CSS, JavaScript, images).
      - `js/`: JavaScript files for enhancing frontend interaction.
  - `csvuploader/`: Project settings and configuration.
  - `media/`: Directory where uploaded files are stored.

## Setup and Usage

1. Clone the repository to your local machine:

git clone https://github.com/yourusername/csvuploader.git
cd csvuploader

2. Install the required dependencies:
pip install -r requirements.txt

3.Apply database migrations:
python manage.py migrate

4.Run the development server:
python manage.py runserver

5.Access the application in your web browser at `http://localhost:8000`.






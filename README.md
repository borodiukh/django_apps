### ToDo App
This project is a simple to-do list application built using Django. 
It allows users to manage tasks by adding, updating, and deleting them. 
The application provides a clean interface for organizing daily tasks efficiently.


### Weather App
This Django project allows users to input a city and receive a 7-day weather forecast.
It retrieves weather data from the WeatherAPI, handles errors like invalid locations or API keys, 
and displays the forecast with city information and weather icons.


### Getting Started

Follow these steps to set up and run the project:

1. Clone the repository using the command: `git clone https://github.com/borodiukh/django_apps.git`
2. Navigate to the repository folder and create a virtual environment. `python -m venv venv` command for Windows
3. Activate the virtual environment. `source ./venv/Scripts/activate` command for Windows
4. Ensure that Python is installed on your system.
5. Install the required packages from the `requirements.txt` file. (`pip install -r requirements.txt`)
-------------------------------------------------------------------------------------------------------
6.1. To run the weather app, you need to obtain your own API key.
6.2. You can acquire your API key from the following website: [Weather API](https://www.weatherapi.com/)
6.3. Inside main folder create a new `.env` file.
6.4. Inside the `.env` file, add your API key using the format: `API_KEY={your_api_key}`


### Project launch
1. In the main project folder, run the command: `python manage.py runserver`.
2. Access the project by visiting: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)



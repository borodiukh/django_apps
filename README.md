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

1. Clone the repository using the command: `git clone <repository_url>`
2. Navigate to the repository folder and create a virtual environment.
3. Activate the virtual environment.
4. Ensure that Python is installed on your system.
5. Install the required packages from the `requirements.txt` file. (`pip install -r requirements.txt`)
6. In the main project folder, run the command: `python manage.py runserver`.
7. Access the project by visiting: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

8. To run the weather app, you need to obtain your own API key.
9. You can acquire your API key from the following website: [Weather API](https://www.weatherapi.com/)
10. Create a new `.env` file.
11. Inside the `.env` file, add your API key using the format: `API_KEY={your_api_key}`


# Asset-Manager


## Description
Provide a brief description of your project here.

## Prerequisites
- Python 3.x
- pip package manager

## Getting Started
Follow the instructions below to get the project up and running on your local machine.

### Clone the Repository
1. Open a terminal/command prompt.
2. Change to the directory where you want to clone the repository.
3. Run the following command:
  ```
  git clone https://github.com/DevDenLab/Asset-Manager
  ```
4. Change to the project's directory:
   ```
   cd Asset-Manager
  ```
### Create a Virtual Environment
1. It's recommended to create a virtual environment to isolate the project's dependencies.
2. Run the following command to create a virtual environment:
- For macOS and Linux:
  ```
  python3 -m venv env
  ```
- For Windows:
  ```
  python -m venv env
  ```

### Activate the Virtual Environment
1. Activate the virtual environment with the following command:
- For macOS and Linux:
  ```
  source env/bin/activate
  ```
- For Windows:
  ```
  .\env\Scripts\activate
  ```

### Install Dependencies
1. With the virtual environment activated, install the project's dependencies:
```
pip install -r requirements.txt
```
### Database Migration
1. Before running the server, perform any necessary database migrations.
```
python manage.py migrate
```
### Start the Server
1. You're now ready to start the server.
2. Run the following command:
```
python manage.py runserver
```
3. Open your web browser and visit `http://localhost:8000/catalog/home/` to view the application.

## Contributing
Specify guidelines for contributing to your project, if applicable.

## License
Provide information about the license under which your project is distributed.


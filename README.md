# Mbira Couture Sticky Notes

## Project Overview

Mbira Couture Sticky Notes is a Django web application developed to help users manage sticky notes for the Mbira Couture website.

## Features

- View sticky notes
- Create new sticky notes
- Edit existing sticky notes
- Delete sticky notes

## Technologies Used

- Python
- Django
- HTML and CSS
- SQLite

## Installation and Setup

### 1. Clone the repository

Clone the project repository from GitHub and navigate to the project directory.

### 2. Create a virtual environment

```bash
python -m venv myvenv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.\myvenv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open the local address displayed in your terminal in a web browser.

## Running Tests

To run the Django tests, execute:

```bash
python manage.py test
```

## Author

Zimbini Koto
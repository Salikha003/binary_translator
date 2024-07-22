# Binary Translator

Binary Translator is a web application built using Python and Django, allowing users to convert text to binary code and binary code back to text.

## Project Overview

Binary Translator enables users to translate text into binary code and vice versa. The application is built on the Django web framework and provides an intuitive interface for translation tasks.

## Installation

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/Salikha003/binary_translator.git
    ```

2. **Create a Virtual Environment**:

    ```sh
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:

    ```sh
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate  # Windows
    ```

4. **Install Required Packages**:

    ```sh
    pip install -r requirements.txt
    ```

5. **Apply Migrations**:

    ```sh
    python manage.py migrate
    ```

6. **Collect Static Files** (if needed):

    ```sh
    python manage.py collectstatic
    ```

## Usage

Once the project is up and running, open your browser and navigate to `http://127.0.0.1:8000/`. Enter text or binary code and click "Translate" to see the conversion.

## Running the Project

1. **Start the Django Development Server**:

    ```sh
    python manage.py runserver
    ```

2. **Access the Application**:

    Open your browser and go to `http://127.0.0.1:8000/` to interact with the application.

## Directory Structure

- `binary/`: Contains Django project files and settings.
- `static/`: Includes static files such as CSS, JavaScript, and images.
- `templates/`: Contains HTML templates.
- `translator/`: The Django app, including views, models, and other components.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For additional information or to report issues, you can contact:

- **Email**: solihahusniddinova@gmail.com
- **GitHub**: [Salikha003](https://github.com/Salikha003)

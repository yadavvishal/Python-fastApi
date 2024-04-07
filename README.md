# FastAPI MongoDB CRUD Application

This is a simple FastAPI application that demonstrates basic CRUD (Create, Read, Update, Delete) operations with MongoDB as the database backend. It provides endpoints to manage student data including creating, reading, updating, and deleting student records.

## Prerequisites

Before running this application, ensure you have the following prerequisites installed:

- Python 3.6+
- MongoDB
- Required Python packages (install using `pip install -r requirements.txt`)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/fastapi-mongodb-crud.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fastapi-mongodb-crud
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. MongoDB Connection URI:
   
   Update the `MONGODB_URI` variable in `main.py` with your MongoDB connection URI.

2. Running the Application

   Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

3. Access the API

   Once the application is running, you can access the API documentation and test the endpoints by visiting [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

## API Endpoints

### Create Student

- **URL:** `/students/`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
        "name": "John Doe",
        "age": 20,
        "address": {
            "city": "New York",
            "country": "USA"
        }
    }
    ```
- **Response:**

    ```json
    {
        "id": "abc123"
    }
    ```

### Get All Students

- **URL:** `/students/`
- **Method:** `GET`
- **Response:**

    ```json
    {
        "data": [
            {
                "name": "John Doe",
                "age": 20
            },
            {
                "name": "Alice Smith",
                "age": 22
            }
        ]
    }
    ```

### Get Student by ID

- **URL:** `/students/{student_id}`
- **Method:** `GET`
- **Response:**

    ```json
    {
        "name": "John Doe",
        "age": 20,
        "address": {
            "city": "New York",
            "country": "USA"
        }
    }
    ```

### Update Student

- **URL:** `/students/{student_id}`
- **Method:** `PATCH`
- **Request Body:**

    ```json
    {
        "age": 21
    }
    ```
- **Response:**

    ```json
    {}
    ```

### Delete Student

- **URL:** `/students/{student_id}`
- **Method:** `DELETE`
- **Response:**

    ```json
    {}
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Number Classification API

## Project Overview
This API is designed to classify numbers based on their mathematical properties and provide interesting facts about them. Given a number as input, the API determines if the number is prime, perfect, Armstrong, odd, or even. Additionally, it retrieves a fun fact about the number from the Numbers API.

---

## API Endpoints

### `/api/classify-number?number=371`

#### Description:
This endpoint accepts a GET request with a `number` parameter and returns its classification along with a fun fact.

#### Parameters:
- **number**: (Required) An integer value to classify.

#### Response Format:
- **200 OK**:
  ```json
  {
      "number": <integer>,
      "is_prime": <boolean>,
      "is_perfect": <boolean>,
      "properties": [<string>],
      "digit_sum": <integer>,
      "fun_fact": <string>
  }
  ```
  Example
    ```json
    {
      "number": 371,
      "is_prime": false,
      "is_perfect": false,
      "properties": ["armstrong", "odd"],
      "digit_sum": 11,
      "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
    }
    ```

    **400 Bad Request**:
    ```json
    {
      "number": <input_value>,
      "error": true
    }
    ```
    Example
      ```json
      {
        "number": "alphabet",
        "error": true
      }
      ```

## Installation instructions

### Prerequisites:
  Python 3.8+
  pip

### Steps:
  1. Clone the repository:
  ```bash
  git clone https://github.com/Bakarray/HNG12_stage_one
  cd number-classification-api
  ```
  2. Create a virtual environment:
  ```bash
  python -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate
  ```
  3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
  4. run development server:
  ```bash
  python manage.py runserver
  ```
  5. Access the API at http://127.0.0.1:8000/api/classify-number?number=<your_number>

## Usage Examples
### Using curl:
```bash
curl "http://127.0.0.1:8000/api/classify-number?number=371"
```
Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
Invalid Input:
```bash
curl "http://127.0.0.1:8000/api/classify-number?number=abc"
```
Response:
```json
{
    "number": "abc",
    "error": true
}
```
### Using Postman:
Open Postman.
Create a new GET request.
Set the URL to http://127.0.0.1:8000/api/classify-number?number=371.
Send the request and view the response.

## Dependencies
The following libraries are used in this project:
  Django : Web framework for building the API.
  Django Rest Framework (DRF) : Toolkit for building RESTful APIs.
  Requests : Library for making HTTP requests to fetch fun facts from the Numbers API.
  django-cors-headers : Middleware to handle Cross-Origin Resource Sharing (CORS).

## Deployment
The API is deployed and publicly accessible at:
https://numberclassification-cfy7.onrender.com/api/classify-number.json

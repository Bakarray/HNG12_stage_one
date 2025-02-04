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

# HNG-Project
This project provides an AWS Lambda-based API that accepts a number and returns interesting mathematical properties about it, along with a fun fact. The API evaluates whether the number is prime, perfect, an Armstrong number, computes its digit sum, and determines its parity (odd/even). Additionally, it fetches a fun mathematical fact from the Numbers API.

# Features
Input Validation: Ensures the provided input is a valid integer.
Mathematical Analysis:
Prime Check: Determines if the number is prime.
Perfect Number Check: Checks if the number is a perfect number.
Armstrong Check: Determines if the number is an Armstrong (narcissistic) number.
Digit Sum: Calculates the sum of the digits.
Properties List: Returns a list indicating if the number is:
An Armstrong number along with its parity (e.g., ["armstrong", "odd"] or ["armstrong", "even"])
Or simply its parity (e.g., ["odd"] or ["even"]) if it’s not an Armstrong number.
Fun Fact: Retrieves a fun fact about the number from the Numbers API using its math endpoint.
API Endpoint
The API is accessed via an HTTP GET request with a query parameter named number.

Example Request
ruby
Copy
Edit
GET /?number=371
Example Successful Response
json
Copy
Edit
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
Example Error Response
If the input is missing or invalid, the API returns a 400 Bad Request:

json
Copy
Edit
{
  "number": "alphabet",
  "error": true
}
Getting Started
Prerequisites
AWS Account: Access to AWS Lambda and API Gateway.
Python 3.x: The function is written in Python.
Dependencies:
The API uses the requests library to fetch the fun fact. Make sure to package this library with your Lambda deployment or include it as a Lambda Layer.

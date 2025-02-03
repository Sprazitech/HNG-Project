import json
import math
import requests

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    # Only need to test divisibility up to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if n is a perfect number.
       A perfect number is a positive integer that is equal to the sum of its proper divisors.
    """
    if n < 1:
        return False
    divisors = [1]  # 1 is always a divisor (for n > 1)
    # Loop to find divisors up to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors) == n

def is_armstrong(n):
    """Check if n is an Armstrong number.
       An Armstrong number (also known as narcissistic number) is a number that is the sum
       of its own digits each raised to the power of the number of digits.
       This check is only applied for non-negative integers.
    """
    if n < 0:
        return False
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d ** power for d in digits) == n

def digit_sum(n):
    """Return the sum of the digits of n. For negative numbers, sum the digits of its absolute value."""
    return sum(int(d) for d in str(abs(n)))

def get_properties(n, armstrong_flag):
    """Determine the properties list.
       - If the number is Armstrong, include 'armstrong' and then 'odd' or 'even'
       - Otherwise, only include 'odd' or 'even'
    """
    parity = "odd" if n % 2 != 0 else "even"
    if armstrong_flag:
        return ["armstrong", parity]
    else:
        return [parity]

def lambda_handler(event, context):
    """
    AWS Lambda handler function.
    Expected event format (via API Gateway GET request):
      {
         "queryStringParameters": {
              "number": "371"
         }
      }
    """

    # Extract the "number" parameter from the query string
    qs = event.get('queryStringParameters') or {}
    number_param = qs.get('number')

    # Input validation: if missing or not a valid integer, return error.
    if number_param is None:
        error_response = {"number": None, "error": True}
        return {
            "statusCode": 400,
            "body": json.dumps(error_response),
            "headers": {"Content-Type": "application/json"}
        }

    try:
        n = int(number_param)
    except ValueError:
        error_response = {"number": number_param, "error": True}
        return {
            "statusCode": 400,
            "body": json.dumps(error_response),
            "headers": {"Content-Type": "application/json"}
        }

    # Compute mathematical properties.
    armstrong_flag = is_armstrong(n)
    properties = get_properties(n, armstrong_flag)
    result = {
        "number": n,
        "is_prime": is_prime(n),
        "is_perfect": is_perfect(n),
        "properties": properties,
        "digit_sum": digit_sum(n),
    }

    # Get a fun fact from the Numbers API using the "math" endpoint.
    # Example URL: http://numbersapi.com/371/math?json
    try:
        api_url = f"http://numbersapi.com/{n}/math?json"
        response = requests.get(api_url)
        if response.status_code == 200:
            fun_fact = response.json().get("text", "")
        else:
            fun_fact = ""
    except Exception as ex:
        # In case of any error fetching the fun fact, leave it empty.
        fun_fact = ""

    result["fun_fact"] = fun_fact

    # Return a successful JSON response.
    return {
        "statusCode": 200,
        "body": json.dumps(result),
        "headers": {"Content-Type": "application/json"}
    }

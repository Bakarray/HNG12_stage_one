import requests, random

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return sum(d ** len(digits) for d in digits) == num

def get_properties(num):
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

def get_digit_sum(num):
    return sum(int(d) for d in str(num))

def get_fun_fact(num):
    types = ["trivia", "math", "date", "year"]
    selected_type = random.choice(types)
    url = f"http://numbersapi.com/{num}/{selected_type}"
    print("url:", url)
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("text", "No fun fact available.")
        return "Failed to fetch fun fact."
    except Exception as e:
        return f"Error fetching fun fact: {e}"
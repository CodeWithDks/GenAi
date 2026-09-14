from langchain_community.tools import tool


# Step 1:  create a function
def multiply(a,b):
    return a*b

# Step 2: add type hints
def multiply(a:int, b:int) -> int:
    return a*b

# Step 3: add tool decorator
@tool(description="Multiple two numbers.")
def multiply(a:int,b:int)->int:
    return f"Here is your multiplication: {a*b}"


# Step 1:  create a function
def add(a,b):
    return a+b

# Step 2: add type hints
def add(a:int, b:int) -> int:
    return a+b

# Step 3: add tool decorator
@tool(description="Add two numbers.")
def add(a:int,b:int)->int:
    return  f"Here is your addition: {a+b}"



operation =input('Enter your operation (add/multiply):').lower().strip()

if operation == "add":
    result = add.invoke({"a": 5, "b": 10})

elif operation == "multiply":
    result = multiply.invoke({"a": 5, "b": 10})

print(result)

print('-----------Details about Multiply tool--------------')
print(multiply.name)
print(multiply.description)
print(multiply.args)

print('-----------Details about add tool--------------')
print(add.name)
print(add.description)
print(multiply.args)

print("----------------schema-------------------------")
print(multiply.args_schema.model_json_schema())
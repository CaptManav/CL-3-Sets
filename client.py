import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://localhost:8000/")

num = int(input("Enter a number: "))
result = client.factorial(num)

print("Factorial is:", result)
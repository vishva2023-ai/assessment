def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Login Failed"

print(login("admin", "1234"))
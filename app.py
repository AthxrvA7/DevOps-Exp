# Hello World application for the GitHub Actions CI/CD pipeline
# small change made on the feature-update branch

def hello_world():
    return "Hello, DevOps"

def welcome_message(name):
    return f"Welcome to DevOps, {name}!"

if __name__ == "__main__":
    print(hello_world())
    print(welcome_message("Atharva"))
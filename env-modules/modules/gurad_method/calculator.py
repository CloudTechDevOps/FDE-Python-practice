def addition (a, b):
    return a + b
print("calculator module is loaded")

if __name__ == "__main__":
    print("This is a calculator module")
    print(addition (10, 5))
    
# when this condtion will be wrong if any one import this module in another module then this condition will be false and the code inside the if block will not be executed.
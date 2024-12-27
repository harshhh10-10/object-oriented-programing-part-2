class employee :
    def __init__(self):
        print("employee called")
    def __del__(self):
        print("destructor called")

obj1 =employee()
del obj1
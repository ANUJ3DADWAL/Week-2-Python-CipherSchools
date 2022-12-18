# if we use default parameter at the at starting then all other parameters are also become default parameters
# Therefore we mostly use default parameter at the end only
def user_info(first_name,last_name,age=20):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")



    print(user_info("Anuj","Dadwal"))    
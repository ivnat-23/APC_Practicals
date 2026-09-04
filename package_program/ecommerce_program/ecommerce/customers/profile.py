def update_profile(customer,name,email):
    customer[0]=name
    customer[1]=email
    return customer

def show_profile(customer):
    print("Name:",customer[0])
    print("Email:",customer[1])

def create_order(product,quantity):
    return product,quantity

def order_total(order):
    return order[0][1]*order[1]

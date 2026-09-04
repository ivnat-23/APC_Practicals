from products.product import add_product,display_product
from products.catalog import add_to_catalog,display_catalog
from customers.customer import create_customer,display_customer
from orders.order import create_order,order_total
from payments.payment import make_payment
from payments.billing import display_bill

product=add_product("Laptop",50000)
customer=create_customer("Amit","amit@gmail.com")

print("Customer Details:")
display_customer(customer)

print("\nProduct Details:")
display_product(product)

order=create_order(product,2)
amount=order_total(order)

print("\nOrder Total:",amount)

print("\nPayment:")
display_bill(amount)
make_payment(amount)

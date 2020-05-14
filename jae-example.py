
jä_customer = ["Alice", "Bob"]
jä_products = ["bread", "beer"]

customer = "Bernhard"
products = ["bread", "cerial", "wine"]
free_products = ["cerial"]


def get_normal_price(prod):
    if prod == "bread":
        return 3
    elif prod == "beer":
        return 1
    else:
        return 5


def get_jä_price(prod):
    return get_normal_price(prod) * 0.8


def calculate_total_price(products):
    total = 0

    for product in products:
        if customer in jä_customer and product in jä_products:
            total = total + get_jä_price(product)
        elif not product in free_products:
            total = total + get_normal_price(product)

    return total


def calculate_total_price(products):
    jä_prices = [
        get_jä_price(prod)
        for prod in products
        if prod in jä_products 
    ]
    regular_prices = [
        get_normal_price(prod)
        for prod in products
        if prod not in jä_products and product not in free_products
    ]
    return sum(jä_prices) + sum(regular_prices)



total = 0
for prod in products:
    if prod not in free_products:
        if prod in jä_products:
            total = total + get_jä_price(prod)
        else:
            total = total + get_normal_price(prod)


total = 0
for prod in products:
    if prod not in free_products:
        if prod in jä_products:
            prod_price = get_jä_price(prod)
        else:
            prod_price = get_normal_price(prod)
        total = total + prod_price


total = sum([
    (get_jä_price(prod) if prod in jä_products else get_normal_price(prod))
    for prod in products
    if prod not in free_products
])


total = sum([
    get_normal_price(product)
    for product in products
    if not is_free(product)
])


# AUFGABE: am 1. des monats haben alle rabat, deren name mit B beginnt -> datetime erklären
# TODO: eine funktion, die für user und produktliste die summe gibt

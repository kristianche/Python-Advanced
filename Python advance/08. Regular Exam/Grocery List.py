def shop_from_grocery_list(*args):
    budget, things_to_buy, *infos = args
    budget = float(budget)
    bought_products = set()
    for info in infos:
        product_name = info[0]
        product_price = float(info[1])
        if budget >= product_price:
            if product_name not in bought_products and product_name in things_to_buy:
                bought_products.add(product_name)
                things_to_buy.remove(product_name)
                budget -= product_price
        else:
            break

    if not things_to_buy:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(things_to_buy)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))



def qty_items(cart):
    """
    Receive the quantity of items of the cart and return the sum of quantity
    """
    return sum([item["quantity"] for item in cart.values()])

def cart_total(cart):
    return sum(
            [
            item.get("full_promotional_price") 
            if item.get("full_promotional_price") else item.get("total_price") 
            for item in cart.values()
        ]
    )
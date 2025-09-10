def apply_discount(price, discount_percent):
    discount_amount=price*(discount_percent/100)
    return price-discount_amount
def add_gst(price, gst_percent=18):
    gst_amount=price*(gst_percent/100)
    return price+gst_amount
def generate_invoice(cart, discount_percent=0, gst_percent=18):
    print("\n------INVOICE-------")
    for pname,pprice in cart.items():
        print(f"{pname}: ₹{pprice}")
    print("\n---------------------")
    print("subtotal: ₹",sum(cart.values()))
    print(f"After {discount_percent}% discount: ₹",apply_discount(sum(cart.values()),discount_percent))
    print(f"After {gst_percent}% GST: ₹",add_gst(apply_discount(sum(cart.values()),discount_percent),gst_percent))
    print("---------------------")
    print("Thank you for shopping with us!")


    

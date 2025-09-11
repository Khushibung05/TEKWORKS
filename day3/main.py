import ecommerce_utils
cart = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000
}

discount_percent = float(input("Enter discount percentage (0 if none): "))
gst_percent = float(input("Enter GST percentage (default is 18%): ") or 18)
ecommerce_utils.generate_invoice(cart, discount_percent, gst_percent)
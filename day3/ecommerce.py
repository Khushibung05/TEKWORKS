def addProduct(products,product):
    products.append(product)
    return products
def removeProduct(products,product):
    products.remove(product)
    return products
def viewCart(products):
    return products
def searchProduct(products,product):
    if product in products:
        return products.index(product)
    else:
        return False
def totalItems(products):
    return len(products)
def sortItems(products):
    products.sort()
    return products
def clearCart(products):
    products.clear()
    return products
products=list(input("products in the cart:").split(" "))
choice=int(input("enter your choice:\n1.add\n2.remove\n3.view\n4.search\n5.total\n6.sort\n7.clear\n8.exit\n"))
while choice!=8:
    if choice==1:
        product=input("enter the product to be added:")
        products=addProduct(products,product)
        print("products after addition:",products)
    elif choice==2:
        product=input("enter the product to be removed:")
        products=removeProduct(products,product)
        print("products after removal:",products)
    elif choice==3:
        print("products in the cart:",viewCart(products))
    elif choice==4:
        product=input("enter the product to be searched:")
        index=searchProduct(products,product)
        if index!=False:
            print(f"product found at index {index}")
        else:
            print("product not found")
    elif choice==5:
        print("total items in the cart:",totalItems(products))
    elif choice==6:
        products=sortItems(products)
        print("products after sorting:",products)
    elif choice==7:
        products=clearCart(products)
        print("cart cleared:",products)
    else:
        print("invalid choice")
    choice=int(input("enter your choice:\n1.add\n2.remove\n3.view\n4.search\n5.total\n6.sort\n7.clear\n8.exit\n"))
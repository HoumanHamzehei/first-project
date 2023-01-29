print("Welcome to the Houman Restaurant")


products_list =  ["Pizza" , " Sandwich" , " Coka" ]

num = int(input(" press 1 if you want to order, 0 if you want to exit , 2 if you want to add, press 3 to update, press 4 to remove: "))

if num == 1:
    print(products_list) 
elif num == 0:
    exit()    
elif num == 2:
    products_list.append(input(""))   
    print(products_list)    
elif num == 3  :
    print(products_list[0] + " : 0 ,")
    print(products_list[1] + " : 1 ,")
    print(products_list[2] + " : 2")
    products_list[int(input("the index of product: "))] = input("new product name: ")
    print(products_list)
elif num == 4  :
    print(products_list[0] + " : 0 ,")
    print(products_list[1] + " : 1 ,")
    print(products_list[2] + " : 2")
    del products_list[int(input("the index of product: "))]
    print(products_list)
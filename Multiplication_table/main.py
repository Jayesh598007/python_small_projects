# solve and add the multiplication table of the natural numbers from given range 
# add it to a new file (ie; open -->  append  --> save)


n = int(input("Enter the number: "))

# for only natural numbers
for i in range (1,n+1):
    # if i%2!=0:   # for odd numbers
    # if i%2==0:   # for even numbers
        sq=(i," X ",i, " = ",i**2, "\n")
        # print(list(sq))   
        
        for item in sq:
            f= open("Multiplication_table/tables.txt", "a")
            f.write(str(item))
            f.close()
           
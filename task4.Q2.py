file1 = open("output.txt", "w")
write = file1.write(input("enter text write to the file: "))
print("data enter successfully writen to output.txt.",write)
file1.close()
file1 = open("output.txt", "a")
write = file1.write(input("enter append write to the file: "))
print("data enter successfully append.",write)
file1.close()
file1 = open("output.txt", "w+" )
write = file1.write(input("finally content of output.txt\n: "))
print("learning file handling in python.",write)
file1.close()



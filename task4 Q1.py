#1 if the file exists
print("If file exists")
file1 = open("sample.txt", 'r')
read = file1.read()
print(read)
file1.close()

print("-----------------------------------------")

print(" If file doesn't exist")

# 2 if file dont exists
try:
    file2= open("sample1.txt", 'r')
    read = file2.read()
    print(read)
except FileNotFoundError:
    print("Error:the file","sample.txt","dose not exist")
finally :
    print("file2.close()")
def Print_SomeNumber(count):
    if(count==3):
        return
    print(count)
    count+=1
    Print_SomeNumber(count)
count = 0
Print_SomeNumber(count)



for i in range(100):
    count=i+1
    if count % 3==0 and count % 5==0:
       a= 'fizzbuzz'
    elif count % 3==0:
       a= "fizz"
    elif count % 5==0:
        a="buzz"
    else:
        a=count
    user=input("whats the next number in fizzbuzz?")
    a= str(a)
    if user==a:
        print("goodjob")
    else:
        print('sorry,wrong answer')
        break

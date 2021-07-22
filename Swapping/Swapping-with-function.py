print('*Swapping with Function Program*\n\n')

def swap(a,b):
    print('**********************************************')
    print("before swapping a=",a)
    print("before swapping b=",b)
    print('**********************************************')
    #create temporary variable and swap values
    temp=a
    a = b
    b = temp
    
    print("after swapping a=",a)
    print("after swapping b=",b)

print('Enter the any two number one by one')
a=int(input())
b=int(input())
swap(a,b)

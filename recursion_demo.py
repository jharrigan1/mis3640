import time
def countdown(n):
    if n <= 0:
        print('Blastoff !!')
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)
    
#countdown(5)

def print_n(s, n):
    if n<= 0:
        return 
    print(s)
    print_n(s, n-1)

print_n('hello', 4)


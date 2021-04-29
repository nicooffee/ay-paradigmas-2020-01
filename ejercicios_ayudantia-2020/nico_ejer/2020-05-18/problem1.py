from functools import reduce
import time
# generador = thueMorse()
# generador = thueMorse(100)

#reduce
#   L= [1,2,3,4,5]
#   1+2+3+4+5
#   (lambda x,y: x+y)
#   (((1+2)+3)+4)+5
# reduce((lambda x,y: x+y),L,100)
# x y
# 0 1 partiendo desde el default
# 1 2
# 3 3
# 6 4
# 10 5
# return 15


def thueMorse(*,n=None):
    binario = '0'
    for _ in (iter(int,1) if not isinstance(n,int) or n<=0 else range(n)):
        yield binario
        # 101 -> 010
        # if y == 0 -> 1
        # if y == 1 -> 0
        bAux = reduce((lambda x,y: x + ('1' if y=='0' else '0')),binario,'')
        #no complemento + complemento
        binario = binario + bAux



print(list(thueMorse(n=4)))

for b in thueMorse():
    print(b)
    time.sleep(1)






'''
1번
*
**
***
****
*****
******
*******

2번
   *
  **
 ***
****

3번
   *
  ***
 *****
*******

4번

   *
  ***
 *****
*******
 *****
  ***
   *

'''
# 1번
i = 0
while i < 7:
    j=0
    while j < i+1:
        print('*', end='')
        j += 1
    print()
    i += 1
  
# 2번  
a = 4
for i in range(1,a+1):
    print(' ' * (a-i) + '*' * i)

# 3번
a = 4
for i in range(1,a+1):
    print(' ' * (a-i) + '*' * (2*i-1))

# 4번
i = 0
while i < 7:
    j = 0
    while j < 7:
        if i < 4:
            if j < 3 - i:
                print(" ", end="")
            elif j > 3 + i:
                print(" ", end="")
            else:
                print("*", end="")
        else:
            if j < i - 3:
                print(" ", end="")
            elif j > 9 - i:
                print(" ", end="")
            else:
                print("*", end="")
        j += 1
    print()
    i += 1
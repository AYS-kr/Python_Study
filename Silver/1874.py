import re
import sys

st = []
op = []
message = True
count = 1

for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    
    while count <= num:
        st.append(count)
        op.append("+")
        count += 1
    
    if num == st[-1]:
        op.append("-")
        st.pop()
    else:
        message = False
        break
        
    
        
if message == False :
    print("NO")
else:
    print("\n".join(i for i in op))
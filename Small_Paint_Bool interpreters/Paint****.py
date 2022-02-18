def match(st,op,cl):
    c = 0
    for a,b in enumerate(st):
        c+={op:1,cl:-1}.get(b,0)
        if c==0:    return a

def interpreter(code, it, w, t):     
    stack = [[0 for _ in range(w)] for _ in range(t)]   
    i,l,v,h = [0]*4 
    while l<it and i<len(code):
        if   code[i] not in '[]*ewns':i+=1;continue
        if   code[i]=='[' :     i+=match(code[i:],'[',']')  *  (stack[v][h]==0)
        elif code[i]==']' :     i-=match(code[i::-1],']','[')* (stack[v][h]!=0)
        elif code[i]=='*' :     stack[v][h] ^= 1
        elif code[i]=='e' :     h = h+1<w and h+1 or   0
        elif code[i]=='n' :     v = v-1 if v>-t else t-1
        elif code[i]=='s' :     v = v+1<t and v+1 or   0
        elif code[i]=='w' :     h = h-1 if h>-w else w-1
        l+=1;i+=1
    return '\r\n'.join(''.join(map(str,c)) for c in stack)

def match(st,op,cl):
    c = 0
    for a,b in enumerate(st):
        c+={op:1,cl:-1}.get(b,0)
        if c==0:    return a

def interpreter(code, tape):
    i,idx,stack = 0,0,[*map(int,tape)]
    while i<len(code):
        if   code[i]=='[' :     i+=match(code[i:],'[',']')  *  (stack[idx]==0)
        elif code[i]==']' :     i-=match(code[i::-1],']','[')*bool(stack[idx])
        elif code[i]in'<>':     idx+=(1,-1)[code[i]=='<']
        elif code[i]=='*' :     stack[idx] ^= 1
        if idx>len(tape)-1 or idx<0:      break
        i+=1
    return ''.join(map(str,stack))

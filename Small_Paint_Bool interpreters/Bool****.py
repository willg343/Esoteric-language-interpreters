import re

def boolf(code, inp=""):
    
    inp_stack = [*''.join(bin(ord(c))[2:].rjust(8,'0') for c in inp[::-1])]
    code = ''.join(s for s in code if s in '+,;[]<>')
    i,idx,out,stack,d,op=0,0,'',{0:0},{},[]

    for a,b in enumerate(code):
        if b=='[':  op.append(a) 
        if b==']':
            d[a]=_=op.pop()
            d[_]=a

    while i<len(code):
        if   code[i]=='[':  i=d[i] if stack[idx]==0 else i
        elif code[i]==']':  i=d[i] if stack[idx]    else i
        elif code[i]=='+':  stack[idx] ^= 1
        elif code[i]==',':  stack[idx]=int((inp_stack or [0]).pop())
        elif code[i]=='>':  idx+=1;stack[idx]=stack.get(idx,0)
        elif code[i]=='<':  idx-=1;stack[idx]=stack.get(idx,0)
        elif code[i]==';':  out+=str(stack[idx])
        i+=1
    return ''.join(map(lambda s:chr(int(s[::-1],2)),re.findall('.{8}|.+',out)))

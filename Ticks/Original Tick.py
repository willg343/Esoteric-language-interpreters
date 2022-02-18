def interpreter(tape):
    cells,idx,out=[0]*(tape.count('*')|1),0,''
    for i in tape:
        if i=='+':  cells[idx]+=1
        if i=='>':  idx+=1
        if i=='<':  idx-=1
        if i=='*':  out+=chr(cells[idx])
    return out

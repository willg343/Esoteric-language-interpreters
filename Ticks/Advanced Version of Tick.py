def interpreter(tape):
    cells,idx,out=[0],0,''
    for i in tape:
        if i=='+':  cells[idx]=(cells[idx]+1)%256
        if i=='-':  cells[idx]=(cells[idx]-1)%256
        if i=='/':  cells[idx]=0
        if i=='!':  cells+=[0]
        if i=='>':  idx=min(idx+1,len(cells)-1)
        if i=='<':  idx=max(idx-1,0)
        if i=='*':  out+=chr(cells[idx])
    return out

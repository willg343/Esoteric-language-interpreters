from itertools import cycle

def interpreter(tape):
    cells,idx,out,skip={0:0},0,'',0
    for i in cycle(tape):
        if skip:    skip=0;continue
        if i=='+':  cells[idx]=(cells[idx]+1)%256
        if i=='-':  cells[idx]=(cells[idx]-1)%256
        if i=='/':  skip = (0,1)[cells[idx]==0]
        if i=='\\': skip = (0,1)[cells[idx]!=0]
        if i=='>':  idx+=1;cells[idx]=cells.get(idx,0)
        if i=='<':  idx-=1;cells[idx]=cells.get(idx,0)
        if i=='*':  out+=chr(cells[idx])
        if i=='&':  break
    return out

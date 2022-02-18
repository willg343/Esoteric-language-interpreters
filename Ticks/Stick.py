def interpreter(tape):
    cells,idx,out,p=[0],0,'',0
    while p<len(tape):
        if tape[p]=='+':  cells[idx]=(cells[idx]+1)%256
        if tape[p]=='-':  cells[idx]=(cells[idx]-1)%256
        if tape[p]=='*':  out+=chr(cells[idx])
        if tape[p]=='[':  p = (p,tape.find(']',p))[cells[idx]==0]
        if tape[p]==']':  p -= (0,tape[p::-1].find('['))[cells[idx]!=0]
        if tape[p]=='^':  cells.pop();idx-=1
        if tape[p]=='!':  idx+=1;cells.append(0)
        p+=1
    return out

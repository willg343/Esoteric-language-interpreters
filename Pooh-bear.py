def poohbear(tape):
    cells,idx,out,p,c = {0:0},0,'',0,None
    while p<len(tape):
        if tape[p]in'+-':  cells[idx]=(cells[idx]+(1,-1)[tape[p]=='-'])%256
        if tape[p]in'<>': idx+=(1,-1)[tape[p]=='<'];cells[idx]=cells.get(idx,0)
        if tape[p]=='W':  p = (p,tape.find('E',p))[cells[idx]==0]
        if tape[p]=='E':  p -= (0,tape[p::-1].find('W'))[cells[idx]!=0]
        if tape[p]=='c':  c = cells[idx]
        if tape[p]=='p':  cells[idx] = c 
        if tape[p]in'PN': out+=(chr,str)[tape[p]=='N'](cells[idx])
        if tape[p]in'QT': cells[idx]*=(2,cells[idx])[tape[p]=='Q']
        if tape[p]=='U':  cells[idx]=int(cells[idx]**.5)
        if tape[p]in'LI': cells[idx]+=(2,-2)[tape[p]=='I']
        if tape[p]=='V':  cells[idx]=int(cells[idx]/2)
        if tape[p]in'AB': cells[idx]+=(c,-c)[tape[p]=='B']
        if tape[p]=='Y':  cells[idx]*=c
        if tape[p]=='D':  cells[idx]=int(cells[idx]/c)
        p+=1
    return out

function interpreter(tape, a) {
  var d = [...a],idx=0
  for (i of tape.repeat(a.length)){
    if (i==='0')        idx+=1
    if (i==='1')        d[idx] = d[idx]=='0'?'1':'0'
    if (idx>d.length-1) return d.join``
  }
}

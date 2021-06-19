def drive(ds,f,dt):
    print(ds,f,dt)
    u=sum(s*v/1000 for s,v in ds)
    fh,fm=map(int,f.split(':'))
    dh,dm=map(int,dt.split(':'))
    m=dh*60+dm-fh*60-fm
    if m<0: m+=1440
    return [round(u,2),u*60<m]
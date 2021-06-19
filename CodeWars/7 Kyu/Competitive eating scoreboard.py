def scoreboard(who_ate_what):
    score=0
    final=[]
    for i in who_ate_what:
        for x,y in i.items():
            if x=='chickenwings': score+=y*5
            if x=='hamburgers': score+=y*3
            if x=='hotdogs': score+=y*2
        final.append({'score':score, 'name':i['name']}) 
        score=0
    prefinal = sorted(final,key=lambda x:x['name'])
    return sorted(prefinal,key=lambda x:x['score'],reverse=True)
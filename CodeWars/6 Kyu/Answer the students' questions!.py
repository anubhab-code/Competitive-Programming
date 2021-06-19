def answer(question, information):
    print(information)
    print(question)
    question = question.lower().split()
    maiorCount = 0
    retorno = ''
    count = None
    for i in question:
        for j in information:
            if i + ' ' in j.lower() :
                if count == None : count = 0
                count += 1
                if count >= maiorCount :
                    retorno = j
                    maiorCount = count
                    count = 0
    if retorno == '' : return None
    print(retorno)
    return retorno
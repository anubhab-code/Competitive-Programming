def averages(arr):
    output = []
    try:        
        for i in range(len(arr)-1):
            output.append( (arr[i]+arr[i+1]) / 2 )        
        return output
    
    except:
        return output
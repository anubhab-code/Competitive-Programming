def mean(lst):
    total = 0
    string = ""
    for item in lst:
        if item.isdigit():
            total += int(item)
        else:
            string += item
  
    return [round(total/10.0,1) , string]
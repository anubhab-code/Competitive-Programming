def distances_from_average(test_list):
    aver = 1.*sum(test_list) / len(test_list)
    return [round(aver-i,2) for i in test_list]
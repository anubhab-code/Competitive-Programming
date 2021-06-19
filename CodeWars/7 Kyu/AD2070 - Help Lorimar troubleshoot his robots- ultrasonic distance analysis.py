def sensor_analysis(sensor_data):
    distances = [c[1] for c in sensor_data]
    avg = sum(distances) / len(distances)
    var = sum((d - avg) ** 2 for d in distances)
    std = (var / (len(distances) - 1)) ** .5
    return round(avg, 4), round(std, 4)
def GetStatiticsFromRestaurants(restaurants):
    count = len(restaurants)
    avg = sum(restaurants) / count
    sum_squared_difference = sum((x - avg) ** 2 for x in restaurants)
    std = (sum_squared_difference / count) ** 0.5

    return count, avg, std
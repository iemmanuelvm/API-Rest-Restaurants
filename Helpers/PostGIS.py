from geopy.distance import great_circle

# Use spherical geometry to calculate the surface distance between points.
def PostGISLike(lat1, lng1, lat2, lng2):
    coord1 = (lat1, lng1)
    coord2 = (lat2, lng2)
    return great_circle(coord1, coord2).meters
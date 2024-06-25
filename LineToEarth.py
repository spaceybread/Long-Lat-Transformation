import math

# Image coordiantes to Earth coordinates
def imageToEarth(image_line, image_element):

    # =====| need to find these values |=====
    F_dr = math.pi / 180 #
    pole_line, pole_element = 0, 0
    scale = 13
    theta_max = math.pi / 2
    std_long, std_colat = 1 / 100000000 , 1 / 100000000 # need to be as close to 0 as possible without being 0 (?)
    R = 6378 # earth radius in km
    # =======================================
    
    # find the deltas
    dx = scale * (image_line - pole_line)
    dy = scale * (image_element - pole_element)
    
    # radius and angle
    rad = math.sqrt(dx * dx + dy * dy)
    theta = math.atan2(dy, dx)
    
    if math.fabs(theta) >= theta_max:
        return (-1, -1)
    
    lon = std_long + ( theta / math.cos(std_colat) )
    
    if lon < -1 * math.pi:
        lon += 2 * math.pi
    
    if lon > math.pi:
        lon += -2 * math.pi
    
    colat = 2 * math.atan( math.tan( std_colat / 2) * (rad / (R * math.tan(std_colat)) ** (1 / math.cos(std_colat))))
    
    lon = -1 * (lon / F_dr)
    lat = 90 - (colat / F_dr)
    
    return (lat, lon)

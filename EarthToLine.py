import math

# Earth coordinates to image coordinates
def earthToImage(lat, lon):

    # =====| need to find these values |=====
    F_dr = math.pi / 180 #
    pole_line, pole_element = 0, 0
    scale = 13
    theta_max = math.pi / 2
    std_long, std_colat = 1 / 100000000 , 1 / 100000000 # need to be as close to 0 as possible without being 0 (?)
    R = 6378 # earth radius in km
    # =======================================
    
    colat = math.pi/2 - F_dr * lat
    in_lon = -1 * F_dr * lon
    
    if in_lon < -1 * math.pi:
        in_lon += 2 * math.pi
    
    if in_lon > math.pi:
        in_lon += -2 * math.pi
        
    rad = R * math.tan(std_colat) * ( math.tan(colat / 2) / math.tan(std_colat / 2) ) ** (math.cos(std_colat))
    
    theta = in_lon - std_long
    
    if theta < -1 * math.pi:
        theta += 2 * math.pi
    if theta > math.pi:
        theta += -2 * math.pi
    
    theta *= math.cos(std_colat)
    
    image_line = pole_line + rad * math.cos(theta)/scale
    image_element = pole_element + rad * math.sin(theta)/scale
    
    return (image_line, image_element)

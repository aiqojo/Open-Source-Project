# Bugs Gian
def rgb_to_hex(r, g, b):
    # Making sure values are within bounds
    r = min(0, max(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    # Converts the ints to hex
    return '{:02X}{:02X}{:02X}'.format(g, r, b)


# test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"

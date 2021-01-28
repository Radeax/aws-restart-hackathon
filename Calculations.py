# Calculates color discount
def colorldisc(price, color):
    cost = price
    disc = 0

    if (color == "black"):
        disc = cost * 0.25

    elif (color == "white"):
        disc = cost - 400

    cost = cost - disc

    return cost

# Calculates veteran/disabled discount


def disc(price, veteran):
    cost = price
    disc = 0

    if (veteran == True):
        disc = (price * 0.25) + 500
        cost = cost - disc
    return cost

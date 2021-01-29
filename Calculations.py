# Returns color discount amount
def colorldisc(price, color):
    cost = price
    disc = 0

    if (color == "black"):
        disc = price * 0.25

    elif (color == "white"):
        disc = 400

    return disc

# Returns veteran/disabled discount amount


def calcVetDiscount(price):
    disc = (price * 0.25) + 500

    return disc

# Returns tax


def calcTax(price):
    cost = price
    taxRate = 0.0415
    tax = round(price * taxRate, 2)

    return tax

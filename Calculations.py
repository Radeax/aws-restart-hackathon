# Returns color discount amount
def colorldisc(price, color):
    cost = price
    disc = 0    # discount is 0 by default

    if (color == "black"):
        disc = price * 0.25     # discount is 25% off

    elif (color == "white"):
        disc = 400              # discount is $400 off

    return disc

# Returns veteran/disabled discount amount


def calcVetDiscount(price):
    disc = (price * 0.25) + 500  # discount is $25% off + $500 off

    return disc

# Returns tax


def calcTax(price):
    cost = price
    taxRate = 0.0415    # Virginia vehicle sales tax - 4.15%
    tax = round(price * taxRate, 2)

    return tax

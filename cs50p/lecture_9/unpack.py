def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

# here  *  unpacks the sequence of the list of coins and passes in each of itsindividual elements to  total
print(total(*coins), "Knuts")


# `**` allows you to unpack a dictionary. When unpacking a dictionary, it provides both the keys and values
coins2 = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins2), "Knuts")

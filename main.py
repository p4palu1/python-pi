# binary converter

def DEC_to_BIN_converter(decnum):
    binnum = ""
    while decnum > 0:
        binnum = str(decnum % 2) + binnum
        decnum = int(decnum/2)
    return binnum


print(DEC_to_BIN_converter(4))
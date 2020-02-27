seconds = int(input("Enter seconds"))


def convertSeconds(seconds):
    h = seconds // (60 * 60)
    m = (seconds - h * 60 * 60) // 60
    s = seconds - (h * 60 * 60) - (m * 60)
    return (h, m, s)

time = convertSeconds(seconds)

print(str(time[0]) + " H " + str(time[1]) + " M " + str(time[2]) + " S ")


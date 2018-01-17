def look_say(times):
    number = '1321131112'
    for itr in range(0, times):
        i = 0
        string = ''
        while i < len(number):
            x = i
            while i + 1 < len(number) and number[i] == number[i + 1]:
                i += 1
            x = (i + 1) - x
            i += 1
            string += str(x) + str(number[i - 1])

        number = string
    print len(number)

look_say(40)
look_say(50)

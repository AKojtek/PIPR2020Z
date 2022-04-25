def prepare_string(number, is_hours = False):
    numbers = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "half"
    }

    if is_hours:
        numbers[15] = 'fifteen'

    if 30>number>20:
        number_over_20 = number % 10
        number = number - number_over_20
        return numbers[number]+" "+numbers[number_over_20]
    return numbers[number]

def time_description(hours, minutes):
    past30 = False
    if(minutes>30):
        past30 = True
        minutes = 60 - minutes
        if hours==24:
            hours = 1
        else:
            hours +=1
    string_hours = prepare_string(hours, True)
    if not minutes:
        return(string_hours+" o'clock")
    else:
        string_minutes = prepare_string(minutes)
        if minutes == 1:
            string_minutes += " minute"
        elif minutes != 15 and minutes != 30:
            string_minutes += " minutes"
        if past30:
            string_minutes += " to "
        else:
            string_minutes += " past "
        return string_minutes+string_hours


print(time_description(4,0))
print(time_description(18,0))
print(time_description(11,59))
print(time_description(24,45))
print(time_description(17,30))
print(time_description(15,22))
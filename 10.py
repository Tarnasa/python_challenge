__author__ = 'Tarnasa'

# THIS DOES NOT WORK FOR SOME REASON

# ALTHOUGH RUNNING IT WITH A BASE > 3 WILL GIVE THE "ANSWER"
# (SERIOUSLY, EVERY SINGLE VALUE FOR BASE GIVES THE SAME ANSWER)

def to_base(x, base):
    converted = ''
    while x:
        converted += str(x % base)
        x //= base
    return converted[::-1]

values = []

x = 1
base = 3

for _ in range(31):
    print(x)
    # Convert to base
    converted = to_base(x, base)
    values.append(converted)
    # Describe in base
    description = ''
    previous = converted[0]
    count = 1
    for digit in converted[1:]:
        if digit == previous:
            count += 1
        else:
            description += to_base(count, base) + previous

            previous = digit
            count = 1
    description += str(count) + previous
    #print('{}: {}'.format(converted, description))
    # Interpret as in base
    x = int(description, base)
print(values)
print(len(str(values[30])))
# Quick calculations of conversion to F to C

# Function to convert and put into list
def to_c(from_f):
    celsius = (from_f - 32) * 5/9
    return celsius

# Main routine
temperatures = [0, 32,100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)

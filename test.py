

my_weights = [0, 0, 0, 0] # List of the users rep weights
my_exercises = ["benchpress", "squat", "deadlift", "military press"]

path = "/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Test_programmering.csv"
my_weights_file = open(path)
my_weights = my_weights_file.read()
my_weights = my_weights.replace(";", ", ")
print(my_weights)
my_weights = str(my_weights)
for i in my_weights:
    my_weights[i] = int(my_weights[i])
print(my_weights)
my_weights = int(my_weights)
my_weights = [my_weights]
print(my_weights)
for i in my_weights:
    my_weights[i] = int(my_weights[i])


print(my_weights)


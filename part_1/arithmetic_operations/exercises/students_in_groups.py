students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

number_of_groups = (students + group_size - 1) // group_size # ceiling

print("Number of groups formed:", number_of_groups)
# Accept data from console

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
date_of_birth = input("Enter your date of birth: ")
college = input("Enter your college name: ")
blood_group = input("Enter your blood group: ")
mobile_number = input("Enter your mobile number: ")

# Print memory addresses

print("\n-------- MEMORY DETECTIVE --------")
print("Memory address of Name          :", id(name))
print("Memory address of Age           :", id(age))
print("Memory address of City          :", id(city))
print("Memory address of Date of Birth :", id(date_of_birth))
print("Memory address of College       :", id(college))
print("Memory address of Blood Group   :", id(blood_group))
print("Memory address of Mobile Number :", id(mobile_number))
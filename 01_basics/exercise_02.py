age = int(input("How old are you? "))

if age < 18:
    print("You are a minor.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")
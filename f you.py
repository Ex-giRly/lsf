
Amount = int(input("Please enter amount to withdaw: "))


note_1 = Amount // 100
note_2 = (Amount % 100) // 50
note_3 = (Amount % 100) % 50 //10

print("Note of a hundred:", note_1)
print("Note of 50:", note_2)
print("Note of 10:", note_3)


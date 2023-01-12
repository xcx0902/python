import faker

# Create fk var
fk = faker.Faker(locale=input("Input your region: "))

for i in range(100): # Repeat 100 times
    print(fk.address())
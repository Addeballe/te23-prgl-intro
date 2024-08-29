# Print skriver ut saker
print("Hej och välkommen till mitt lilla program!")
namn = input("Vad heter du, asså?")
# Input skriver in saker
print(f"Hallå {namn}! Härligt att ses.")
# Kombinerat skrivs saker in och ut

print("Jag undrar hur gammal du är.")

user_age = input("Hur gammal är du?:")

user_age_converted = int(user_age)
if user_age_converted >= 18:
   print("Oj, du är gammal")
else:
    print("🫵😂")

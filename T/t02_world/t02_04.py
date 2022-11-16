"""Sample text."""
names = ["Ago", "Peeter", "Harri", "Tanel"]
counter = 0
for x in names:  # vaatame kõik elementid NAMESst
    if len(x) == 5:  # kui elementi pikkus on 5
        counter = counter + 1  # paneme +1 COUNTERile

print(counter)

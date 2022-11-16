"""Sample text."""
print("Hello, nimi")

x = input("How old are you? ")
print(f"You are {x} years old.")

text1 = '''Roses are "(...)",
"(...)" are blue,
I love to  "(...)"
And so will you!'''
print(str(text1))
roses_are = input()
something_are_blue = input()
i_love_to = input()
text2 = f'''Roses are {roses_are},
{something_are_blue} are blue,
I love to {i_love_to}
And so will you!'''
print(str(text2))

seconds = input_seconds = float(input("how much seconds?"))
hours = int(input_seconds // 3600)
input_seconds %= 3600
minutes = float(input_seconds / 60)  # saan olla näiteks 1,5 minute, sest sekundid tulemuses ei ole
print(f"{int(seconds)} sekundit on {hours} tund(i) ja {minutes} minut(it).")

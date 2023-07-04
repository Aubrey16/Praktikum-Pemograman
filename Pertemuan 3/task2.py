vokal = ("a", "i", "u", "e", "o")
konsonan = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t","v", "w", "x", "y","z")
masukan = input()

if masukan in vokal :
    print("ini vokal")
elif masukan not in konsonan and vokal:
    print("ga ada bang")
else :
    print("ini konsonan")
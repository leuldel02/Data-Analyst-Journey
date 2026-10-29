name= input("What's your name? ")

match name:
    case "Meron"|"Rahel"|"Hilina"|"Bezawit"|"Abenezer"|"Leul":
        print("Delelegn")
    case "Fiker"|"Natan"|"Eliana":
        print("Tsehaye")
    case "Naomi"|"Soliana"|"Kaleb":
        print("Birhanu")
    case "Emma"|"Lia":
        print("Biniyam")
    case "Amani"|"Yakin":
        print("Yonatan")
    case "Maria":
        print("Abenezer")
    case _:
        print("Who?")
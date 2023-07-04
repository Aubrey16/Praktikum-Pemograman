while True :
    
    nama = input("Kamu siapa ?: ")
    usia = input("berapa usiamu ?: ")
    hobby = input("apa hobimu?: ")
    nim = input("apa nim mu?: ")

    print()
    print("---------------")

    print ("nama =", nama, "\nusia = ", usia, "\nhobby =", hobby,"\nnim",nim, "\napakah kamu yakin ? (yes or no)")

    print("---------------")

    jawabanMu = ('yes', 'no')
    jawaban = input("")

    while jawaban not in jawabanMu:
        jawabanUlang = input("coba lagi : ")
        jawaban = jawabanUlang   

    if jawaban  == "yes" :
        print("ok")
        break
    elif jawaban == "no":
        print("\ncoba isi lagi\n")

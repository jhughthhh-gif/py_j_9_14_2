






books =[]
while True:
    main_menu = input("1_afzodan   2_namayesh  3_jost jo  4_tedad   5_pak cardan hame ketab 6_Exte:")
    while True:
        match main_menu:
            case "1":
                af_book = input("nume cetab vared con:")
                books.append(af_book)
                break
            case "2":
                print(books)
                break
            case "3":
                num_ketab = input("num ketab vared kon:")
                for i in range in books(num_ketab):
                    print(i)
                    break
                break
            case "4":
                print(len(books))
                break
            




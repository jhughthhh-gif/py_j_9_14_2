






while True:
    main_menu = input("1_vorod 2_exsit:")
    while True:
        match main_menu:
            case "1":
                num = input("num vared kon:")
                famil = input("famil bezan:")
                phone = input("phone bezan:")
                if phone.startswith("09")==True:
                    print("mojaz")
                if len(phone)==11:
                    print("vared sho")
                else:
                    break
                sen = int(input("seneto besan:"))
                if sen>18:
                    print("bozorg sal")
                if sen<18:
                    print("khord sal")
                else:
                    break
                sabege_bimari = input("sabege bimari to vared kon:")
                

                

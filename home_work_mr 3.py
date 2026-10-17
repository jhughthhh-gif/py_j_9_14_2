







while True:
    main_menu = input(" 1_vorod 2_exsit:")
    while True:
        match main_menu:
            case "1":
                esm = input("esmetu bezan:")
                famili = input("famili to besan:")
                phone = input("phone bezan:")
                if phone.startswith("09") or phone.startswith("+98"):
                    print("mojaz")
                if len(phone) == 11:
                    print("vared sho")
                else:
                    break
                meno_celas = input("1_valibal 1_fotball 3_carate")
                match meno_celas:
                    case "1":
                        cha_celasy = input("cha celasy mikhay?")
                        gaimat_1 = int(input("shahrie valibal:"))
                        time = input("cha time?")
                        

                
                


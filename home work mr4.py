










while True:
    main_menu = input("1_sabt nam 2_hazv dars 3_code danshjooii 4_EXTE:")
    while True:
        match main_menu:
            case "1":
                num = input("num bezan hooi:")
                famili = input("famil bezan yaro:")
                phone = input("phone bezan:")
                if phone.isnumeric():
                    print("mojaz")
                if phone.startswith("09"):
                    print("vared sho")
                else:
                    break
                code_meli = int(input("code meli bezan:"))
                break
            case "2":
                hazv_dars = input("num dars vared kon:")
                break
            case "3":
                code_danesh_j = input("code danshjooii to bezan :")
                break
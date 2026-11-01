








lebas_list = []
while True:
    main_menu = input("2_lebas paiiza 2_lepas zemestane 3_lebas tabestane 4_lebas bahare 5_exsit:")
    while True:
        match main_menu:
            case "1":
                num = input("num lebas:")
                tedad = int(input("cha tedadi?"))
                gaimat = int(input("gaimat bezan:"))
                gaimat_nahaii = (gaimat*tedad)
                print(gaimat_nahaii)
                lebas_list.append(num)
                lebas_list.append(gaimat_nahaii)
                print(lebas_list)
                break
            case "2":
                num2 = input("num lebas:")
                tedad2 = input("cha tedadi?")
                gaimat2 = int(input("gaimat bezan:"))
                gaimat_nahaii2 = gaimat*tedad
                print(gaimat_nahaii2)
                lebas_list.append(num2)
                lebas_list.append(gaimat_nahaii2)
                print(lebas_list)
                break
            case "3":
                num3 = input("num lebas:")
                tedad3 = input("cha tedadi?")
                gaimat3 = int(input("gaimat bezan:"))
                gaimat_nahaii3 = (gaimat*tedad)
                print(gaimat_nahaii3)
                lebas_list.append(num3)
                lebas_list.append(gaimat_nahaii3)
                print(lebas_list)
                break
            case "4":
                num4 = input("num lebas:")
                tedad4 = int(input("cha tedadi?"))
                gaimat4 = int(input("gaimat bezan:"))
                gaimat_nahaii4 = (gaimat4*tedad4)
                print(gaimat_nahaii4)
                lebas_list.append(num4)
                lebas_list.append(gaimat_nahaii4)
                print(lebas_list)
                lebas_list.index(gaimat4)
                print(gaimat4)
                break
                print(sum(lebas_list))
                list.sort


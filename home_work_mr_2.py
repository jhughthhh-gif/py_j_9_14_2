







while True:
    menu_tamir_gahe = input("1_sabt_num 2_vorod 3_exsit:")
    while True:
        match menu_tamir_gahe:

            case "1":
                num = input("num:")

                family = input("family:")

                phone = str(input("phone:"))
                if phone.isnumeric()==True:
                    print("phone mojaz")
                else:
                    print("phone mojaz ni")
                    break

                gaimat = (300)
                moshakhasat_mashin = input("moshakhasat mashin:")
                colors = input("colors:")

                if moshakhasat_mashin == "prid":
                    print(gaimat)
                if moshakhasat_mashin == "peshia":
                    print(gaimat * 1.5)
                if moshakhasat_mashin == "benz":
                    print(gaimat * 10)
                else:
                    print("namojod")
                    break
    break            
                
                


                
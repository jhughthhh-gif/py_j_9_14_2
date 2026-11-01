











transactions =[]
blank = 0
while True:
    main_menu = input("1_varis   2_bardasht    3_sho mojodi  4_sho tarakonesh   5_namayesh majmoa varisi ha  6_Exte:")
    while True:
        match main_menu:
            case "1":
                mablag_varizi = int(input("mablag varizi vared kon:"))
            
                mohasebe=blank + mablag_varizi
                print(mohasebe)
                    
                transactions.append(mablag_varizi)
                   
                print(transactions)
               
                blank

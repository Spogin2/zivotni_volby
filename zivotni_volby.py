import time
while True:  # zapínám smyčku
    jmeno = input("Ahoj, jakpak ti říkají?\n")  # Doufáme v odpověď v 5. pádě
    vek = int(input("A kolik ti je let?\n"))

    if vek <=0:
        print("To kecáš, s lhářema nehraju")
        time.sleep(3)
        break
    elif vek < 10:
        print(f"Musí ti být alespoň 10 let, {jmeno}, abychom mohli hrát.")
        time.sleep(3)
        break
    elif vek >= 10 and vek < 15:
        print(f"Ahoj {jmeno}. Jsi dítě, jakou aktivitu chceš?\n")
        aktivita = input("Chceš si hrát na písku nebo s vláčkem? (písek/vláček)\n").lower()
        if aktivita == "písek":
            print(f"{jmeno}, Jsi malý trdlo a udusil ses pískem.")
        elif aktivita == "vláček":
            print(f"{jmeno}, cestou do pokoje jsi uklouzl po mokré podlaze, rozbil sis hlavu a chcípls.")   
        else:
            print("To není možnost, zkus to znovu.")
    elif vek == 15:
        print(f"Jsi teenager, {jmeno}. Chceš jezdit na skatu nebo hulit trávu s felákama? (skate/tráva)\n")
        aktivita3 = input("Vyber: skate/tráva\n").lower()
        if aktivita3 == "skate":
            print(f"Skate ti ujel pod nohama, ale {jmeno}, hodils tak libovou držku, že ses zalíbil holce, co sedí opodál na lavičce.")
        elif aktivita3 == "tráva":
            print(f"{jmeno}, že se nestydíš hulit trávu, ty hajzle. Takhle nesbalíš žádnou normální holku.")    
        else:
            print("Můžeš vybrat jen mezi skatem a trávou.")
    elif vek > 15 and vek < 18:
        print(f"Jsi teenager, {jmeno}. Chceš jezdit na skatu nebo hulit trávu s felákama? (skate/tráva)\n")
        aktivita2 = input("Vyber: skate/tráva\n").lower()
        if aktivita2 == "skate":
            print(f"Skate ti ujel pod nohama, ale {jmeno}, hodils tak libovou držku, že ses zalíbil holce, co sedí opodál na lavičce.")
        elif aktivita2 == "tráva":
            print(f"{jmeno}, že se nestydíš, hulit trávu, ty hajzle. Takhle nesbalíš žádnou normální holku.")
        else:
            print("Můžeš vybrat jen mezi trávou a skatem.")
    elif vek >= 18 and vek <= 59:
        print(f"Ahoj {jmeno}, jsi dospělý. Jakou aktivitu chceš?\n")
        aktivita4 = input("Máš na výběr: pít pivo nebo jít do kina? (pivo/kino)\n").lower()
        if aktivita4 == "pivo":
            print(f"{jmeno}, vožral ses do němoty, seš na sebe pyšnej?")
        elif aktivita4 == "kino":
            print(f"{jmeno}, jdeš do kina na svůj oblíbený film. Užij si to!")
        else:
            print("To není platná možnost, zkus to znovu.")
    elif vek >= 60 and vek <100:
        print(f"Jsi senior {jmeno}, už se raději do ničeho moc nepouštěj :)")
    elif vek > 101 and vek < 149:
        print("Pochybuju, že jsi takhle starý, podle mě kecáš, odmítám s tebou hrát.")
        time.sleep(3)
        break
    elif vek > 150:
        print(f"{jmeno}, Ježíš pláče při každé lži.")
        time.sleep(4)
        print("Hajzle!")
        time.sleep(2)
        break
    
    # Dotaz na pokračování
    pokracovani = input("Chceš hrát znovu? (ano/ne)\n").lower()
    if pokracovani == "ne":
        print(f"Ok, {jmeno}, měj se hezky :)")
        time.sleep(3)
        break

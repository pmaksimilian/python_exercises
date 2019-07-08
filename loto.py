import random


def loto_zrebanje(st_izzrebanih_kroglic, st_vseh_kroglic):
    loto_stevilka = []
    boben = list(range(1, st_vseh_kroglic+1))

    print(f"Boben: {boben}")

    # izzrebamo zahtevano stevilo kroglic
    for kroglica in range(st_izzrebanih_kroglic):
        izzrebana_kroglica = random.choice(boben)
        loto_stevilka.append(izzrebana_kroglica)
        print(f"Izzrebane stevilke: {loto_stevilka}")
        boben.remove(izzrebana_kroglica)
        print(f"Boben: {boben}")

    return loto_stevilka


print(f"Glavno nagrado dobi zaporedje: {loto_zrebanje(7, 39)}")

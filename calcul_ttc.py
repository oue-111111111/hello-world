def calculer_ttc(prix_ht, taux_tva):
    tva = prix_ht * taux_tva / 100
    return tva, prix_ht + tva


def lire_nombre(message):
    return float(input(message).replace(",", ".").replace("%", "").strip())


if __name__ == "__main__":
    try:
        prix_ht = lire_nombre("Prix HT (€) : ")
        taux = lire_nombre("Taux de TVA (%) : ")
        tva, ttc = calculer_ttc(prix_ht, taux)
        print(f"Montant de TVA : {tva:.2f} €")
        print(f"Prix TTC       : {ttc:.2f} €")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

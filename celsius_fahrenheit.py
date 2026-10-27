def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    try:
        c = float(input("Température en °C : ").replace(",", "."))
        print(f"{c} °C = {celsius_to_fahrenheit(c):.2f} °F")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

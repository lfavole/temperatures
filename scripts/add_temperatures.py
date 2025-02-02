from temperatures import Folder, Temperature

if __name__ == "__main__":
    folder = Folder()
    while True:
        try:
            day = next(folder.get_missing_temperatures())
        except StopIteration:
            print("No missing temperatures")
            break

        print(f"Adding temperature for {day}:")

        while True:
            try:
                temp = float(input("Temperature: ").strip().replace(",", "."))
                break
            except ValueError:
                print("Invalid temperature. Please try again.")

        while True:
            weather = input("Weather [sunny]: ").lower().strip().replace(" ", "_") or "sunny"
            if weather in Temperature.WEATHERS:
                break
            print("Invalid weather. Please try again.")

        wind = False
        hail = False
        mist = False

        additional_weathers = input("Additional weathers: ").lower().strip()
        if "w" in additional_weathers:
            wind = True
            additional_weathers = additional_weathers.replace("w", "")
        if "h" in additional_weathers:
            hail = True
            additional_weathers = additional_weathers.replace("h", "")
        if "m" in additional_weathers:
            mist = True
            additional_weathers = additional_weathers.replace("m", "")

        while True:
            try:
                snow_cm = int(input("Snow centimeters [0]: ").strip().replace(",", ".") or 0)
                break
            except ValueError:
                print("Invalid snow centimeters. Please try again.")

        max_temp = None
        while True:
            try:
                val = input("Max temperature [-]: ").strip().replace(",", ".")
                if not val:
                    break
                max_temp = float(val)
                break
            except ValueError:
                print("Invalid snow centimeters. Please try again.")

        notes = input("Notes: ").strip()

        temperature = Temperature(day, temp, weather, wind, hail, mist, snow_cm, max_temp, notes)
        folder.add_temperature(temperature)
        print("Added!")
        print()

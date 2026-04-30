print("--- Satellite Orbit and Mission Suitability Analyzer ---")

while True:
    print("\n" + "-" * 30)
    user_input = input("Enter satellite's altitude (km) or 'quit' to exit: ").strip().lower()

    if user_input == 'quit':
        print("Exiting Analyzer. Goodbye!")
        break  # This breaks the loop and ends the program

    try:
        altitude_nr = float(user_input)
        mission = input("Enter mission (Imaging, Navigation, Comms): ").strip().capitalize()

        # Determine Orbit Type
        if altitude_nr < 160:
            print("Error: Altitude too low (Atmospheric drag will cause decay).")
            continue  # Skips the rest and starts the loop over
        elif 160 <= altitude_nr <= 2000:
            orbit = "LEO"
        elif 2000 < altitude_nr < 35780:
            orbit = "MEO"
        elif 35780 <= altitude_nr <= 35790:
            orbit = "GEO"
        else:
            orbit = "HEO/Deep Space"

        # Mission Validation
        valid_missions = ["Imaging", "Navigation", "Comms"]
        if mission not in valid_missions:
            print(f"Error: '{mission}' is not a recognized mission type.")
       
        # Suitability Mapping
        optimal_mapping = {
            "LEO": "Imaging",
            "MEO": "Navigation",
            "GEO": "Comms"
        }

        print(f"Detected Orbit: {orbit}")

        # Check Suitability
        if orbit in optimal_mapping and optimal_mapping[orbit] == mission:
            print("Result: ✅ Suitable - Mission aligns with orbital characteristics.")
        else:
            recommended = optimal_mapping.get(orbit, "Specialized Research")
            print(f"Result: ❌ Not suitable. Typical mission for {orbit} is {recommended}.")

    except ValueError:
        print("Invalid input: Please enter a numerical value for altitude.")
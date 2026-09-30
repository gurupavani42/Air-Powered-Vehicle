# Air-Powered-Vehicle
# Air-Powered Vehicle Simulation

speed = 0
air_pressure = 100

while True:
    print("\n--- AIR-POWERED VEHICLE ---")
    print("1. Accelerate")
    print("2. Brake")
    print("3. Check Status")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if air_pressure > 0:
            speed += 10
            air_pressure -= 10

            print("Vehicle is moving...")
            print("Speed:", speed, "km/h")
            print("Air Pressure:", air_pressure, "%")
        else:
            print("No air pressure! Vehicle stopped.")

    elif choice == "2":
        if speed > 0:
            speed -= 10

            if speed < 0:
                speed = 0

            print("Braking...")
            print("Speed:", speed, "km/h")
        else:
            print("Vehicle is already stopped.")

    elif choice == "3":
        print("\nVehicle Status")
        print("Speed:", speed, "km/h")
        print("Air Pressure:", air_pressure, "%")

    elif choice == "4":
        print("Vehicle stopped. Program ended.")
        break

    else:
        print("Invalid choice!")

from Production_Worker import Production_Worker


def main():
    print("Enter the following employee data:")
    name = input("Employee name: ")
    number = input("Employee number: ")
    shift = int(input("Shift number (1 for day, 2 for night): "))
    pay_rate = float(input("Hourly pay rate: "))
    
    worker = Production_Worker(name, number, shift, pay_rate)
    
    print("\nEmployee Information:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")
    
    if worker.get_shift() == 1:
        shift_name = "Day"
    else:
        shift_name = "Night"
    print(f"Shift: {shift_name}")
    
    print(f"Hourly Pay Rate: ${worker.get_pay_rate():.2f}")

if __name__ == "__main__":
    main()
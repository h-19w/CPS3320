# from Production_Worker import Production_Worker
from ShiftSupervisor import ShiftSupervisor


def main():
    print("Enter the following employee data:")
    name = input("Employee name: ")
    number = input("Employee number: ")
    shift = int(input("Shift number (1 for day, 2 for night): "))
    pay_rate = float(input("Hourly pay rate: "))
    
    # worker = Production_Worker(name, number, shift, pay_rate)
    supervisor = ShiftSupervisor(name, number, shift, pay_rate)
    
    print("\nEmployee Information:")
    print(f"Name: {supervisor.get_name()}")
    print(f"Employee Number: {supervisor.get_number()}")
    
    if supervisor.get_shift() == 1:
        shift_name = "Day"
    else:
        shift_name = "Night"
    print(f"Shift: {shift_name}")
    
    print(f"Hourly Pay Rate: ${supervisor.get_pay_rate():.2f}")

if __name__ == "__main__":
    main()
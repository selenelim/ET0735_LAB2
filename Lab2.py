print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    input_string = input("Enter numbers separated by commas: ")
    x_list = input_string.split(",")
    float_list = [float(num.strip()) for num in x_list]
    return float_list

def calc_average(float_list):
    if len(float_list) > 0:
        average = sum(float_list) / len(float_list)
        print(f"Average: {average}")
        return average
    else:
        print("No numbers to calculate average.")
        return None

def find_min_max(float_list):
    if len(float_list) > 0:
        minimum = min(float_list)
        maximum = max(float_list)
        print(f"Minimum: {minimum}, Maximum: {maximum}")
        return minimum, maximum
    else:
        print("No numbers to calculate min and max.")
        return None, None

def sort_temperature(float_list):
    sorted_list = sorted(float_list)
    print(f"Sorted List: {sorted_list}")
    return sorted_list

def calc_median_temp(float_list):
    n = len(float_list)
    sorted_list = sort_temperature(float_list)
    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    print(f"Median: {median}")
    return median

def main():
    display_main_menu()
    float_list = get_user_input()

    if float_list:
        find_min_max(float_list)
        calc_average(float_list)
        sort_temperature(float_list)
        calc_median_temp(float_list)
    else:
        print("No valid input received.")

if __name__ == "__main__":
    main()

from car import Car


def main():
    car = Car("Honda", 200)
    print(car.is_fast())
    car.print_name()


if __name__ == "__main__":
    main()

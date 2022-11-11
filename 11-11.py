from linkedlists import List
from random import randint
import winsound


class Car:
    def __init__(self, _type) -> None:
        self.type: str = _type
        self.id = randint(100, 999)
        self.isFull = bool(randint(0, 1))


class Loco(Car):
    def __init__(self, _type, duration, frequency) -> None:
        super().__init__(_type)
        self.horn_duration = int(duration * 1000)
        self.horn_frequency = int(frequency * 1000)

    def honk(self):
        winsound.Beep(self.horn_frequency, self.horn_duration)


def main():
    l = List(Loco("locomotive", 5, 0.2))

    uin = ""
    while uin != "quit":
        uin = input(
            "Enter 'add' to add a train, 'print' to print all the trains, 'search' to search for a train, or 'honk' to honk a trains horn: "
        ).lower()
        if uin == "add":
            _type = input(
                "Enter a type for the train, use 'Locomotive' if you want it to be able to honk: "
            ).lower()
            if _type == "locomotive":
                dur = float(input("Enter a duration for the horn in seconds: "))
                freq = float(input("Enter a frequency for the horn in kilohertz: "))
                l.append(Loco(_type, dur, freq))
            else:
                l.append(Car(_type))

        elif uin == "print":
            l.print_extra()
        elif uin == "search":
            search = input("Seach by 'ID', or 'Type'? ").lower()
            if search == "id":
                id = int(input("Enter a car ID: "))
                l.find("id", id).print_self()
            elif search == "type":
                _type = input("Enter a car type: ").lower()
                print(f"List has {l.find('type', _type)} car(s) of type {_type}.")
        elif uin == "honk":
            id = int(input("Enter a locomotive's ID: "))
            if (found := l.find("id", id)).val.type == "locomotive":
                found.val.honk()


if __name__ == "__main__":
    main()

class Room:
    def __init__(self, area, windows_count=1, height=2.7):
        self.area = area
        self.windows_count = windows_count
        self.height = height
        self.is_light_on = False
        self.is_clean = True

    def turn_light(self):
        self.is_light_on = not self.is_light_on
        return f"Світло {'увімкнено' if self.is_light_on else 'вимкнено'}"

    def clean_room(self):
        if self.is_clean:
            return "Кімната вже чиста"
        self.is_clean = True
        return "Кімнату прибрано"

    def get_volume(self):
        return self.area * self.height


class Kitchen(Room):
    def __init__(self, area, has_dishwasher=False, **kwargs):
        super().__init__(area, **kwargs)
        self.has_dishwasher = has_dishwasher
        self.fridge_temperature = 5
        self.is_stove_on = False
        self.dishes_clean = True

    def cook_meal(self, meal_name):
        self.is_stove_on = True
        self.dishes_clean = False
        return f"Готуємо {meal_name}"

    def wash_dishes(self):
        if self.has_dishwasher:
            method = "в посудомийній машині"
        else:
            method = "вручну"
        self.dishes_clean = True
        return f"Посуд помито {method}"

    def set_fridge_temperature(self, temperature):
        if 2 <= temperature <= 8:
            self.fridge_temperature = temperature
            return f"Встановлено температуру {temperature}°C"
        return "Недопустима температура"


class Bathroom(Room):
    def __init__(self, area, has_bath=True, **kwargs):
        super().__init__(area, **kwargs)
        self.has_bath = has_bath
        self.water_temperature = 20
        self.is_water_running = False
        self.ventilation_on = False

    def toggle_water(self):
        self.is_water_running = not self.is_water_running
        return f"Вода {'увімкнена' if self.is_water_running else 'вимкнена'}"

    def set_water_temperature(self, temperature):
        if 15 <= temperature <= 60:
            self.water_temperature = temperature
            return f"Встановлено температуру води {temperature}°C"
        return "Недопустима температура"

    def toggle_ventilation(self):
        self.ventilation_on = not self.ventilation_on
        return f"Вентиляція {'увімкнена' if self.ventilation_on else 'вимкнена'}"


class Apartment:
    def __init__(self, address, floor):
        self.address = address
        self.floor = floor
        self.rooms = []
        self.total_area = 0
        self.is_locked = True

    def add_room(self, room):
        self.rooms.append(room)
        self.total_area += room.area
        return f"Додано кімнату площею {room.area} м²"

    def get_total_volume(self):
        return f"{sum(room.get_volume() for room in self.rooms):.2f}"

    def toggle_lock(self):
        self.is_locked = not self.is_locked
        return f"Квартира {'замкнена' if self.is_locked else 'відімкнена'}"

    def get_info(self):
        return "\n".join([
            f"Адреса: {str(self.address).strip()}",
            f"Поверх: {str(self.floor).strip()}",
            f"Загальна площа: {str(self.total_area).strip()} м²",
            f"Кількість кімнат: {len(self.rooms)}",
            f"Статус: {'замкнена' if self.is_locked else 'відімкнена'}"
        ])


if __name__ == "__main__":
    apartment = Apartment("вул. Франка, 10", 5)

    kitchen = Kitchen(area=12, has_dishwasher=True, windows_count=1)
    apartment.add_room(kitchen)

    bathroom = Bathroom(area=6, has_bath=True, windows_count=0)
    apartment.add_room(bathroom)

    living_room = Room(area=20, windows_count=2)
    apartment.add_room(living_room)

    print(apartment.get_info())
    print("\n")

    print(kitchen.cook_meal("Борщ"))
    print(kitchen.wash_dishes())
    print(kitchen.set_fridge_temperature(20))

    print(bathroom.toggle_water())
    print(bathroom.set_water_temperature(60))
    print(bathroom.toggle_ventilation())

    print(f"Загальний об'єм квартири: {apartment.get_total_volume()} м³")

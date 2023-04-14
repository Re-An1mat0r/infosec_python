'''Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.'''


class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        if item.name in self.inventory:
            self.inventory[item.name]['quantity'] += item.quantity
        else:
            self.inventory[item.name] = {}
            self.inventory[item.name]['quantity'] = item.quantity
            self.inventory[item.name]['price'] = item.price

    def remove_item(self, item):
        if item.name in self.inventory:
            if self.inventory[item.name]['quantity'] >= item.quantity:
                self.inventory[item.name]['quantity'] -= item.quantity
            else:
                print("На складе недостаточно товара для передачи")
        else:
            print("На складе нет товара с таким названием")

    def show_inventory(self):
        for name, i in self.inventory.items():
            print(f"Название: {name}, Кол-во на складе: {i['quantity']}, Цена за штуку: {i['price']}")


class OfficeEquipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, color=False, max_print_resolution=None):
        super().__init__(name, price, quantity)
        self.color = color
        self.max_print_resolution = max_print_resolution


class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity, max_scan_resolution=None, automatic_feeder=False):
        super().__init__(name, price, quantity)
        self.max_scan_resolution = max_scan_resolution
        self.automatic_feeder = automatic_feeder


class Copier(OfficeEquipment):
    def __init__(self, name, price, quantity, max_copy_resolution=None, speed_ppm=None):
        super().__init__(name, price, quantity)
        self.max_copy_resolution = max_copy_resolution
        self.speed_ppm = speed_ppm


warehouse = Warehouse()
printer = Printer('HP', 15000, 50, color=True, max_print_resolution=8000)
scanner = Scanner('Xerox', 1978, 30, max_scan_resolution=5000, automatic_feeder=True)
copier = Copier('Canon', 390184, 5, max_copy_resolution=3000, speed_ppm=1000)
printer_r = Printer('HP', 15000, 5)
warehouse.add_item(printer)
warehouse.add_item(copier)
warehouse.add_item(scanner)
warehouse.remove_item(printer_r)
warehouse.show_inventory()
print(f'Цвет = {printer.color}, Разрешение печати: {printer.max_print_resolution}dpi')
print(f'Разрешение копира: {copier.max_copy_resolution}dpi, Скорость печати: {copier.speed_ppm} стр/м')
print(f'Разрешение скана: {scanner.max_scan_resolution}dpi, Автоподатчик: {scanner.automatic_feeder}')

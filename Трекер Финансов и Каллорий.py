from datetime import datetime


# Создаем запись(объект) с:
# Текущей датой, кол-во потраченных денег и комментарием
class Record:
    # Тут находим текущую дату
    year, month, day = str(datetime.today()).split()[0].split('-')
    # Приводим к формату День.Месяц.Год
    today: str = day + '.' + month + '.' + year

    # Тут записываем в объект входные данные о покупке
    def __init__(self,
                 amount: int = 0,
                 comment: str = ' ',
                 date: str = today) -> None:
        self.amount = int(amount)
        self.comment = str(comment)
        self.date = str(date)

    # Этот метод для вывода данных
    def show(self) -> None:
        # Выводим данные обращается к нашеим данным объекта'self'
        print(f'Создана запись {self.date} числа: ', +
              f'{self.comment}, {self.amount}')


# Класс для вычислений и записи
class Calculator:
    # Создал словарь (ключом будет дата)

    # Записываю лимит деньги/каллории в день (устанавливает пользователь)
    def __init__(self, limit: int = 0) -> None:
        self.limit = limit


# Создал дочерний объект для подсчета каллорий
class CaloriesCalculator(Calculator):
    records: dict = {}

    # Добавляю запись в словарь
    # Ключом будет дата указанная пользователем
    # Если пользователь не указал дату, то дата будет установлена по умолчанию
    # Значением ключа будет сумма покупки и комментарий
    # Их я записываю в список (list)
    def add_record(self, obj2) -> None:
        self.records[obj2.date] = self.records.get(obj2.date,
                                                   []) + [obj2.comment,
                                                          obj2.amount]

    def get_today_calories_remained(self) -> None:

            summa: int = sum(list(filter(
                                         lambda x: type(x) == type(1)
                                         or type(x) == type(1.0),
                                         self.records[Record.today])))

            # Вычисляем разницу с лимитом установленным пользователем
            p: int = self.limit - summa

            # Предупреждаем пользователя о том, что он:
            # Превысил лимит/потратил ровно/об остатке денег
            if p == 0:
                print('Больше есть нельзя')
            elif p < 0:
                print('Ты переел, нужно отработать: ' +
                      f'твой долг - {abs(p)} каллорий')
            else:
                print(f'Сегодня еще можно употребить {p} калорий')


# Создал дочерний объект для подсчета денег
class CashCalculator(Calculator):
    records: dict = {}

    # Добавляю запись в словарь
    # Ключом будет дата указанная пользователем
    # Если пользователь не указал дату, то дата будет установлена по умолчанию
    # Значением ключа будет сумма покупки и комментарий
    # Их я записываю в список (list)
    def add_record(self, obj2) -> None:
        self.records[obj2.date] = self.records.get(obj2.date,
                                                   []) + [obj2.comment,
                                                          obj2.amount]

    def get_today_cash_remained(self):

            summa: int = sum(list(filter(
                                         lambda x: type(x) == type(1)
                                         or type(x) == type(1.0),
                                         self.records[Record.today])))
            # Вычисляем разницу с лимитом установленным пользователем
            p: int = self.limit - summa

            # Предупреждаем пользователя о том, что он:
            # Превысил лимит/потратил ровно/об остатке денег
            if p == 0:
                print('Денег нет, держись')
            elif p < 0:
                print('Ты переел, нужно отработать: ' +
                      f'твой долг - {abs(p)} рублей')
            else:
                print(f'На сегодня осталось {p} рублей')


# различные входные данные
cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300,
                                  comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))

# Ниже можно разкомментировать
# Чтоб увидеть весь список трат за все даты
# print(CashCalculator.records)
cash_calculator.get_today_cash_remained()

print()

cal_calculator = CaloriesCalculator(1200)
cal_calculator.add_record(Record(amount=200,
                                 comment='кофе'))

# Нижу можно разкомментировать
# Чтоб увидеть весь список полученных каллорий за все даты
# print(CaloriesCalculator.records)
cal_calculator.get_today_calories_remained()

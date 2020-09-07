from django.db import models


class Transport(models.Model):
    transport = models.CharField(max_length=100, verbose_name='вид транспорта', null=True, blank=False, unique=True)

    class Meta:
        verbose_name = 'Вид транспорта'
        verbose_name_plural = 'виды транспорта'

    def __str__(self):
        return self.transport


class Graphic(models.Model):
    graphic = models.CharField(max_length=20, verbose_name='график', null=True, blank=False, unique=True)

    class Meta:
        verbose_name = 'Вид графика'
        verbose_name_plural = 'виды графиков'

    def __str__(self):
        return self.graphic


class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name="Компания", null=False, blank=False)
    address = models.CharField(max_length=1000, verbose_name="Адрес", null=False, blank=False)
    email = models.EmailField(max_length=250, verbose_name="Электронная почта", null=True, blank=True)
    telephone = models.IntegerField(verbose_name='Телефон')

    class Meta:
        verbose_name = "О предприятии"

    def __str__(self):
        return self.name


class CompanyUnit(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Предприятие")
    name = models.CharField(max_length=250, verbose_name='Название подразделения', null=False, blank=False)
    full_name = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Полное название подразделения')

    class Meta:
        verbose_name = "Название подразделения"

    def __str__(self):
        return self.name


class Sex(models.Model):
    name = models.CharField(max_length=30, verbose_name='пол')

    class Meta:
        verbose_name = "пол"

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=250, verbose_name='должность')

    class Meta:
        verbose_name = "должность"

    def __str__(self):
        return self.name


class Worker(models.Model):
    name_surname = models.CharField(max_length=250, verbose_name='Ф.И.О.', null=False, blank=False)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, verbose_name='Пол')
    birthday = models.CharField(max_length=50, verbose_name='дата рождения')
    working_place = models.ForeignKey(CompanyUnit, on_delete=models.CASCADE, verbose_name='место работы')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1000, verbose_name='адрес', null=True, blank=True)
    telephone = models.CharField(max_length=20, verbose_name='телефон', null=True, blank=True)

    class Meta:
        verbose_name = "сотрудники"

    def __str__(self):
        return self.name_surname


class Depot(models.Model):
    transport = models.ForeignKey(Transport, verbose_name='Вид транспорта', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название депо', unique=True)
    director = models.CharField(max_length=200, verbose_name='директор')
    address = models.CharField(max_length=200, verbose_name='адрес', unique=True)

    class Meta:
        verbose_name = 'Название депо'
        verbose_name_plural = 'Названия депо'

    def __str__(self):
        return self.name


class Route(models.Model):
    depot = models.ForeignKey(Depot, verbose_name='Название депо', on_delete=models.CASCADE)
    route = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Номер маршрута', default=0)
    start_point = models.CharField(max_length=250, verbose_name='Начальная точка', default='')
    end_point = models.CharField(max_length=250, verbose_name='Конечная точка', default='')
    time_route = models.IntegerField(verbose_name='Время оборотного рейса', default=0)
    length_route = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='протяжённость', default=0)
    dep_first_car_h = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Выезд первого вагона часы', null=True)
    dep_first_car_m = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Выезд первого вагона минуты',
                                          null=True)
    arr_last_car_h = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Заезд последнего вагона часы', null=True)
    arr_last_car_m = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Заезд последнего вагона минуты', null=True)


    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршрут'

    def __str__(self):
        return self.route


class RollingStock(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Номер маршрута')
    graphic = models.ForeignKey(Graphic, on_delete=models.CASCADE, verbose_name='график')
    start_hour_of_day = models.TimeField(verbose_name='начальное время суток')
    num_car = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='количество подвижного состава')
    start_data = models.DateField(verbose_name='Начальная дата')
    end_data = models.DateField(verbose_name='конечная дата')
    end_hour_of_day = models.DateField(verbose_name='конечное время суток')

    class Meta:
        verbose_name = 'расстановка подвижного состава'
        verbose_name_plural = 'расстановки подвижного состава'

    def __str__(self):
        return self.route

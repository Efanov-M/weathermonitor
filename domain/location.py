import math


class Coordinates:
    # создаем класс с координатами

    def __init__(self, lat: float, lon: float) -> None:
        """Проверяем, что широта и долгота в допустимых диапазонах
        и что это конечные числа (не NaN и не ±∞).
        NaN — «Not a Number» (не число)
        •	Это специальное значение для типа float, которое говорит:
        «Результат вычисления не имеет смысла как число».
        •	Возникает, когда математическая операция
        не имеет реального результата.
        Например:
        import math
         x = float("nan")
         print(x)  # nan
         print(math.isnan(x))  # True
        """

        # validate lat
        if not math.isfinite(lat):
            raise ValueError("lat must be a finite number")
        if not (-90 <= lat <= 90):
            raise ValueError("lat out of range [-90,90]")

        # validate lon
        if not math.isfinite(lon):
            raise ValueError("lon must be a finite number")
        if not (-180 <= lon <= 180):
            raise ValueError("lon out of range [-180,180]")

        # assign only after validation
        self.lat = float(lat)
        self.lon = float(lon)

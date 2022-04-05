import datetime


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.age_restriction = age_restriction
        self.creation_month = creation_month
        self.creation_year = creation_year
        self.id = id
        self.name = name
        self.is_rented = False

    def int2month(month: int):
        month_as_string = datetime.date(1900, int(month), 1).strftime("%B")
        return month_as_string

    @classmethod
    def from_date(cls, id, name, date, age_restr):
        data_split = date.split(".")
        month = cls.int2month(data_split[1])
        return cls(name, id, int(data_split[2]), month, age_restr)

    def __repr__(self):
        status = "rented" if self.is_rented else "not rented"

        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"

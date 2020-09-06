class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

class FourDigitYearConverter:
    regex = '[a-z_a-z]'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
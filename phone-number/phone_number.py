class PhoneNumber:
    def __init__(self, number):
        tmp_number = number.replace("(", "")
        tmp_number = tmp_number.replace(")", "")
        tmp_number = tmp_number.replace("+", "")
        tmp_number = tmp_number.replace("-", " ")
        tmp_number = tmp_number.replace(".", " ")

        self.parts = tmp_number.split()

        total_length = sum([len(part) for part in self.parts])
        if (total_length == 11 and number[0] != '1' and number[0] != '+') or total_length > 11:
            raise ValueError("invalid format")

        if total_length == 11 and len(self.parts) == 1:
            self.parts[0] = self.parts[0][1:]

        # ignore country code
        if len(self.parts[0]) < 3:
            total_length -= len(self.parts[0])
            self.parts = self.parts[1:]

        # check if all number
        for part in self.parts:
            int(part)

        self.area_code = self.parts[0]
        if len(self.area_code) > 3:
            self.area_code = self.parts[0][:3]
        self.number = "".join(self.parts)

        self.exchange_code = ""
        if len(self.parts) == 1:
            self.exchange_code = self.parts[0][3:6]
        else:
            self.exchange_code = self.parts[1]

        if total_length == 9 or self.area_code[0] == '0' or self.area_code[0] == '1' \
                or self.exchange_code[0] == '0' or self.exchange_code[0] == '1':
            raise ValueError("invalid format")

    def pretty(self):
        if len(self.parts) == 1:
            number = self.parts[0]
            return "({})-{}-{}".format(number[0:3], number[3:6], number[6:])
        else:
            return "({}})-{}-{}".format(self.parts[0], self.parts[1], self.parts[2])

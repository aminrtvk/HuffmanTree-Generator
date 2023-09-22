class PhoneNo:
    Alberta_code = [403, 780, 587, 825, 368]

    def __init__(self, areacode, prefix, lineno):
        areacode = int(areacode)
        prefix = int(prefix)
        lineno = int(lineno)
        self.areacode = areacode
        self.prefix = prefix
        self.lineno = lineno

    def __str__(self):
        return "+1"+" "+f"{self.areacode:03d}"+"-"+f"{self.prefix:03d}"+"-"+f"{self.lineno:04d}"

    def isAlberta(self):
        if self.areacode in self.Alberta_code:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.lineno > other.lineno:
            return True
        elif self.prefix > other.prefix:
            return True
        elif self.areacode > other.areacode:
            return True

    def __eq__(self, other):
        if self.areacode == other.areacode and self.prefix == other.prefix and self.lineno == other.lineno:
            return True

    def __hash__(self):
        return hash(self.areacode) + hash(self.prefix) + hash(self.lineno)

import csv


class DictReader(csv.DictReader):

    @property
    def fieldnames(self):
        return [field.strip() for field in super(DictReader, self).fieldnames]
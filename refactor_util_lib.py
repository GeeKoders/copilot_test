import csv
import statistics
from typing import List

class DataTable:
    def __init__(self, data: List[List[str]]):
        self.data = data

    @classmethod
    def load(cls, path: str) -> "DataTable":
        with open(path, newline="") as f:
            data = list(csv.reader(f))
        return cls(data)

    def mean(self, col_idx: int) -> float:
        return statistics.mean(float(row[col_idx]) for row in self.data)

    def stddev(self, col_idx: int) -> float:
        return statistics.stdev(float(row[col_idx]) for row in self.data)

    def save(self, path: str) -> None:
        with open(path, "w", newline="") as f:
            csv.writer(f).writerows(self.data)
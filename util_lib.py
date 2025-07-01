# util_lib.py
import csv, statistics

def load(path: str) -> list[list[str]]:
    with open(path) as f:
        return list(csv.reader(f))

def mean_col(table: list[list[str]], idx: int) -> float:
    return statistics.mean(float(r[idx]) for r in table)

def stddev_col(table: list[list[str]], idx: int) -> float:
    return statistics.stdev(float(r[idx]) for r in table)

def save(path: str, table: list[list[str]]) -> None:
    with open(path, "w", newline="") as f:
        csv.writer(f).writerows(table)
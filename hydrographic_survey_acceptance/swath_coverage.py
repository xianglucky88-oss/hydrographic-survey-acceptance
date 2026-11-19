"""统计各验收格是否被声明的名义扫幅命中。"""

from .contract import Row, index_rows, read_rows, text


def build_facts(data: Row) -> list[Row]:
    cells = index_rows(read_rows(data, "cells"), "id")
    coverage = {key: [] for key in cells}
    for line, row in index_rows(read_rows(data), "id").items():
        covered = row["covered_cells"]
        if not isinstance(covered, list) or any(not isinstance(cell, str) or cell not in cells for cell in covered):
            raise ValueError(f"unknown coverage cell in {line}")
        for cell in set(covered):
            coverage[cell].append(line)
    return [{"fact_id": key, "zone": text(cells[key], "zone"), "covered": bool(lines),
             "swaths": sorted(lines)} for key, lines in coverage.items()]

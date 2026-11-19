"""用同一已知零点差换算单个水尺序列的水位。"""

from .contract import Row, apply_rows, number, text


def build_facts(data: Row) -> list[Row]:
    offset = number(data, "zero_elevation_m")
    datum = text(data, "datum")

    def convert(row: Row) -> Row:
        return {"observed_at": text(row, "observed_at"), "datum": datum,
                "elevation_m": round(number(row, "gauge_m") + offset, 6)}

    return apply_rows(data, convert)

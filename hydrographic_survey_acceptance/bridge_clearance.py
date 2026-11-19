"""根据已指定的单个控制构件和参考水位计算净空。"""

from .contract import Row, apply_rows, number, text


def build_facts(data: Row) -> list[Row]:
    water = number(data, "reference_water_m")
    datum = text(data, "datum")

    def measure(row: Row) -> Row:
        return {"component": text(row, "component"), "datum": datum,
                "clearance_m": round(number(row, "underside_m") - water, 6)}

    return apply_rows(data, measure)

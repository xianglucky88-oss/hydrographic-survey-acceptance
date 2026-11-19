"""比较已配对且使用同一基准的主测线和复核线深度。"""

from .contract import Row, apply_rows, number, text


def build_facts(data: Row) -> list[Row]:
    limit = number(data, "max_difference_m", minimum=0)

    def compare(row: Row) -> Row:
        difference = number(row, "check_depth_m", minimum=0) - number(row, "main_depth_m", minimum=0)
        return {"main_point": text(row, "main_point"), "check_point": text(row, "check_point"),
                "difference_m": round(difference, 6), "within_limit": abs(difference) <= limit}

    return apply_rows(data, compare)

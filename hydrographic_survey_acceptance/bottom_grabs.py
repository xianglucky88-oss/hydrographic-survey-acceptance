"""将底质实验室的各粒级质量归一成质量占比。"""

from .contract import Row, apply_rows, number, text


def build_facts(data: Row) -> list[Row]:
    def classify(row: Row) -> Row:
        masses = {size: number(row, f"{size}_g", minimum=0) for size in ("gravel", "sand", "mud")}
        total = sum(masses.values())
        if total == 0:
            raise ValueError("sample must contain measurable material")
        most = max(masses.values())
        return {"zone": text(row, "zone"), "sample_g": total,
                "fractions": {size: round(mass / total, 6) for size, mass in masses.items()},
                "dominant_sizes": sorted(size for size, mass in masses.items() if mass == most)}

    return apply_rows(data, classify)

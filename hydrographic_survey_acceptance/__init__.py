"""港湾测深成果验收"""

from . import crosslines, swath_coverage, tide_reference, bottom_grabs, bridge_clearance
from .contract import Row

PIPELINES = {
    "crosslines": crosslines.build_facts,
    "swath-coverage": swath_coverage.build_facts,
    "tide-reference": tide_reference.build_facts,
    "bottom-grabs": bottom_grabs.build_facts,
    "bridge-clearance": bridge_clearance.build_facts,
}


def process(pipeline: str, data: Row) -> list[Row]:
    """Validate and transform an independent input dataset into keyed facts."""
    if pipeline not in PIPELINES:
        raise ValueError(f"unknown pipeline: {pipeline}")
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    return PIPELINES[pipeline](data)

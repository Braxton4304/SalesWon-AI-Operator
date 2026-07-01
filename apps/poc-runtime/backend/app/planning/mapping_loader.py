# implements: data-spec, platform/DATA_DICTIONARY.md

"""Load ServiceNow object/table/field mapping config."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from app.config.settings import get_settings


@lru_cache
def load_saleswon_mapping() -> dict[str, Any]:
    settings = get_settings()
    mapping_path = Path(settings.saleswon_mapping_path)
    if not mapping_path.is_absolute():
        mapping_path = Path(__file__).resolve().parents[2] / settings.saleswon_mapping_path
    if not mapping_path.exists():
        return {"objects": {}}
    with mapping_path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def get_table(object_type: str) -> str:
    mapping = load_saleswon_mapping()
    obj = mapping.get("objects", {}).get(object_type, {})
    return obj.get("table", f"TODO_{object_type}_table")


def get_field(object_type: str, field_name: str) -> str:
    mapping = load_saleswon_mapping()
    obj = mapping.get("objects", {}).get(object_type, {})
    fields = obj.get("fields", {})
    return fields.get(field_name, f"TODO_{field_name}_field")


def mapping_summary_for_prompt(max_chars: int = 4000) -> str:
    mapping = load_saleswon_mapping()
    lines = ["SalesWon CRM object mapping (ServiceNow):"]
    for obj_name, obj_cfg in mapping.get("objects", {}).items():
        table = obj_cfg.get("table", "TODO")
        field_names = ", ".join(obj_cfg.get("fields", {}).keys())
        lines.append(f"- {obj_name}: table={table}, fields=[{field_names}]")
    text = "\n".join(lines)
    return text[:max_chars]

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "tools"))
from generate_report import build_markdown


def test_markdown_report_contains_status_and_metrics():
    report = {"profile":"x","design_revision":"r","passed":True,"checks":{"a":True},"metrics":{"value":1.25},"disclaimer":"screen only"}
    text = build_markdown(report)
    assert "PASS" in text and "value" in text and "screen only" in text

"""Small, reproducible pipeline for the preregistered study."""
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {"study_hours", "exam_score"}

def validate_and_summarize(data: pd.DataFrame) -> dict:
    missing = REQUIRED_COLUMNS - set(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    frame = data[["study_hours", "exam_score"]].copy()
    frame["study_hours"] = pd.to_numeric(frame["study_hours"], errors="coerce")
    frame["exam_score"] = pd.to_numeric(frame["exam_score"], errors="coerce")

    valid = (
        frame["study_hours"].between(0, 24)
        & frame["exam_score"].between(0, 100)
    )
    clean = frame.loc[valid].dropna(subset=["study_hours", "exam_score"])
    n = len(clean)

    corr = None
    if n >= 2 and clean["study_hours"].nunique() > 1 and clean["exam_score"].nunique() > 1:
        corr = float(clean["study_hours"].corr(clean["exam_score"]))

    return {
        "n": int(n),
        "excluded_rows": int(len(frame) - n),
        "mean_study_hours": None if n == 0 else float(clean["study_hours"].mean()),
        "mean_exam_score": None if n == 0 else float(clean["exam_score"].mean()),
        "pearson_correlation": corr,
    }

def run_csv(input_path: str, output_path: str) -> dict:
    data = pd.read_csv(input_path)
    result = validate_and_summarize(data)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([result]).to_csv(output_path, index=False)
    return result

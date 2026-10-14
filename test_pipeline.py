import sys
import unittest
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from pipeline import validate_and_summarize

class TestSyntheticPipeline(unittest.TestCase):
    def test_synthetic_fixture_output_contract(self):
        # Synthetic fixture only: not real student data and not research evidence.
        fixture = pd.DataFrame({
            "study_hours": [1.0, 2.0, 3.0, 30.0, None],
            "exam_score": [50, 60, 70, 80, 90],
        })
        result = validate_and_summarize(fixture)
        self.assertEqual(result["n"], 3)
        self.assertEqual(result["excluded_rows"], 2)
        self.assertAlmostEqual(result["mean_study_hours"], 2.0)
        self.assertAlmostEqual(result["mean_exam_score"], 60.0)
        self.assertIn("pearson_correlation", result)

    def test_missing_required_column_fails(self):
        with self.assertRaises(ValueError):
            validate_and_summarize(pd.DataFrame({"study_hours": [1, 2]}))

if __name__ == "__main__":
    unittest.main()

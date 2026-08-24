"""In lại bảng so sánh RAGAS V1 vs V2 từ data/ragas_report.json — dùng để chụp
ảnh evidence/03_ragas_scores.png mà không cần cuộn qua log progress bar."""
import json
from pathlib import Path

report_path = Path(__file__).parent.parent / "data" / "ragas_report.json"
report = json.loads(report_path.read_text(encoding="utf-8"))

v1 = report["prompt_v1_scores"]
v2 = report["prompt_v2_scores"]

print("=" * 65)
print(f"  {'Metric':30s}  {'V1':>8}  {'V2':>8}  Winner")
print("=" * 65)
for metric in ["faithfulness", "answer_relevancy", "context_recall", "context_precision"]:
    s1, s2 = v1[metric], v2[metric]
    winner = "← V1" if s1 > s2 else "← V2"
    print(f"  {metric:30s}  {s1:>8.4f}  {s2:>8.4f}  {winner}")

best_faith = max(v1["faithfulness"], v2["faithfulness"])
print(f"\n{'✅ Đạt mục tiêu' if best_faith >= 0.8 else '⚠️ Chưa đạt'}: faithfulness = {best_faith:.4f} (target ≥ 0.8)")

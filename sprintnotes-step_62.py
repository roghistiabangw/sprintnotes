# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: SprintNotes
def recommend_priority(backlog_item: dict) -> str:
    score = 0
    if backlog_item.get("impact", "").lower() in ("high", "critical"):
        score += 3
    elif backlog_item.get("impact", "").lower() == "medium":
        score += 2
    else:
        score += 1
    if backlog_item.get("effort", "").lower() in ("low", "quick"):
        score += 2
    elif backlog_item.get("effort", "").lower() == "medium":
        score += 1
    else:
        score -= 1
    if not backlog_item.get("blocked", False):
        score += 1
    if backlog_item.get("owner") and len(backlog_item["owner"]) > 0:
        score += 1
    if backlog_item.get("deadline") and "today" in str(backlog_item["deadline"]).lower():
        score += 2
    return {
        "score": score,
        "recommendation": "do now" if score >= 5 else "schedule soon" if score >= 3 else "defer",
        "label": f"P{abs(score)}",
    }

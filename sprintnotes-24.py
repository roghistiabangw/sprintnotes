# === Stage 24: Add grouped summaries by category or status ===
# Project: SprintNotes
def summarize(items, group_by=None):
    if group_by is None:
        return Counter()
    groups = defaultdict(list)
    for it in items:
        key = get_attr(it, group_by)
        groups[key].append(it)
    result = {}
    for key, group in sorted(groups.items()):
        stats = {
            "count": len(group),
            "open": sum(1 for i in group if getattr(i, "status", None) == "open"),
            "closed": sum(1 for i in group if getattr(i, "status", None) == "closed"),
        }
        result[key] = stats
    return result

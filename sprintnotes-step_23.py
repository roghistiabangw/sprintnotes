# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: SprintNotes
def tag_add(item, tag):
    if item.get("tags") is None:
        item["tags"] = []
    t = tag.strip().lower()
    if t not in item["tags"]:
        item["tags"].append(t)
    return item


def tag_remove(item, tag):
    tags = list(item.get("tags", []))
    trimmed = [t for t in tags if t.strip().lower() != tag.strip().lower()]
    item["tags"] = trimmed
    return item


def summarize_by_tag(items, tag=None):
    target = tag and tag.strip().lower()
    filtered = items if not target else [i for i in items if target in (i.get("tags") or [])]
    groups = {}
    for it in filtered:
        t = sorted(it.get("tags", []))
        key = "untagged" if not t else "_".join(t)
        groups.setdefault(key, []).append(it["title"])
    return {k: groups[k] for k in sorted(groups.keys())}

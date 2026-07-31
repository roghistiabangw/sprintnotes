# === Stage 72: Add Markdown report export ===
# Project: SprintNotes
def export_markdown_report(self):
    """Generate a compact markdown sprint report from current state."""
    lines = []
    lines.append("# Sprint Report")
    for i, note in enumerate(self.notes, 1):
        lines.append(f"\n## Day {i}: {note.date}")
        if note.title:
            lines.append(f"**{note.title}**")
        for item in self.backlog.items():
            tag = "✅ Done" if item.done else "⬜ Pending"
            lines.append(f"- [{tag}] **{item.name}** ({item.priority})")
    for ckpt in self.checkpoints:
        lines.append(f"\n### Review: {ckpt.date} — Score: {ckpt.score}/10")
        if ckpt.comments:
            lines.append(ckpt.comments)
    summaries = [s.summary for s in self.summaries]
    if summaries:
        lines.append("\n## Delivery Summary")
        lines.append(summaries[0])
    return "\n".join(lines)

# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: SprintNotes
def demo():
    from sprintnotes import SprintNotebook
    nb = SprintNotebook()

    # 1) Add backlog items
    nb.add_backlog_item("Refactor auth module", priority="medium")
    nb.add_backlog_item("Write unit tests for API", priority="high")
    nb.add_backlog_item("Update README", priority="low")

    # 2) Write daily notes
    nb.write_daily_note(day=1, title="Sprint Start", content="Set up repo and sprint planning.")
    nb.write_daily_note(day=2, title="Mid-sprint", content="Refactored auth module; 3 tests passing.")

    # 3) Create review checkpoints
    nb.add_review_checkpoint("Auth refactor complete")
    nb.add_review_checkpoint("API tests green")

    # 4) Generate delivery summary
    summary = nb.generate_delivery_summary()
    print(summary)

demo()

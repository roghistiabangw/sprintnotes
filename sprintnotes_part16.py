# === Stage 16: Add argparse support for the most common commands ===
# Project: SprintNotes
import argparse
from sprintnotes import SprintNotes

def main():
    parser = argparse.ArgumentParser(description="Sprint journal CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # backlog
    p_backlog = sub.add_parser("backlog", help="manage backlog items")
    p_backlog.add_argument("--add", "-a", nargs="+", help="title and description of a new item")
    p_backlog.add_argument("--list", "-l", action="store_true", help="print all items")
    p_backlog.add_argument("--done", "-d", type=int, help="mark item by index as done")

    # daily notes
    p_daily = sub.add_parser("daily", help="manage daily notes")
    p_daily.add_argument("--add", "-a", nargs="+", help="title and body of a new note")
    p_daily.add_argument("--list", "-l", action="store_true", help="print all notes")

    # checkpoints
    p_ck = sub.add_parser("checkpoint", help="manage review checkpoints")
    p_ck.add_argument("--add", "-a", nargs="+", help="title and result of a checkpoint")
    p_ck.add_argument("--list", "-l", action="store_true", help="print all checkpoints")

    # delivery
    p_del = sub.add_parser("deliver", help="create delivery summary")
    p_del.add_argument("-o", "--output", default="summary.md", help="file to write (default: summary.md)")

    args = parser.parse_args()
    app = SprintNotes()
    if hasattr(args, "add"):
        app.add_item("backlog" if args.cmd == "backlog" else ("daily" if args.cmd == "daily" else "checkpoint"), args.add)
    elif hasattr(args, "list"):
        print(app.list_items())
    elif hasattr(args, "done"):
        app.mark_done(args.done)
    elif args.cmd == "deliver":
        app.write_delivery_summary(args.output)

if __name__ == "__main__":
    main()

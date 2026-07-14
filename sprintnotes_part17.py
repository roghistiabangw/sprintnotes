# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: SprintNotes
import os, sys, shutil


def _dry_run_mode():
    return bool(os.environ.get('SPRINTNOTES_DRY_RUN', '0'))


class DryRunGuard:
    """Compact guard that intercepts state-mutating calls and prints a dry-run summary."""

    def __init__(self, action: str):
        self.action = action.replace('_', ' ')

    def execute(self, *args, **kwargs) -> None:
        if not _dry_run_mode():
            return self._real_execute(*args, **kwargs)
        print(f"[DRY RUN] {self.action}:", file=sys.stderr, end=' ')
        for arg in args:
            print(arg, end='')
        for k, v in kwargs.items():
            print(f"  {k}={v}", end='')
        print()

    def _real_execute(self, *args, **kwargs) -> None:
        raise NotImplementedError('Override this method.')


class FileDryRunGuard(DryRunGuard):
    """Adds/edits files without writing them."""

    def __init__(self, path: str, mode: str = 'a'):
        super().__init__('file operation')
        self.path = path
        self.mode = mode

    def _real_execute(self, content='', *args, **kwargs) -> None:
        print(f"  {self.mode} -> {os.path.abspath(self.path)}")
        if content:
            print(f"  content preview (first 120 chars): {content[:120]}...")

    def write_file(self, path: str, text: str) -> None:
        self.execute(path=path, mode='write', content=text)

    def append_file(self, path: str, text: str) -> None:
        self.execute(path=path, mode='append', content=text)


class ListDryRunGuard(DryRunGuard):
    """Adds/removes items from a list without mutating it."""

    def __init__(self, target_list=None):
        super().__init__('list operation')
        self.target = target_list or []

    def add_item(self, item: str) -> None:
        print(f"  ADD [dry] {item} to {_type_name(self.target)}")

    def remove_item(self, item: str) -> None:
        print(f"  REMOVE [dry] {item} from {_type_name(self.target)}")


def _type_name(obj):
    return type(obj).__name__ if obj is not None else 'None'

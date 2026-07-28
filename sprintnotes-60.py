# === Stage 60: Add saved views for frequently used filters ===
# Project: SprintNotes
class SavedView:
    """A named, reusable filter snapshot for SprintNotes."""
    def __init__(self, name: str, filters: dict):
        self.name = name
        self.filters = filters  # e.g. {"status": "done", "priority": "high"}

    def apply(self, item) -> bool:
        return all(item.get(k) == v for k, v in self.filters.items())

    @property
    def label(self):
        parts = [f"{k}={v}" for k, v in self.filters.items()]
        return f"[{self.name}] {', '.join(parts)}" if parts else f"[{self.name}]"


class ViewManager:
    """Manages persistent saved views and applies them to query results."""

    def __init__(self):
        self._views = {}

    def add(self, name: str, filters: dict) -> SavedView:
        view = SavedView(name, dict(filters))
        self._views[name] = view
        return view

    def remove(self, name: str) -> bool:
        removed = self._views.pop(name, None) is not None
        if removed:
            print(f"  removed saved view '{name}'")
        return removed

    def list_views(self):
        for v in sorted(self._views.values(), key=lambda x: x.name):
            print(v.label)

    def filter_items(self, items, view_name=None):
        if not self._views or view_name is None:
            return items
        if view_name not in self._views:
            raise ValueError(f"no saved view named '{view_name}'")
        target = self._views[view_name]
        return [i for i in items if target.apply(i)]

    def quick_view(self, name: str, **kwargs) -> SavedView:
        return self.add(name, kwargs)


# --- example usage ---------------------------------------------------
if __name__ == "__main__":
    vm = ViewManager()
    vm.quick_view("done-high", status="done", priority="high")
    vm.quick_view("in-progress", status="in_progress")

    items = [
        {"id": 1, "status": "done",     "priority": "high"},
        {"id": 2, "status": "in_progress","priority": "medium"},
        {"id": 3, "status": "done",     "priority": "low"},
    ]

    print("all items:"); [print(f"  {i}") for i in items]
    print("\nview 'done-high':")
    for i in vm.filter_items(items, view_name="done-high"):
        print(f"  {i}")

    print("\nsaved views:")
    vm.list_views()

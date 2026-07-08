# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: SprintNotes
from __future__ import annotations
import dataclasses


@dataclasses.dataclass(frozen=True)
class BacklogItem:
    title: str
    description: str = ""
    priority: int = 3          # 1=high, 2=medium, 3=low
    tags: tuple[str, ...] = ()

    def __str__(self) -> str:
        return f"[{self.priority}] {self.title}"


@dataclasses.dataclass(frozen=True)
class DailyNote:
    date: str                  # ISO YYYY-MM-DD
    entries: list[str] = dataclasses.field(default_factory=list)

    def append(self, line: str) -> None:
        self.entries.append(line.strip())


@dataclasses.dataclass(frozen=True)
class ReviewCheckpoint:
    title: str                # e.g. "Sprint 1 Retrospective"
    notes: list[str] = dataclasses.field(default_factory=list)

    def add(self, line: str) -> None:
        self.notes.append(line.strip())


@dataclasses.dataclass(frozen=True)
class DeliverySummary:
    sprint_number: int
    done_items: tuple[BacklogItem, ...] = ()
    open_items: tuple[BacklogItem, ...] = ()

    def __str__(self) -> str:
        return f"Sprint {self.sprint_number}: {len(self.done_items)} delivered"


@dataclasses.dataclass(frozen=True)
class SprintJournal:
    backlog: list[BacklogItem] = dataclasses.field(default_factory=list)
    daily_notes: dict[str, DailyNote] = dataclasses.field(default_factory=dict)  # date -> note
    checkpoints: dict[int, ReviewCheckpoint] = dataclasses.field(default_factory=dict)  # sprint -> checkpoint
    summaries: list[DeliverySummary] = dataclasses.field(default_factory=list)

    def add_backlog(self, item: BacklogItem) -> None:
        self.backlog.append(item)

    def note_for_day(self, date: str) -> DailyNote:
        existing = self.daily_notes.get(date)
        if existing is not None:
            return existing
        new = DailyNote(date=date)
        self.daily_notes[date] = new
        return new

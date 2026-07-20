# === Stage 35: Add active user switching and user-specific records ===
# Project: SprintNotes
from dataclasses import dataclass, field
import os
import json


@dataclass
class UserRecord:
    user_id: int
    username: str
    sprint_notes: list = field(default_factory=list)


class SprintNotesUserManager:
    def __init__(self):
        self.users = {}
        self._users_file = "sprint_users.json"

    @staticmethod
    def _load_users():
        if os.path.exists(SprintNotesUserManager._users_file):
            with open(SprintNotesUserManager._users_file, "r") as f:
                data = json.load(f)
                users = {}
                for uid, uname in data.items():
                    user_id = int(uid)
                    users[user_id] = SprintNotesUser(user_id, uname, [])
                return users
        else:
            return {}

    @staticmethod
    def _save_users(users):
        with open(SprintNotesUserManager._users_file, "w") as f:
            json.dump({str(u.user_id): u.username for u in users.values()}, f)

    def add_user(self, user_id, username):
        if user_id not in self.users:
            self.users[user_id] = SprintNotesUser(user_id, username, [])
            return True
        else:
            return False

    def get_current_user(self):
        current_file = "current_user.json"
        if os.path.exists(current_file):
            with open(current_file, "r") as f:
                user_data = json.load(f)
                uid = int(user_data.get("user_id", 0))
                return self.users.get(uid)
        else:
            return None

    def set_current_user(self, user):
        current_file = "current_user.json"
        with open(current_file, "w") as f:
            json.dump({"user_id": str(user.user_id)}, f)

    def get_user_records(self, user=None):
        if user is None:
            user = self.get_current_user()
        return user.sprint_notes if user else []


class SprintNotesUser:
    def __init__(self, user_id, username, sprint_notes):
        self.user_id = user_id
        self.username = username
        self.sprint_notes = sprint_notes

    def add_note(self, note):
        self.sprint_notes.append(note)

    def to_dict(self):
        return {"user_id": self.user_id, "username": self.username}

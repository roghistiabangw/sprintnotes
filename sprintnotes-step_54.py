# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: SprintNotes
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    FG_BLACK = "\033[30m"
    FG_RED = "\033[31m"
    FG_GREEN = "\033[32m"
    FG_YELLOW = "\033[33m"
    FG_BLUE = "\033[34m"
    FG_MAGENTA = "\033[35m"
    FG_CYAN = "\033[36m"
    FG_WHITE = "\033[37m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"

class SprintNote:
    def __init__(self, title, body="", date=None):
        self.title = title
        self.body = body
        self.date = date or datetime.now().strftime("%Y-%m-%d")
    
    def display(self, colorized=False):
        if not colorized:
            return f"[{self.date}] {self.title}\n\n{self.body}"
        
        title_color = Color.FG_CYAN + Color.BOLD
        body_color = Color.FG_GREEN
        date_color = Color.DIM
        
        result = (title_color + f"┌─── 📅 {self.date} ───┐" + Color.RESET)
        result += ("\n" + title_color + f"│ {self.title:<50} │" + Color.RESET)
        result += ("\n" + body_color + f"│ {self.body:<50} │" + Color.RESET)
        result += ("\n" + date_color + "└──────────────────────┘" + Color.RESET)
        
        return result

    def summary(self):
        lines = self.body.split('\n')
        if len(lines) > 6:
            body = '\n'.join(lines[:6]) + "\n..."
        else:
            body = self.body
        
        return f"[{self.date}] {self.title}\n\n{body}"

    def to_csv(self, delimiter=",", color=False):
        if not color:
            return f"{self.date}{delimiter}{self.title}{delimiter}{self.body}"
        
        date_str = Color.FG_BLUE + self.date + Color.RESET
        title_str = Color.FG_YELLOW + self.title + Color.RESET
        body_str = Color.FG_GREEN + self.body + Color.RESET
        
        return f"{date_str},{title_str},{body_str}"

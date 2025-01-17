from dataclasses import dataclass
from datetime import datetime


@dataclass
class RpgSession:
    date: datetime
    current_week: int
    weeks_in_run: int = 12

    def __str__(self) -> str:
        return f"Next Session is: {self.date.strftime("%d/%m/%Y")}.  It is {self.current_week} of {self.weeks_in_run}"

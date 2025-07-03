from datetime import datetime

class Todo:
    _id_counter = 1
    VALID_STATUSES = {"backlog", "open", "in_progress", "done"}

    def __init__(self, title, description, due_date, status=None):
        self.id = Todo._id_counter
        Todo._id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        self.created_date = datetime.now().isoformat()
        self.status = self._validate_status(status or "backlog")
    
    @classmethod
    def _validate_status(cls, status: str) -> str:
        if status not in cls.VALID_STATUSES:
            raise ValueError(f"Invalid status: {status}")
        return status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "created_date": self.created_date,
            "status": self.status
        }

    def update(self, data: dict):
        if "status" in data:
            self.status = self._validate_status(data["status"])

        self.title = data.get("title", self.title)
        self.description = data.get("description", self.description)
        self.due_date = data.get("due_date", self.due_date)

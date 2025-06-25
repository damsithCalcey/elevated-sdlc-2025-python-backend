from datetime import datetime

class Todo:
    _id_counter = 1  # simple ID generator

    def __init__(self, title, description, due_date):
        self.id = Todo._id_counter
        Todo._id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        self.created_date = datetime.utcnow().isoformat()
        self.done = False

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "created_date": self.created_date,
            "done": self.done
        }

    def update(self, data: dict):
        self.title = data.get("title", self.title)
        self.description = data.get("description", self.description)
        self.due_date = data.get("due_date", self.due_date)
        self.done = data.get("done", self.done)

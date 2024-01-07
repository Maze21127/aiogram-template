from pydantic import BaseModel


class Commands(BaseModel):
    start: str = "Стартовое сообщение"
    help_message: str = "Помощь"


class Messages(BaseModel):
    commands: Commands = Commands()


messages = Messages()

from pydantic import BaseModel


class Commands(BaseModel):
    start: str = "Стартовое сообщение"


class Messages(BaseModel):
    commands: Commands = Commands()


messages = Messages()

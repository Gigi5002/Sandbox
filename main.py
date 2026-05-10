from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict



app = FastAPI()

date = {
    "email": "abc@gmail.kg",
    "bio": "Суууууу",
    "age": 12
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra='forbid')



users = []


@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"ok": True}


@app.get("/users")
def get_user() -> list[UserSchema]:
    return users

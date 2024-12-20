from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def general() -> str:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> str:
    return {"message": f"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def id_call(user_id: int) -> str:
    return {"message": f"Вы вошли как пользователь №{user_id}"}

@app.get("/user")
async def user_call(username: str, age: int) -> str:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


import uvicorn
import yaml

from fastapi import FastAPI, Depends, HTTPException, Request, status

with open("config.yml") as f:
    config = yaml.safe_load(f)

app = FastAPI()

# i'd like JWT authentication - don't know how yet.

@app.post(
    "/api/user",
    #response_model=
    status_code=status.HTTP_201_CREATED,
)
def create_user(create_user: schemas):# create user
    pass

@app.get(
    "/api/user/{user_id}"
    # response_model=
)
def get_user(): # you probably want public and private users.
    pass

def main():
    uvicorn.run(**config.get("uvicorn"))


if __name__ == "__main__":
    main()

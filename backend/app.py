import uvicorn
import yaml

from fastapi import FastAPI


with open("config.yml") as f:
    config = yaml.safe_load(f)

app = FastAPI()

@app.post(
    "/api/user"
)

def main():
    uvicorn.run(**config.get("uvicorn"))


if __name__ == "__main__":
    main()

from fastapi import FastAPI


app = FastAPI()


@app.route("/home")
def home():
    return "Namaste"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=5001, reload=True)
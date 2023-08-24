from fastapi import FastAPI
from kafka import KafkaProducer
import json

app = FastAPI()

producer = KafkaProducer(
    bootstrap_servers=["kafka:29092", "kafka:39092", "kafka:49092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


@app.route("/home")
def home(name: str):
    producer.send("mytopic", f"message from {name}")
    return "Namaste"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)

from fastapi import FastAPI
from kafka import KafkaProducer
import json

app = FastAPI()

producer = None

@app.on_event("startup")
async def startup_event():
    producer = KafkaProducer(
        bootstrap_servers=["kafka-1:9093", "kafka-1:9094"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
@app.post("/order/<count>")
def home(count: int):
    producer.send("mytopic", f"message from {count}")
    return count


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)

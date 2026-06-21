import os
import requests
from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import Resource

SERVICE_B_URL = os.getenv("SERVICE_B_URL", "http://service-b:8080")
OTLP_ENDPOINT = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://jaeger:4317")

resource = Resource.create({"service.name": "service-a"})
provider = TracerProvider(resource=resource)
provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=OTLP_ENDPOINT, insecure=True)))
trace.set_tracer_provider(provider)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()


@app.route("/")
def index():
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("call-service-b"):
        resp = requests.get(f"{SERVICE_B_URL}/", timeout=5)
        b_data = resp.text
    return f"service-a: ok, service-b says: {b_data}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

from flask import Flask, render_template, request
import datetime
import random

app = Flask(__name__)

# =====================================================
# COGNITIVE ENGINE
# =====================================================

class CognitiveEngine:

    def __init__(self):
        self.memory = []
        self.mode = "presentation"
        self.depth = "advanced"
        self.confidence = 0.87

        self.knowledge = {
            "introduction": {
                "basic": "AI is the simulation of human intelligence in machines.",
                "advanced": """Artificial Intelligence is a computational intelligence framework enabling
systems to perform learning, reasoning, prediction, and optimization using data-driven models."""
            },
            "technical": {
                "advanced": """AI systems operate in two phases:
Training → Pattern learning via optimization
Inference → Prediction on unseen data

Neural Equation:
Output = Activation(Σ Weight × Input + Bias)

Models optimize parameters using gradient descent."""
            },
            "applications": {
                "advanced": """Applications include:
Healthcare diagnostics
Fraud detection systems
Autonomous navigation
Adaptive education platforms
Defense analytics"""
            },
            "ethics": {
                "advanced": """AI ethics ensures:
Transparency
Accountability
Fairness
Privacy
Human Oversight

Bias originates from skewed training data."""
            },
            "philosophy": {
                "advanced": """AI is neither divine nor demonic.
It amplifies human intention embedded within data and governance."""
            },
            "future": {
                "advanced": """Future scenarios:
Regulated AI civilization
Surveillance states
Artificial Superintelligence

Outcome depends on ethical governance."""
            }
        }

    def classify(self, text):

        if "what is ai" in text or "introduction" in text:
            return "introduction"
        if "technical" in text or "how works" in text:
            return "technical"
        if "applications" in text:
            return "applications"
        if "ethics" in text or "bias" in text:
            return "ethics"
        if "god" in text or "devil" in text:
            return "philosophy"
        if "future" in text:
            return "future"

        return None

    def analytical_fallback(self, text):
        if "why" in text:
            return "This involves structural analysis of AI governance and computational modeling."
        if "how" in text:
            return "The mechanism involves algorithmic training and optimization cycles."
        return "This inquiry relates to advanced Artificial Intelligence modeling systems."

    def respond(self, user_input):
        self.memory.append(user_input)

        topic = self.classify(user_input.lower())

        if topic:
            self.confidence = min(0.99, self.confidence + 0.01)
            return self.knowledge[topic][self.depth]

        return self.analytical_fallback(user_input)

engine = CognitiveEngine()

# =====================================================
# ROUTES
# =====================================================

@app.route("/", methods=["GET", "POST"])
def home():

    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = engine.respond(user_input)

    return render_template(
        "index.html",
        response=response,
        confidence=int(engine.confidence * 100),
        memory=len(engine.memory)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

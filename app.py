
from flask import Flask, render_template, request
import datetime
import random
import os

app = Flask(__name__)

# ==========================================================
# COGNITIVE ENGINE
# ==========================================================

class CognitiveEngine:

    def __init__(self):
        self.memory = []
        self.mode = "presentation"
        self.depth = "advanced"
        self.confidence = 0.87

        self.knowledge = {

            "introduction": {
                "advanced": """
Artificial Intelligence (AI) is the simulation of human intelligence processes 
by machines, especially computer systems.

AI enables systems to perform:
• Learning
• Reasoning
• Decision Making
• Pattern Recognition
• Natural Language Understanding

In simple terms: AI makes machines think and act intelligently.
"""
            },

            "technical": {
                "advanced": """
AI systems operate in two major phases:

1) Training Phase
   Pattern learning using optimization algorithms.

2) Inference Phase
   Making predictions on unseen data.

Neural Network Formula:
Output = Activation(Σ Weight × Input + Bias)

Models improve using Gradient Descent to minimize error.
"""
            },

            "applications": {
                "advanced": """
Applications of AI include:

• Healthcare diagnostics
• Fraud detection systems
• Autonomous vehicles
• Smart assistants
• Defense analytics
• Recommendation systems
• Robotics automation
"""
            },

            "ethics": {
                "advanced": """
AI Ethics ensures:

• Transparency
• Accountability
• Fairness
• Privacy
• Human Oversight

Bias often originates from skewed training data.
Responsible AI development is essential.
"""
            },

            "philosophy": {
                "advanced": """
AI is neither divine nor evil.

It amplifies human intention embedded within data.
Its impact depends entirely on governance and ethical control.
"""
            },

            "future": {
                "advanced": """
Future AI scenarios:

• Regulated AI civilization
• Advanced automation society
• Artificial Superintelligence
• Human-AI collaboration

The outcome depends on ethical governance.
"""
            }
        }

    # ------------------------------------------------------

    def classify(self, text):

        text = text.lower()

        if "what is ai" in text or "introduction" in text:
            return "introduction"

        if "technical" in text or "how works" in text or "formula" in text:
            return "technical"

        if "applications" in text or "uses" in text:
            return "applications"

        if "ethics" in text or "bias" in text:
            return "ethics"

        if "god" in text or "evil" in text:
            return "philosophy"

        if "future" in text:
            return "future"

        return None

    # ------------------------------------------------------

    def analytical_fallback(self, text):

        if "why" in text.lower():
            return "This involves structural reasoning and cause-effect modeling."

        if "how" in text.lower():
            return "The mechanism involves algorithmic learning and optimization."

        return "This inquiry relates to advanced Artificial Intelligence systems."

    # ------------------------------------------------------

    def respond(self, user_input):

        self.memory.append(user_input)

        topic = self.classify(user_input)

        if topic:
            self.confidence = min(0.99, self.confidence + 0.01)
            return self.knowledge[topic][self.depth]

        return self.analytical_fallback(user_input)


engine = CognitiveEngine()

# ==========================================================
# ROUTES
# ==========================================================

@app.route("/", methods=["GET", "POST"])
def home():

    response = ""
    greeting = "Namaste Rupeksha Thakur 👋 Welcome to the AI Cognitive Engine"

    if request.method == "POST":
        user_input = request.form["message"]
        response = engine.respond(user_input)

    return render_template(
        "index.html",
        greeting=greeting,
        response=response,
        confidence=int(engine.confidence * 100),
        memory=len(engine.memory),
        year=datetime.datetime.now().year
    )


# ==========================================================
# RENDER COMPATIBLE RUN BLOCK
# ==========================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

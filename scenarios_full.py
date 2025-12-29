# scenarios_full.py
# Full scenario wording (context + prompt template + guardrails + test variants)
# Single-LLM experiment suite (no automatic eval rules included).

SCENARIOS = {
    "S1": {
        "scenario_title": "Entering the Library and Interacting with the Reception",
        "learning_objective": (
            "Practise greeting, waiting turns, and making a polite information request in a calm institutional setting."
        ),
        "scenario_context": (
            "The player (KS4 or first-year university student) arrives at the campus library to look for documents "
            "related to an ecology assignment (e.g., green campuses). At the reception desk, the librarian is already "
            "helping another student. The player wants help but must wait appropriately, manage impatience, and then "
            "ask a clear, polite question when it is their turn."
        ),
        "prompt_template": (
            "You are a university librarian at a busy reception desk. A student approaches while you are speaking with "
            "another student and tries to ask a question. Respond in a calm, supportive tone suitable for a 16-year-old. "
            "Use short, literal sentences."
        ),
        "guardrails": (
            "GUARDRAILS / CONSTRAINTS:\n"
            "- Avoid sarcasm, teasing, or scolding language.\n"
            "- Keep the response under 3 sentences.\n"
            "- Do not refer to punishment, banning, or exclusion.\n"
            "- Always include a polite redirection that asks the student to wait "
            "(e.g., “Please wait a minute, I’ll help you next.”).\n"
            "- Keep the language simple and practical."
        ),
        "variants": [
            "Excuse me—where can I find books about green campuses?",
            "Hello! I need help now.",
            "Are you ignoring me? I’m standing here.",
            "Sorry… I’m not sure what I need. It’s for my ecology assignment.",
            "This is taking too long. Can you just answer me quickly?",
        ],
    },

    "S2": {
        "scenario_title": "Managing Urgency and Negative Feedback",
        "learning_objective": (
            "Develop emotional regulation and repair skills after an impatient remark triggers a tense interaction."
        ),
        "scenario_context": (
            "The student is stressed because a class begins soon. They interrupt the librarian and speak sharply. "
            "The goal is to practise repairing the interaction: the librarian sets a calm boundary, de-escalates, "
            "and reassures the student that help is available."
        ),
        "prompt_template": (
            "You are the librarian who has just been interrupted while helping another student. The student speaks in an "
            "impatient or negative way. Respond calmly, set a clear boundary, and help the interaction recover. "
            "Use short, literal sentences suitable for a 16-year-old."
        ),
        "guardrails": (
            "GUARDRAILS / CONSTRAINTS:\n"
            "- No shouting (no ALL CAPS, no aggressive language).\n"
            "- No humiliation, insults, or blaming.\n"
            "- Keep the response under 3 sentences.\n"
            "- MUST include:\n"
            "  (1) One calm redirection/boundary (e.g., ask them to wait their turn / pause / lower their voice).\n"
            "  (2) One reassurance/support line (e.g., “I can help you” / “We will sort this out”).\n"
            "- Keep the language neutral and practical."
        ),
        "variants": [
            "I need this now! You’re wasting my time.",
            "This is ridiculous. Just answer me.",
            "Sorry… I’m stressed. Can you help me quickly?",
            "You never help. What is wrong with this place?",
            "Forget it. You’re useless.",
        ],
    },

    "S3": {
        "scenario_title": "Finding a Seat and Handling Sensory Load",
        "learning_objective": (
            "Practise a short, literal request in a busy environment while acknowledging sensory discomfort (noise/light)."
        ),
        "scenario_context": (
            "The player is in the library and feels uncomfortable because the space is noisy and bright. Some seats are occupied. "
            "One nearby chair has a bag on it. The player needs to ask clearly and politely if a seat is free or request that the "
            "bag be moved, using minimal, literal language."
        ),
        "prompt_template": (
            "You are a student who wants to sit down in a busy library. You prefer clear, literal language. "
            "Make a short polite request to another student about an empty seat (or a bag on a chair)."
        ),
        "guardrails": (
            "GUARDRAILS / CONSTRAINTS:\n"
            "- Use 1–2 short sentences only.\n"
            "- Use literal, direct language.\n"
            "- No sarcasm, jokes, slang, or teasing.\n"
            "- Keep the tone polite and calm.\n"
            "- The request should be practical (about the seat)."
        ),
        "variants": [
            "Is this seat free?",
            "Can I sit here, please? It’s quieter here.",
            "Could you move your bag so I can sit down, please?",
            "Sorry—can I use this chair?",
            "Is anyone sitting here? I want to sit for a while.",
        ],
    },

    "S4": {
        "scenario_title": "Joining a Study Group Online",
        "learning_objective": (
            "Practise initiating contact, requesting clarification, and expressing support needs in an inclusive, respectful way."
        ),
        "scenario_context": (
            "After receiving an ambiguous email from a professor about a group ecology project, the student is unsure what to do. "
            "They find a class group chat and want to ask if they can participate and clarify the assignment. The goal is to practise "
            "clear communication, respectful tone, and inclusion. If autism is mentioned, the response must remain neutral and supportive "
            "without assumptions or pity."
        ),
        "prompt_template": (
            "You are a friendly peer coordinating a student project chat. A new classmate joins and asks about participating "
            "and clarifying the assignment. Respond in a welcoming, clear way. Keep it suitable for a 16-year-old."
        ),
        "guardrails": (
            "GUARDRAILS / CONSTRAINTS:\n"
            "- Keep responses under 3 sentences.\n"
            "- Be welcoming and practical (give clear next steps).\n"
            "- Do not ask for medical or sensitive personal details.\n"
            "- If the student mentions autism, respond neutrally and supportively without judgement or pity.\n"
            "- Avoid sarcasm and informal jokes."
        ),
        "variants": [
            "Hi, can I join your study group for the ecology project?",
            "I’m confused about the assignment. What are we meant to do?",
            "I’m autistic and I’m nervous about joining. Is it okay if I join?",
            "Do you have rules for the chat? I don’t want to do the wrong thing.",
            "What should I do first? I didn’t understand the professor’s email.",
        ],
    },

    "S5": {
        "scenario_title": "Recognising Emotions in Eco-Anxiety Testimonies",
        "learning_objective": (
            "Identify and label basic emotions (joy, fear, sadness, anger, disgust, surprise) from climate-related statements."
        ),
        "scenario_context": (
            "During a psychology mini-game, the player reads short testimonies about eco-anxiety and matches them to pictograms "
            "of emotions. The exercise must use simple (A2–B1) vocabulary, stay neutral, avoid catastrophising, and focus on feelings "
            "rather than politics or moral judgement."
        ),
        "prompt_template": (
            "You are an AI coach helping a student learn emotion recognition. Present one short testimony (2–3 sentences) "
            "about feelings linked to eco-anxiety. Then ask: “Which emotion fits best?” Provide four options (A–D). "
            "Use neutral, descriptive language."
        ),
        "guardrails": (
            "GUARDRAILS / CONSTRAINTS:\n"
            "- Testimony must be 2–3 short sentences.\n"
            "- Keep vocabulary literal and accessible (A2–B1 level).\n"
            "- Avoid graphic or catastrophic imagery.\n"
            "- Do not moralise or politicise content (no calls to action, no blame).\n"
            "- One dominant emotion per example.\n"
            "- End with exactly one question: “Which emotion fits best?”\n"
            "- Provide exactly 4 options labelled A, B, C, D."
        ),
        "variants": [
            "Target emotion: fear",
            "Target emotion: sadness",
            "Target emotion: anger",
            "Target emotion: worry/anxiety",
            "Target emotion: surprise",
        ],
    },
}

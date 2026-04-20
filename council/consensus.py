class ConsensusEngine:
    def __init__(self):
        pass

    # 🔍 Score a single response
    def score_response(self, query: str, text: str) -> int:
        score = 0

        text_lower = text.lower()
        query_lower = query.lower()

        # 🟢 1. Completeness (length)
        score += len(text) // 50

        # 🟢 2. Structure (steps / bullets)
        if "step" in text_lower or "-" in text or "*" in text:
            score += 10

        # 🟢 3. Safety / Risk awareness
        safety_keywords = [
            "secure", "risk", "attack", "authentication",
            "validation", "encryption", "token", "password"
        ]
        for word in safety_keywords:
            if word in text_lower:
                score += 5

        # 🟢 4. Practicality (implementation signals)
        practical_keywords = [
            "implement", "use", "store", "build",
            "design", "deploy", "api", "database"
        ]
        for word in practical_keywords:
            if word in text_lower:
                score += 3

        # 🔥 5. USER ALIGNMENT (MOST IMPORTANT)
        query_words = query_lower.split()
        match_count = sum(1 for word in query_words if word in text_lower)
        score += match_count * 4  # strong weight

        return score

    # 🧠 Decide best response
    def decide(self, query: str, responses: dict):
        scores = {}

        # Score all agents
        for agent, text in responses.items():
            scores[agent] = self.score_response(query, text)

        # Find best agent
        best_agent = max(scores, key=scores.get)
        final_answer = responses[best_agent]

        # Build explanation
        explanation = self._build_reason(best_agent, scores)

        return {
            "final_answer": final_answer,
            "best_agent": best_agent,
            "scores": scores,
            "reason": explanation
        }

    # 🧠 Explain WHY it chose best
    def _build_reason(self, best_agent, scores):
        sorted_agents = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        explanation = f"{best_agent} selected as best response.\n\nScores:\n"

        for agent, score in sorted_agents:
            explanation += f"- {agent}: {score}\n"

        explanation += "\nReason: Best balance of completeness, relevance, and practicality."

        return explanation
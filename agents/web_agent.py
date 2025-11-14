import google.generativeai as genai

class WebAgent:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash-latest")

    def handle(self, query):
        prompt = f"""
        You are a helpful web intelligence agent.

        USER QUERY:
        {query}

        Provide a clear answer.
        """

        response = self.model.generate_content(prompt)
        return response.text

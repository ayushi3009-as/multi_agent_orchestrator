from agents.document_agent import DocumentAgent

class Orchestrator:

    def __init__(self):
        self.doc_agent = DocumentAgent()

    def route(self, query, text):
        return self.doc_agent.handle(query, text)

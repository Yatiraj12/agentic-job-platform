"""
Simple in-memory conversation memory store
"""

class ConversationMemory:

    def __init__(self):
        self.memory = {}

    def add_message(self, session_id, role, content):

        if session_id not in self.memory:
            self.memory[session_id] = []

        self.memory[session_id].append({
            "role": role,
            "content": content
        })

    def get_history(self, session_id):

        return self.memory.get(session_id, [])

memory_store = ConversationMemory()
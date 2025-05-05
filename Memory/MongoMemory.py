from langchain.chains import LLMChain

class MongoMemory:

    def __init__(self, collection):
        self.collection = collection

    def save_message(self, user_input, bot_response, food_style, difficulty):
        self.collection.insert_one({"user": user_input, "bot": bot_response,"food_style": food_style, "difficulty": difficulty})

    def load_messages(self):
        messages = self.collection.find({}, {"_id": 0})
        return [f"User: {m['user']}\nBot: {m['bot']}" for m in messages]

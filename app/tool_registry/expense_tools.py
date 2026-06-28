TOOLS_EXPENSES = [
    {   
        "type": "function",
        "name": "add_expense",
        "description": "Add a new expense",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": { "type": "number" },
                "category": { "type": "string" },
                "description": { "type": "string" }
            }
        }
    },
    {
        "type": "function",
        "name": "get_expenses",
        "description": "Get all expenses",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]

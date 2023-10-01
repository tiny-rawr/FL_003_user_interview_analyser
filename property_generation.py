def generate_properties(questions):
    properties = {
        "interview": {
            "type": "object",
            "properties": {}
        }
    }

    for question in questions:
        description = f"A direct quote from the interview that answers the question '{question}'"
        properties["interview"]["properties"][question] = {
            "type": "array",
            "items": {
                "type": "string",
                "description": description
            }
        }

    return properties
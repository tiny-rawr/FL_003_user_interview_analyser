import openai
import json

def gpt_api_call(model_type, system_behaviour, user_submitted_content, name_of_function, function_description, properties, required_properties):
    api_call = openai.ChatCompletion.create(
        model=model_type,
        messages=[
            {"role": "system", "content": system_behaviour},
            {"role": "user", "content": user_submitted_content}
        ],
        functions=[{
            "name": name_of_function,
            "description": function_description,
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required_properties
            }
        }],
        function_call={"name": name_of_function}
    )
    output = api_call["choices"][0]["message"]
    data = json.loads(output["function_call"]["arguments"]) if output.get("function_call") else {}

    data = data.get('interview', [])
    return data


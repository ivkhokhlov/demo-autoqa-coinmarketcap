from pydantic import BaseModel, ValidationError
from typing import Optional


def is_object_matches_model(parsed_json: dict, model_class) -> bool:
    try:
        response = model_class.model_validate(parsed_json)
        return True
    except ValidationError as e:
        print("Validation error:", e)
        return False
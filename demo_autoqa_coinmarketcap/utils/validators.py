from pydantic import ValidationError
from structlog import get_logger

logger = get_logger()


def is_object_matches_model(parsed_json: dict, model_class) -> bool:
    try:
        response = model_class.model_validate(parsed_json)
        return True
    except ValidationError as e:
        logger.error(e)
        return False

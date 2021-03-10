# The F401 error code is "imported but unused"
# ignoring it here because this module is imported to register handlers in submodules
from . import core, permission, sbml, user  # noqa: F401
from .signals import (
    errors_reported,
    study_modified,
    study_removed,
    type_modified,
    type_removed,
    user_modified,
    user_removed,
    warnings_reported,
)

# doing `from main.signals import *` will import these names
__all__ = [
    "errors_reported",
    "study_modified",
    "study_removed",
    "type_modified",
    "type_removed",
    "user_modified",
    "user_removed",
    "warnings_reported",
]

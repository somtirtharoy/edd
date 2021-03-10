from django.utils.translation import gettext_lazy as _

from main.exceptions import EDDError, EDDWarning, MessagingMixin


class LoadError(EDDError):
    """
    Parent Exception for all exception types in the edd.load app.

    Contains no boilerplate meant for reading by end-users by default.
    """

    pass


class LoadWarning(EDDWarning):
    """
    Parent Warning for "plain" import/load warnings.

    Contains no boilerplate meant for reading by end-users.
    """

    pass


class EDDImportError(MessagingMixin, LoadError):
    def __init__(self, **kwargs):
        if "category" not in kwargs:
            kwargs.update(category=_("Uncategorized Error"))
        super().__init__(**kwargs)


class EDDImportWarning(MessagingMixin, LoadWarning):
    def __init__(self, **kwargs):
        if "category" not in kwargs:
            kwargs.update(category=_("Uncategorized Warning"))
        super().__init__(**kwargs)


class InvalidLoadRequestError(EDDImportError):
    def __init__(self, **kwargs):
        super().__init__(
            category=_("Invalid ID"),
            summary=_("Data loading request was not found"),
            **kwargs,
        )

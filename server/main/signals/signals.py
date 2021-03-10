import django.dispatch

study_modified = django.dispatch.Signal(providing_args=["study", "using"])
study_removed = django.dispatch.Signal(providing_args=["doc", "using"])
type_modified = django.dispatch.Signal(providing_args=["measurement_type", "using"])
type_removed = django.dispatch.Signal(providing_args=["doc", "using"])
user_modified = django.dispatch.Signal(providing_args=["user", "using"])
user_removed = django.dispatch.Signal(providing_args=["doc", "using"])

# create signals for errors and warnings
errors_reported = django.dispatch.Signal(providing_args=["key", "errors"])
warnings_reported = django.dispatch.Signal(providing_args=["key", "warnings"])

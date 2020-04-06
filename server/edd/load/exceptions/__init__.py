"""Module contains exceptions for edd.load."""

from .core import EDDImportError, EDDImportWarning, LoadError, ReportingLimitWarning
from .execute import (
    ExecutionError,
    ExecutionWarning,
    MissingAssayError,
    MissingLineError,
    UnplannedOverwriteError,
)
from .parse import (
    BadParserError,
    DuplicateColumnError,
    EmptyFileError,
    IgnoredColumnWarning,
    IgnoredValueWarning,
    IgnoredWorksheetWarning,
    InvalidValueError,
    MissingParameterError,
    ParseError,
    RequiredColumnError,
    RequiredValueError,
    UnsupportedMimeTypeError,
    UnsupportedUnitsError,
)
from .resolve import (
    CommunicationError,
    CompartmentNotFoundError,
    DuplicateAssayError,
    DuplicateLineError,
    DuplicateMergeWarning,
    DuplicationWarning,
    GeneNotFoundError,
    IllegalTransitionError,
    ImportConflictWarning,
    ImportTooLargeError,
    InvalidIdError,
    MeasurementCollisionError,
    MergeWarning,
    MetaboliteNotFoundError,
    MissingAssayTimeError,
    OverdeterminedTimeError,
    OverwriteWarning,
    PhosphorNotFoundError,
    ProteinNotFoundError,
    ResolveError,
    ResolveWarning,
    TimeNotProvidedError,
    TimeUnresolvableError,
    UnexpectedError,
    UnitsNotProvidedError,
    UnmatchedAssayError,
    UnmatchedLineError,
    UnmatchedMtypeError,
    UnmatchedNamesError,
    UnmatchedStudyInternalsError,
)
from .table import ImportBoundsError, ImportTaskError

__all__ = [
    "BadParserError",
    "CommunicationError",
    "CompartmentNotFoundError",
    "DuplicateAssayError",
    "DuplicateColumnError",
    "DuplicateLineError",
    "DuplicateMergeWarning",
    "DuplicationWarning",
    "EDDImportError",
    "EDDImportWarning",
    "EmptyFileError",
    "ExecutionError",
    "ExecutionWarning",
    "GeneNotFoundError",
    "IgnoredColumnWarning",
    "IgnoredValueWarning",
    "IgnoredWorksheetWarning",
    "IllegalTransitionError",
    "ImportBoundsError",
    "ImportConflictWarning",
    "ImportTaskError",
    "ImportTooLargeError",
    "InvalidIdError",
    "InvalidValueError",
    "LoadError",
    "MeasurementCollisionError",
    "MergeWarning",
    "MetaboliteNotFoundError",
    "MissingAssayError",
    "MissingAssayTimeError",
    "MissingLineError",
    "MissingParameterError",
    "OverdeterminedTimeError",
    "OverwriteWarning",
    "ParseError",
    "PhosphorNotFoundError",
    "ProteinNotFoundError",
    "ReportingLimitWarning",
    "RequiredColumnError",
    "RequiredValueError",
    "ResolveError",
    "ResolveWarning",
    "TimeNotProvidedError",
    "TimeUnresolvableError",
    "UnexpectedError",
    "UnitsNotProvidedError",
    "UnmatchedAssayError",
    "UnmatchedLineError",
    "UnmatchedMtypeError",
    "UnmatchedNamesError",
    "UnmatchedStudyInternalsError",
    "UnplannedOverwriteError",
    "UnsupportedMimeTypeError",
    "UnsupportedUnitsError",
]

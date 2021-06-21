from uuid import uuid4

import pytest

from .. import exceptions, parsers, reporting
from ..signals import warnings_reported
from . import factory


def test_AmbrExcelParser_success():

    path = ("ambr_export_test_data.xlsx",)
    parser = parsers.AmbrExcelParser(uuid4())

    with factory.load_test_file(*path) as file:
        parsed = parser.parse(file)
    verify_generic_parse_result(parsed)


def test_GenericExcelParser_success():

    path = ("generic_import.xlsx",)
    parser = parsers.GenericExcelParser(uuid4())

    with factory.load_test_file(*path) as file:
        parsed = parser.parse(file)
    # verify_generic_parse_result(parsed)


def verify_generic_parse_result(parsed):
    pass
    # # Utility method that compares parsed content from XLSX and CSV format files,
    # # verifying that:
    # #     A) the results are correct, and
    # #     B) that they're consistent regardless of file format.
    #
    # # verify that expected values were parsed
    # assert parsed is not None
    # assert parsed.line_or_assay_names == {"A", "B"}
    # assert parsed.mtypes == {"CID:440917", "CID:5288798"}
    # record_count = len(parsed.series_data)
    # assert record_count == 2
    # assert parsed.any_time is True
    # assert parsed.has_all_times is True
    # assert parsed.record_src == "row"
    # assert parsed.units == {"g/L", "hours"}
    # # drill down and verify that ParseRecords were created as expected
    # assert len(parsed.series_data) == 2
    # first = parsed.series_data[0]
    # assert first.loa_name == "A"
    # assert first.mtype_name == "CID:440917"
    # assert first.y_unit_name == "g/L"
    # assert first.x_unit_name == "hours"
    # assert first.value_format == "0"
    # assert first.data == [[8], [1]]
    # second = parsed.series_data[1]
    # assert second.loa_name == "B"
    # assert second.mtype_name == "CID:5288798"
    # assert second.y_unit_name == "g/L"
    # assert second.x_unit_name == "hours"
    # assert second.value_format == "0"
    # assert second.data == [[24], [2]]

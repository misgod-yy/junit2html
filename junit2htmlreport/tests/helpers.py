"""
Helper funcs for tests
"""
import os
from inputfiles import get_filepath
from junit2htmlreport import runner


def run_runner(tmpdir, filename):
    """
    Run the junit2html program against the given report and produce a html doc
    :param tmpdir:
    :param filename:
    :return:
    """
    testfile = get_filepath(filename=filename)
    outfile = os.path.join(tmpdir.strpath, "report.html")
    runner.run([testfile, outfile])
    assert os.path.exists(outfile)


def test_runner_simple(tmpdir):
    """
    Test the stand-alone app with a simple fairly empty junit file
    :param tmpdir:  py.test tmpdir fixture
    :return:
    """
    run_runner(tmpdir, "junit-simple_suites.xml")

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import fetch as module_0
import scrapy.exceptions as module_1


def test_case_0():
    command_0 = module_0.Command()


def test_case_1():
    command_0 = module_0.Command()
    var_0 = command_0.syntax()
    assert var_0 == "[options] <url>"


def test_case_2():
    command_0 = module_0.Command()
    var_0 = command_0.short_desc()
    assert var_0 == "Fetch a URL using the Scrapy downloader"
    var_1 = command_0.set_crawler(command_0)
    command_1 = module_0.Command()
    command_2 = module_0.Command()


def test_case_3():
    command_0 = module_0.Command()
    var_0 = command_0.long_desc()
    assert (
        var_0
        == "Fetch a URL using the Scrapy downloader and print its content to stdout. You may want to use --nolog to disable logging"
    )
    var_1 = command_0.syntax()
    assert var_1 == "[options] <url>"
    command_1 = module_0.Command()
    command_2 = module_0.Command()
    str_0 = "Z"
    with pytest.raises(module_1.UsageError):
        command_0.run(str_0, command_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    command_0 = module_0.Command()
    command_0.add_options(command_0)


def test_case_5():
    command_0 = module_0.Command()
    var_0 = module_0.Command()
    var_1 = command_0.syntax()
    assert var_1 == "[options] <url>"
    with pytest.raises(module_1.UsageError):
        command_0.run(var_1, var_1)


def test_case_6():
    command_0 = module_0.Command()
    str_0 = "Z"
    with pytest.raises(module_1.UsageError):
        command_0.run(str_0, command_0)

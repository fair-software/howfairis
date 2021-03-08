from howfairis.readme import Readme
from howfairis.readme_format import ReadmeFormat
from tests.helpers.load_snippets_from_local_data import load_snippets_from_local_data


def test_1():
    rst_filename = "1-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    readme = Readme(filename=None, text=original_text, file_format=ReadmeFormat.RESTRUCTUREDTEXT)
    actual_text = readme.text
    expected_text = snippets["/1-expected.rst"]
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text, \
           "expected the second paragraph with normal text to still be there."
    assert actual_text == expected_text


def test_2():
    rst_filename = "2-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    readme = Readme(filename=None, text=original_text, file_format=ReadmeFormat.RESTRUCTUREDTEXT)
    actual_text = readme.text
    expected_text = snippets["/2-expected.rst"]
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text, \
           "expected the second paragraph with normal text to still be there."
    assert actual_text == expected_text


def test_3():
    rst_filename = "3-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    readme = Readme(filename=None, text=original_text, file_format=ReadmeFormat.RESTRUCTUREDTEXT)
    actual_text = readme.text
    expected_text = snippets["/3-expected.rst"]
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text, \
           "expected the second paragraph with normal text to still be there."
    assert actual_text == expected_text


def test_4():
    rst_filename = "4-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    readme = Readme(filename=None, text=original_text, file_format=ReadmeFormat.RESTRUCTUREDTEXT)
    actual_text = readme.text
    expected_text = snippets["/4-expected.rst"]
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text,\
           "expected the second paragraph with normal text to still be there."
    assert actual_text == expected_text


def test_5():
    rst_filename = "5-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    readme = Readme(filename=None, text=original_text, file_format=ReadmeFormat.RESTRUCTUREDTEXT)
    actual_text = readme.text
    expected_text = snippets["/5-expected.rst"]
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "https://img.shields.io/badge/ascl-1410.001-red" in actual_text, "expected the ascl badge to still be there"
    assert "https://bestpractices.coreinfrastructure.org/projects/4630/badge" in actual_text, \
           "expected the core infrastructures badge to still be there"
    assert "These badges are nested deeper in the DOM than regular text:" in actual_text, \
           "expected the first paragraph with normal text to still be there."
    assert actual_text == expected_text


def test_6():
    rst_filename = "6-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    readme = Readme(filename=None, text=original_text, file_format=ReadmeFormat.RESTRUCTUREDTEXT)
    actual_text = readme.text
    expected_text = snippets["/6-expected.rst"]
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert actual_text == expected_text

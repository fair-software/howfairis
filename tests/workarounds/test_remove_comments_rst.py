from howfairis.workarounds.remove_comments_rst import remove_comments_rst
from tests.helpers.load_snippets_from_local_data import load_snippets_from_local_data


def test_1():
    rst_filename = "1-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    actual_text = remove_comments_rst(original_text)
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text, \
           "expected the second paragraph with normal text to still be there."
    assert actual_text == "This is normal text\n\nThis is more normal text"


def test_2():
    rst_filename = "2-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    actual_text = remove_comments_rst(original_text)
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text, \
           "expected the second paragraph with normal text to still be there."
    assert actual_text == "This is normal text\n\nThis is more normal text"


def test_3():
    rst_filename = "3-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    actual_text = remove_comments_rst(original_text)
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text, \
           "expected the second paragraph with normal text to still be there."
    assert actual_text == "This is normal text\n\nThis is more normal text"


def test_4():
    rst_filename = "4-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    actual_text = remove_comments_rst(original_text)
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text,\
           "expected the second paragraph with normal text to still be there."
    assert actual_text == "This is normal text\n\nThis is more normal text"


def test_5():
    rst_filename = "5-original.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    actual_text = remove_comments_rst(original_text)
    expected_text = snippets["/5-expected.rst"]
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "https://img.shields.io/badge/ascl-1410.001-red" in actual_text, "expected the ascl badge to still be there"
    assert "https://bestpractices.coreinfrastructure.org/projects/4630/badge" in actual_text, \
           "expected the core infrastructures badge to still be there"
    assert "These badges are nested deeper in the DOM than regular text:" in actual_text, \
           "expected the first paragraph with normal text to still be there."
    assert actual_text == expected_text

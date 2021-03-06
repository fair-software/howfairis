from howfairis.workarounds.remove_comments_rst import remove_comments_rst
from tests.helpers.load_snippets_from_local_data import load_snippets_from_local_data


def test_1():
    rst_filename = "comment-1.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    actual_text = remove_comments_rst(original_text)
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text, "expected the second paragraph with normal text to still be there."
    assert actual_text == "This is normal text\n\nThis is more normal text"


def test_2():
    rst_filename = "comment-2.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    actual_text = remove_comments_rst(original_text)
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text, "expected the second paragraph with normal text to still be there."
    assert actual_text == "This is normal text\n\nThis is more normal text"


def test_3():
    rst_filename = "comment-3.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    actual_text = remove_comments_rst(original_text)
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text, "expected the second paragraph with normal text to still be there."
    assert actual_text == "This is normal text\n\nThis is more normal text"


def test_4():
    rst_filename = "comment-4.rst"
    snippets = load_snippets_from_local_data(__file__)
    original_text = snippets["/" + rst_filename]
    actual_text = remove_comments_rst(original_text)
    assert actual_text != original_text, "expected the comment to have been removed."
    assert "This is a comment in rst" not in actual_text, "expected the comment to have been removed."
    assert "This is normal text" in actual_text, "expected the first paragraph with normal text to still be there."
    assert "This is more normal text" in actual_text, "expected the second paragraph with normal text to still be there."
    assert actual_text == "This is normal text\n\nThis is more normal text"

from howfairis.readme import Readme
from howfairis.readme_format import ReadmeFormat


class TestRemoveCommentsFromRst:
    def test_withoutcomment_unchanged(self):
        text = '''
Hello
-----

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4017908.svg
   :target: https://doi.org/10.5281/zenodo.4017908
'''
        readme = Readme('README.rst', text, ReadmeFormat.RESTRUCTUREDTEXT)
        readme.remove_comments()

        assert 'zenodo.org/badge/DOI/10.5281/zenodo.4017908' in readme.text

    def test_withcommenteachline_commentgone(self):
        text = '''
Hello
-----

.. .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4017908.svg
..    :target: https://doi.org/10.5281/zenodo.4017908

'''
        readme = Readme('README.rst', text, ReadmeFormat.RESTRUCTUREDTEXT)
        readme.remove_comments()

        assert '10.5281' not in readme.text

    def test_withcmultiline_commentgone(self):
        text = '''
Hello
-----

.. This text will not be shown
   (but, for instance, in HTML might be
   rendered as an HTML comment)

Bla
'''
        readme = Readme('README.rst', text, ReadmeFormat.RESTRUCTUREDTEXT)
        readme.remove_comments()

        expected = '''
Hello
-----


Bla
'''
        assert readme.text == expected

    def test_speccomment_allgone(self):
        # Text from https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#comments
        text = '''
.. This is a comment

..
   _so: is this!

..
   [and] this!

..
   this:: too!

..
   |even| this:: !

.. [this] however, is a citation
'''
        readme = Readme('README.rst', text, ReadmeFormat.RESTRUCTUREDTEXT)
        readme.remove_comments()

        expected = '''
.. [this] however, is a citation
'''
        print(repr(readme.text))
        assert readme.text == expected

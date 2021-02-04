from howfairis.Readme import Readme
from howfairis.ReadmeFormat import ReadmeFormat


class TestRemoveCommentsFromRst:
    def test_rstwithoutcomment_unchanged(self):
        text = '''
Hello
-----

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4017908.svg
   :target: https://doi.org/10.5281/zenodo.4017908
'''
        readme = Readme('README.rst', text, ReadmeFormat.RESTRUCTUREDTEXT)
        readme.remove_comments()

        assert 'zenodo.org/badge/DOI/10.5281/zenodo.4017908' in readme.text

    def test_rstwithcommenteachline_commentgone(self):
        text = '''
Hello
-----

.. .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4017908.svg
..    :target: https://doi.org/10.5281/zenodo.4017908
'''
        readme = Readme('README.rst', text, ReadmeFormat.RESTRUCTUREDTEXT)
        readme.remove_comments()

        assert 'zenodo.org/badge/DOI/10.5281/zenodo.4017908' not in readme.text


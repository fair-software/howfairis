import inspect
import re
import requests
from colorama import Fore
from colorama import Style
from howfairis.Compliance import Compliance
from howfairis.mixins import ChecklistMixin
from howfairis.mixins import CitationMixin
from howfairis.mixins import LicenseMixin
from howfairis.mixins import RegistryMixin
from howfairis.mixins import RepositoryMixin
from howfairis.Readme import Readme
from howfairis.ReadmeFormat import ReadmeFormat


class Checker(RepositoryMixin, LicenseMixin, RegistryMixin, CitationMixin, ChecklistMixin):
    def __init__(self, config, repo):
        super().__init__()
        self.compliance = None
        self.config = config
        self.readme = None
        self.repo = repo
        self.badge = None
        self.badge_url = None

        self._get_readme()

    def _eval_regexes(self, regexes, check_name=None):
        if check_name is None:
            # get name of the function who's calling me
            check_name = inspect.stack()[1].function
        if self.readme.text is None:
            self._print_state(check_name=check_name, state=False)
            return False
        for regex in regexes:
            if re.compile(regex).search(self.readme.text) is not None:
                self._print_state(check_name=check_name, state=True)
                return True
        self._print_state(check_name=check_name, state=False)
        return False

    def _get_readme(self):
        def remove_comments(text):
            return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

        for readme_filename in ["README.rst", "README.md"]:
            raw_url = self.repo.raw_url_format_string.format(readme_filename)
            try:
                response = requests.get(raw_url)
                # If the response was successful, no Exception will be raised
                response.raise_for_status()
            except requests.HTTPError:
                continue

            if readme_filename == "README.md":
                readme_fmt = ReadmeFormat.MARKDOWN
            elif readme_filename == "README.rst":
                readme_fmt = ReadmeFormat.RESTRUCTUREDTEXT
            else:
                readme_fmt = None

            if self.config.merged.get("include_comments") is True:
                text = response.text
            else:
                text = remove_comments(response.text)
            self.readme = Readme(filename=readme_filename, text=text, fmt=readme_fmt)
            return self

        print("Did not find a README[.md|.rst] file at " + raw_url.replace(readme_filename, ""))
        self.readme = Readme(filename=None, text=None, fmt=None)
        return self

    @staticmethod
    def _print_state(check_name="", state=None, indent=6):
        if state is True:
            print(" " * indent + Style.BRIGHT + Fore.GREEN + "\u2713 " + Style.RESET_ALL + check_name)
        elif state is False:
            print(" " * indent + Style.BRIGHT + Fore.RED + "\u00D7 " + Style.RESET_ALL + check_name)

    def _calc_badge(self):
        score = self.compliance.count(True)

        if score in [0, 1]:
            color_string = "red"
        elif score in [2, 3]:
            color_string = "orange"
        elif score in [4]:
            color_string = "yellow"
        elif score == 5:
            color_string = "green"

        self.badge_url = "https://img.shields.io/badge/fair--software.eu-{0}-{1}".format(self.compliance.urlencode(),
                                                                                         color_string)
        if self.readme.fmt == ReadmeFormat.RESTRUCTUREDTEXT:
            self.badge = ".. image:: {0}\n   :target: {1}".format(self.badge_url, "https://fair-software.eu")
        if self.readme.fmt == ReadmeFormat.MARKDOWN:
            self.badge = "[![fair-software.eu]({0})]({1})".format(self.badge_url, "https://fair-software.eu")

        return self

    def has_open_brackets(self, badges):
        if len(badges) == 0:
            return(False)
        last_badge = badges[-1]
        bracket_counts = { "[":0, "]":0 } 
        for i, c in enumerate(last_badge):
            if last_badge[i] == "[" or last_badge[i] == "]":
                bracket_counts[c] += 1
        return(bracket_counts["["] > bracket_counts["]"] or
               (bracket_counts["["] == 0 and bracket_counts["]"] == 0))

    def finishes_with_image_tag(self, badges):
        return(len(badges) > 0 and re.search("image::$", badges[-1]))

    def get_badges_rst(self):
        badges = []
        for text_part in self.readme.text.split():
            if re.search("image::", text_part) or self.finishes_with_image_tag(badges):
                badges.append(text_part)
        return("\n".join(badges))

    def get_badges_md(self):
        badges = []
        for text_part in self.readme.text.split():
            if re.search('![[]', text_part) or self.has_open_brackets(badges):
                badges.append(text_part)
        return("\n".join(badges))

    def get_badges(self):
        if self.readme.text is None:
            return False
        if self.readme.fmt == ReadmeFormat.MARKDOWN:
            return(self.get_badges_md())
        if self.readme.fmt == ReadmeFormat.RESTRUCTUREDTEXT:
            return(self.get_badges_rst())
        return(self)

    def check_five_recommendations(self):
        badges = Checker(self.config, self.repo)
        badges.readme = Readme(filename=self.readme.filename,
                               text=self.get_badges(),
                               fmt=self.readme.fmt)
        self.compliance = Compliance(repository=badges.check_repository(),
                                     license_=badges.check_license(),
                                     registry=badges.check_registry(),
                                     citation=badges.check_citation(),
                                     checklist=badges.check_checklist())
        self._calc_badge()
        return self

def get_mocked_responses():
    return [
        (("http://github.com/fair-software/badge", ), dict(text="dummy response")),
        (("https://api.github.com/repos/fair-software/badge", ), dict(json=dict(default_branch="master")))
    ]

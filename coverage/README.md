# Coverage reporting

The coverage reports will be written in this directory. After running `pytest`, the directory should look more or less like this:

```text
coverage/
├── .coverage
├── coverage.xml
├── htmlcov
│   ├── coverage_html.js
│   ├── fairtally_check_py.html
│   ├── fairtally_cli_py.html
│   ├── fairtally___init___py.html
│   ├── fairtally_redirect_stdout_stderr_py.html
│   ├── fairtally_utils_py.html
│   ├── fairtally___version___py.html
│   ├── favicon_32.png
│   ├── index.html
│   ├── jquery.ba-throttle-debounce.min.js
│   ├── jquery.hotkeys.js
│   ├── jquery.isonscreen.js
│   ├── jquery.min.js
│   ├── jquery.tablesorter.min.js
│   ├── keybd_closed.png
│   ├── keybd_open.png
│   ├── status.json
│   └── style.css
└── README.md
```

Everything except the README is generated (see configuration in `/.coveragerc`).

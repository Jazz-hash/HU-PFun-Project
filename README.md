# HU-PFun-Project

## Semester 1 Project - Programming Fundamentals

### Web Crawler &nbsp;&nbsp;[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg) &nbsp;![GitHub release](https://img.shields.io/github/release/Jazz-hash/HU-PFun-Project)](https://github.com/Jazz-hash/HU-PFun-Project)

#### URL: [https://hu-web-crawler.herokuapp.com/](https://hu-web-crawler.herokuapp.com/)

#### Environment: &nbsp; [![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.org/project/pip/)

- Tested and verified by github actions [https://github.com/Jazz-hash/HU-PFun-Project/actions](https://github.com/Jazz-hash/HU-PFun-Project/actions)

## Prerequisite

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

- python and pip ( version = "\*" )

  Visit [https://www.python.org/](https://www.python.org/) and download any version of python for your operating system.

  ```
  # For verification open command prompt or terminal and run
  python --version
  Output: Python 3.x.x
  ```

- pipenv ( version = "\*" )
  ```
  pip install pipenv
  # Again for verification
  pipenv --version
  Output: pipenv, version 2020.x.x
  ```

## Available Scripts

- Download Project files

  - Clone
    ```
    git clone https://github.com/Jazz-hash/HU-PFun-Project
    cd HU-PFun-Project/
    ```
    <bold>Or</bold>
  - Download the repository from [https://github.com/Jazz-hash/HU-PFun-Project](https://github.com/Jazz-hash/HU-PFun-Project) then move to the directory where you downloaded or cloned the repository and cd into project directory.

    `cd HU-PFun-Project-main/`

- Install dependencies
  ```
  pipenv install -r requirements.txt
  ```
- Launching in project's virtual environment
  ```
  pipenv shell
  ```
- Testing
  ```
  python test.py
  Output: Test Passed ! All libraries working.
  ```
- Importing variables
  - For linux users
    `export FLASK_APP=app/server.py && export FLASK_ENV=development`
  - For windows users
    `SET FLASK_APP=app/server.py SET FLASK_ENV=development`
- Now for the final step
  ```
  flask run
  Output:
   * Serving Flask app "app/server.py" (lazy loading)
   * Environment: development
   * Debug mode: on
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   * Restarting with inotify reloader
   * Debugger is active!
   * Debugger PIN: 164-091-533
  ```
- Open browser and enter address [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and hit enter.

### Magic happens !!

- Refer to project manual for instructions located in <b>docs</b> folder on how to use this efficient tool.
- Docs: `cd <project-main-directory>/docs/`
  - Project-Report.pdf
  - Project-Manual.pdf
- Video: [Click here !](https://drive.google.com/file/d/1iXGdbSQzdcHMSISSeLjCFeqlFeMaN1br/view?usp=sharing)

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)&nbsp;![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
]()

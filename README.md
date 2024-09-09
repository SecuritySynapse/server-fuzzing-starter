# 🔬 Server Fuzzing

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## ✨ Table of Contents

<!---toc start-->

* [🔬 Server Fuzzing](#-server-fuzzing)
  * [✨ Table of Contents](#-table-of-contents)
  * [🏁 Introduction](#-introduction)
  * [🤝 Seeking Assistance](#-seeking-assistance)
  * [🛫 Project Overview](#-project-overview)

<!---toc end-->

## 🏁 Introduction

If you are a student completing this project as part of a class at Allegheny
College, you can check the schedule on the course web site for the due date or
ask the course instructor for more information about the due date. Please note
that the content provided in the `README.md` file for this GitHub repository is
an overview of the project and thus may not include the details for every step
needed to successfully complete every project deliverable. This means that you
may need to schedule a meeting during the course instructor's office hours to
discuss aspects of this project. Finally, it is important to point out that
your repository for this project was created from the GitHub repository
template called
[server-fuzzing-starter](https://github.com/SecuritySynapse/server-fuzzing-starter);
you can check this repository for any updates to this project's documentation
or source code!

## 🤝 Seeking Assistance

Even though the course instructor will have covered all of the concepts central
to this project before you start to work on it, please note that not every
detail needed to successfully complete the assignment will have been covered
during prior classroom sessions. This is by design as an important skill that
you must practice as an algorithm engineer is to search for and then understand
and ultimately apply the technical content found in additional resources.

## 🛫 Project Overview

This project invites you to implement and use a program called `serverfuzzer`
that conducts a fuzzing campaign to automatically determine the security flaw
that can cause the following function to crash and therefore limit server's
availability:

```python
import json

def process_json(json_str: str) -> float:
    """Process a JSON string and return the highest total price among orders."""
    # load the JSON data by coonverting from a string to a dictionary
    data = json.loads(json_str)
    # calculate the total price for each order using the
    # price and quantity of each item in the order
    totals = {
        order["id"]: sum(
            item["quantity"] * item["price"] for item in order["items"]
        )
        for order in data
    }
    # return the highest total price
    return max(totals, key=totals.get)  # type: ignore
```

The specific goal of the fuzzing campaign that `serverfuzzer` undertakes is to
(i) automatically generates random JSON inputs, (ii) input them into the
`process_json` function, (iii) observe the program's behavior, and (iv)
determine whether or not the function crashed. The `serverfuzzer` program will
then report both the total number of the inputs that caused the `process_json`
function to crash out and the total number of inputs that it generated and
subsequently provided to `process_json`. It will also display the "minimal"
input or the smallest possible automatically-generated input that caused the
`process_json` function to crash. Although you are permitted to take manual
testing steps to better understand the defect in the `process_json` function,
you must implement and use a completely automated fuzzing technique in
`serverfuzzer` to conduct the fuzzing campaign.

To learn more about fuzzing and to gather inspiration for your own
implementation of the `serverfuzzer`, please consult the following resources:

- [Atheris: A Coverage-Guided, Native Python Fuzzer](https://github.com/google/atheris)
- [AFL: American Fuzzy Lop, A Security-Oriented Fuzzer](https://github.com/google/AFL)
- [Fuzzing: Breaking Things with Random Inputs](https://www.fuzzingbook.org/html/Fuzzer.html)
- [Property-Based Testing with Hypothesis](https://github.com/HypothesisWorks/hypothesis)

Once you understand more about the importance of server availability and the
ways in which fuzzing techniques can automatically generate inputs that cause a
program to crash &mdash; thereby restricting availability &mdash; make sure
that you consider the following design issues for `serverfuzzer`:

- Although you are not required to do so, your implementation may leverage
existing tools such as `atheris`, `afl`, `fuzzingbook`, or `hypothesis`.
- Your implementation must automatically generate random inputs and cannot,
under any circumstance, always generate the same stream of inputs every time it
is run on either your laptop or in GitHub Actions.
- If the `serverfuzzer` causes the `process_json` function to crash, it must
record the exception stack trace and/or the error message associated with the
crash and the JSON input that lead to the crash.
- The `serverfuzzer` program must display both the total number of inputs that
it generated and subsequently provided to `process_json` and the total number of
inputs that ultimately caused the `process_json` function to crash.
- The `serverfuzzer` program must display the "minimal" input, or the smallest
input that reliably caused the `process_json` function to crash during a
specific run of a fuzzing campaign.
- The `serverfuzzer` program must have a "verbose mode", activated through the
`--verbose` command-line argument, that displays every one of the automatically
generated inputs along with the exception stack trace and/or the error message
associated with the crash and the JSON input that lead to the crash.
- When the `serverfuzzer` program displays a JSON file as part of its output it
must do so in a "pretty" format that makes it easy for a person to read.
- The `serverfuzzer` program must run correctly without error on MacOS, Windows,
and Linux, as confirmed through the execution of the program in GitHub Actions.

Here is an example of the JSON file of an order that `process_json` parses:

```text
{
   'id': '1234567890',
   'items': [
      {'quantity': 31668, 'description': 'product description 1', 'price': 25.99},
      {'quantity': 28467, 'description': 'product description 2', 'price': 42.79},
      {'quantity': 32735, 'description': 'product description 3', 'price': 1000.00}
   ]
},
```

After cloning this repository to your computer, please take the following steps
to get started on the project:

- Make sure that you are using a recent version of Python 3.12 to complete this
assignment by typing `python --version` in your terminal; if you are not using
a recent version of Python please upgrade before proceeding.
- Make sure that you are using a recent version of Poetry 1.8 to complete this
assignment by typing `poetry --version` in your terminal; if you are not using
a recent version of Poetry please upgrade before proceeding.
- Before moving to the next step, you may need to again type `poetry install`
one or more times in order to avoid the appearance of warnings when you next
run the `serverfuzzer` program. Note that you need to provide a complete
implementation of all of the `serverfuzzer` program's features before you can
conduct your own fuzzing campaign to automatically find the defect in
`process_json`.

Finally, here are other issues that you should keep in mind as you work on the
`serverfuzzer` program:

- If you have already installed the
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs the
automated grading checks provided by
[GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
repository's base directory, run the automated grading checks by typing
`gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all of the required responses to the technical
writing prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
labels from all of the provided source code. This means that instead of only
deleting the `TODO` marker from the code you should delete the `TODO` marker
and the entire prompt and then add your own comments to demonstrate that you
understand all of the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
labels from every line of the `writing/reflection.md` file. This means that you
should not simply delete the `TODO` marker but instead delete the entire prompt
so that your reflection is a document that contains polished technical writing
that is suitable for publication on your professional web site.

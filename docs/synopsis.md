# Synopsis: Password Strength Verification System

## Introduction
This project applies Theory of Computation concepts to password validation. It uses Regular Expressions and a Deterministic Finite Automaton (DFA) to determine whether a password belongs to a language defined by a set of structural rules.

## Problem statement
Users may create passwords that fail basic length and character-composition requirements. This project automates validation and reports which conditions pass or fail.

## Objectives
1. Validate password length and required character categories.
2. Implement an independent Regex validator.
3. Implement a DFA-style recognizer.
4. Present the results through a web UI.
5. Test both implementations and compare their decisions.

## Rules
Password length must be 8–16 characters, with at least one uppercase ASCII letter, lowercase ASCII letter, digit, and punctuation character. Only printable ASCII characters other than space are allowed.

## Methodology
Define the accepted alphabet, design the regular expression, represent DFA states with a length counter and category bitmask, implement both validators in Python, integrate with Flask, build a responsive HTML/CSS/JavaScript UI, and verify behavior using automated tests.

## Tools
Python, Flask, Python `re`, HTML, CSS, JavaScript, and `unittest`.

## Expected outcome
A working web application with accept/reject results, per-rule feedback, DFA trace, and a comparison of the two validators.

## Limitations
This checks a structural policy only. It does not provide authentication, password hashing, breach checks, or protection from phishing and guessing attacks.

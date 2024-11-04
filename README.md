# TRGCON24

## Introduction to Exponential Programming [Jose Luis]

[link to presentation]

## Copilot v Cusor [Manu]

### Introduction to the tools

[demo]

### Autocomplete

How does it work and how do they compare?
- code generation
- smart rewrites
- multi-line autocomplete (cursor)
- cursor prediction (cursor)
https://www.cursor.com/features

### Chat

Most common usage:
- asking AI to explain code
- asking for advice on some implementation
- creating documentation from scratch
- creating tests from scratch
- writing code that doesn't require existing code modifications (usually new code working independently from existing code, example: adding a function to read yaml files)

Now that the code edits are available, it makes the chat more useful for:
- implementing functionality that depends on the existing code
- refactoring existing code

### Tips

- Start general then get specific
- Give examples (PS: can add examples in the docstrings)
- Break complex tasks into smaller tasks (PS: can use the Chat to do that)
- Give as much relevant context as possible
- Clean your chat !!!

https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot

### Code reviews

How does it work and how do they compare?

### Additional features

- Git commit generation (Github Copilot)
- Working on pull requests (Github Copilot)

### Limitations:
- the AI doesn't have the global context of the codebase as the developer have
- large codebases have a lot of dependencies that are hard to track for the AI
- passing the full context to the AI is not usually feasible due to token limits

How do both tools work around those limitations?
- @codebase functionality
- cursor composer
- cursor notepads functionality

https://www.reddit.com/r/cursor/comments/1fu02l6/cursor_composer_works_great_for_me_but_it/


## Codeas  [Manu]

[demo]
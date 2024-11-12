## Inline Chat

### Comparison:  

similar / Cursor seems a bit faster / diff UI seems nicer

## Chat

### Managing context in the chat interface:

Copilot: #files / @workspace
Cursor: (+) / @files / @folder / @codebase / @notepad

I. Large context: (copilot = @workspace vs cursor = @codebase / @folder)

Codebase explanation:
- Explain what this project does at high level. Do not reference code as part of your answer. Be concise in your answer
- Tell me about the current project structure
- How do I run this app
- Could you write a markdown documentation explain the project, its structure and how to run it

Searching through the codebase
- Which functions are responsible for executing the LLM calls?

Implementation advice:
- How would you implement a new use case such as translating a codebase to another language? 
- List all of the files I should give the LLM as context in order to generate the code for this new use case

II. Specific context: #files vs @files /@folder / @notepad

Modifying code:
- How could I make this code more readable?
- Would you rename any of the variables or functions to make them more descriptive?

Creating code from scratch:
- Add an option to 

III. Code edits (Composer in Cursor)

Modifying code:
- How could you apply DRY principle to this code?

Adding new functionality:
- Could you create a new use case that translates the given codebase to another programming language? 


IV. Instructions customization

Copilot = .github/copilot-instructions.md
Cursor = .cursorrules


🤖👱🛠️
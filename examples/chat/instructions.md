## Inline Chat

### Comparison:  

similar / Cursor seems a bit faster / diff UI seems nicer

## Chat

### Managing context in the chat interface:

Copilot: #files / @workspace
Cursor: (+) / @files / @folder / @codebase / @notepad

I. @workspace vs @codebase / @folder

Codebase explanation and search:
- Explain what this project does at high level. Do not reference code as part of your answer. Be concise in your answer
- Tell me about the current project structure
- How do I run this app
- Which functions are responsible for executing the LLM calls?

Implementation advice:
- How would you implement a new use case such as translating a codebase to another language? 
- List all of the files I should give the LLM as context in order to generate the code for this new use case

II. #files vs @folder / @files

Modifying code:
- How could I make this code more readable? Break down your suggestions into multiple small changes
- How could you apply DRY principle to this code? Break down your suggestions into multiple small changes
- Would you rename any of the variables or functions? If yes, list all of the changes you would make and why

Creating new code from scratch:
- Could you please implement a new use case such as translating a codebase to another language? 

### Composer

### Additional features

@notepad: context reusability
Editing system prompt in Cursor but not in Copilot (.cursorrules)



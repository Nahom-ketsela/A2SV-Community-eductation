class Solution:
    interpretor = {"G" : "G", "()" : "o", "(al)": "al"}
    def interpret(self, command: str) -> str:
        for key in self.interpretor.keys():
            command = command.replace(key, self.interpretor[key])

        return command

class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        for i in range(len(command)):
            if command[i] == "G" :
                ans.append(command[i])
            elif command[i] == "(" :
                if command[i+1] == ")":
                    ans.append("o")
                    i+=1
                    continue
                else :
                    ans.append("al")
                    i+=3
                    continue
        return "".join(ans)
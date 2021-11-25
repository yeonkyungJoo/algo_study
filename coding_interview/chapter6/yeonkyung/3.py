class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:

        digit_logs = list()
        letter_logs = list()
        for log in logs:
            if log.split()[1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        letter_logs.extend(digit_logs)
        return letter_logs

if __name__ == "__main__":
    print(Solution().reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
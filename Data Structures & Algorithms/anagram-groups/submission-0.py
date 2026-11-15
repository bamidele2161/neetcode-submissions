class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bank = []
        faith = sorted(strs)
        for i in range(len(faith) - 1):
            print(faith[i])
            if sorted(faith[i]) == sorted(faith[i + 1]):
                new = [faith[i], faith[i + 1]]
                print(new, "solution")
                bank.append(new)

        return bank
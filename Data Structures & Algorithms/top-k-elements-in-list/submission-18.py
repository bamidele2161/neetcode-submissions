class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        container = {}
        for i in nums:
            if i in container:
                container[i] += 1
            else:
                container[i] = 1
        sorted_container = dict(sorted(container.items(), key=lambda item: item[1], reverse=True))
        result.sort(reverse=True)
        for i in sorted_container.keys():
            result.append(i)
        return result[:k]
        
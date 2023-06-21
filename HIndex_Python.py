class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = [0] * (len(citations) + 1)

        for num in citations:
            numSum = 0
            if num > len(citations):
                count[len(citations)] += 1
                numSum = count[len(citations)]
            else:
                count[num] += 1
                numSum = sum(count[num: ])
        
        for i in range(len(citations), 0, -1):
            numSum = sum(count[i:])
            if numSum >= i:
                return i

        return 0

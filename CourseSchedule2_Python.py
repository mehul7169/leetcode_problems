class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for x,y in prerequisites:
            adj[y].append(x)
            indegree[x] += 1
        print(adj)
        print(indegree)
        queue = []

        output = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.pop(0)
            output.append(cur)

            for i in adj[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        if len(output) == numCourses: return output
        else: return []
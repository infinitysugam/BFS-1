
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        degree = [0 for i in range(0,numCourses)]
        queue = collections.deque()
        hashmap = {}
        for i in range(0,len(prerequisites)):
            degree[prerequisites[i][1]]+=1

            if prerequisites[i][0] not in hashmap.keys():
                hashmap[prerequisites[i][0]]=[]
            
            hashmap[prerequisites[i][0]].append(prerequisites[i][1])

        for i in range(0,len(degree)):
            if degree[i]==0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            children = hashmap.get(course, [])
            if  children:
                for i in children:
                    degree[i]-=1
                    if degree[i]==0:
                        queue.append(i)

        for i in range(0,len(degree)):
            if degree[i]!=0:
                return False
        return True


        
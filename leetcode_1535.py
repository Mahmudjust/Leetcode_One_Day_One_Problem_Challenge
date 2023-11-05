class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxelement=max(arr)
        queue=deque(arr[1:])
        curr=arr[0]
        winstreak=0
        
        
        while queue:
            opponent=queue.popleft()
            if curr> opponent:
                queue.append(opponent)
                winstreak+=1

            else:
                queue.append(curr)
                curr=opponent
                winstreak=1

            if winstreak==k or curr==maxelement:
                return curr

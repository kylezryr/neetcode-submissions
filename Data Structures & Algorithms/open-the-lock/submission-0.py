class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        queue = deque()
        queue.append(("0000", 0))
        visited = set(deadends)

        def neighbors(lock):
            result = []
            for i in range(4):
                upOne = str((int(lock[i]) + 1) % 10)
                result.append(lock[:i] + upOne + lock[i+1:])
                downOne = str((int(lock[i]) - 1) % 10)
                result.append(lock[:i] + downOne + lock[i+1:])
            return result

        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            for neighbor in neighbors(lock):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, turns + 1))

        return -1
            

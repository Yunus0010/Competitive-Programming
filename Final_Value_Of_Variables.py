class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        count = 0
        for op in operations:
            if op == "X++" or op == "++X":
                count += 1
            elif op == "X--" or op == "--X":
                count -= 1
        return count
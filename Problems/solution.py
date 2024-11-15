class Solution:
    def __init__(self):
        self._solution = "This is the solution class"
    
    def __str__(self):
        return "This is the string representation of the Solution class"
    
    def __repr__(self):
        return "This is the representation of the Solution class"

def main():
    solution = Solution()
    print(solution)
    print(repr(solution))

if __name__ == "__main__":
    main()
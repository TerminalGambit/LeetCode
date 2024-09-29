class AllOne:
    def __init__(self):
        self.dico = {}

    def inc(self, key: str) -> None:
        if key in self.dico:
            self.dico[key] += 1
        else:
            self.dico[key] = 1

    def dec(self, key: str) -> None:
        if key in self.dico:
            if self.dico[key] > 1:
                self.dico[key] -= 1
            else:
                del self.dico[key]

    def getMaxKey(self) -> str:
        if not self.dico:
            return ""
        return max(self.dico, key=self.dico.get)

    def getMinKey(self) -> str:
        if not self.dico:
            return ""
        return min(self.dico, key=self.dico.get)

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
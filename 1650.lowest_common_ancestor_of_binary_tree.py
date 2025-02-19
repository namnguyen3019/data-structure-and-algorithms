class Solution:
    def lowestCommonAncAestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q

        while p1 != p2:
            if p1.parent:
                p1 = p1.parent
            else:
                p1 = q

            if p2.parent:
                p2 = p2.parent
                p2 = p
        return p1

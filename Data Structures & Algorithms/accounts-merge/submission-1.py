class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        parent = {}

        for i in range(len(accounts)):
            for n in range(1, len(accounts[i])):
                email = accounts[i][n]
                name = accounts[i][0]
                email_to_name[email] = name
                if email not in parent:
                    parent[email] = email
        
        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])
            return parent[email]

        
        def union(e1,e2):
            p1,p2 = find(e1),find(e2)

            if p1 == p2:
                return

            parent[p1] = p2

        for account in accounts:
            anchor = account[1]
            for email in account[2:]:
                union(anchor,email)

        groups = {}

        for email in parent:
            root = find(email)
            if root not in groups:
                groups[root] = []
            groups[root].append(email)

        result = []

        for root, emails in groups.items():
            result.append([email_to_name[root]] + sorted(emails))

        return result

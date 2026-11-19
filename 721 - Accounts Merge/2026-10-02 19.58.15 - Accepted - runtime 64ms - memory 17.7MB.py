from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        parent = {}
        rank = {}
        email_to_name = {}

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return

            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a

            if rank[root_a] == rank[root_b]:
                rank[root_a] += 1

        for account in accounts:
            name = account[0]
            first_email = account[1]

            if first_email not in parent:
                parent[first_email] = first_email
                rank[first_email] = 0

            email_to_name[first_email] = name

            for email in account[2:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0

                email_to_name[email] = name
                union(first_email, email)

        groups = defaultdict(list)

        for email in parent:
            groups[find(email)].append(email)

        result = []

        for root, emails in groups.items():
            emails.sort()
            result.append([email_to_name[root]] + emails)

        return result
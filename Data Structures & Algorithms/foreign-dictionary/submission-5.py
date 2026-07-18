class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        result = []
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min(len(word1),len(word2))):
                if word1[j] != word2[j]:
                    if word1[j] not in graph:
                        graph[word1[j]] = []
                    graph[word1[j]].append(word2[j])
                    break

        all_chars = set()
        for word in words:
            all_chars.update(word)

        for char in all_chars:
            if char not in graph:
                graph[char] = []

        in_degree = {char:0 for char in all_chars}

        for char in graph:
            for neighbor in graph[char]:
                in_degree[neighbor] += 1

        #initialize queue with chars that have nothing before them, meaning they are at the front
        queue = deque([char for char in all_chars if in_degree[char] == 0])

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in graph[char]:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) < len(all_chars):
            return ""
        
        return ''.join(result)
        
                        





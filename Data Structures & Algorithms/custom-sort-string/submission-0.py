class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter

 
        freq = Counter(s)
        result = []

    # Add characters according to custom order
        for ch in order:
            if ch in freq:
                result.append(ch * freq[ch])
                del freq[ch]

    # Add remaining characters
        for ch, count in freq.items():
            result.append(ch * count)

        return "".join(result)


        order = "xabfcg"
        s = "bdca"

        print(customSortString(order, s))
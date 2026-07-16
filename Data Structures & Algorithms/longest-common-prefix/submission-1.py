class Solution:
   
    def longestCommonPrefix(self, strs):

        prefix = ""

        first_string = strs[0]

        for i in range(len(first_string)):

            current_char = first_string[i]

            for j in range(1, len(strs)):

                # Check if current string is too short
                if i >= len(strs[j]):
                    return prefix

                # Check if characters are different
                if strs[j][i] != current_char:
                    return prefix

            # If every string matched at this position
            prefix = prefix + current_char

        return prefix
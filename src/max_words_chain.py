"""
This code contains functions to count max chain length
"""


def max_chain_length(word_list):
    """
    counts max chain length
    """
    word_list.sort(key=len)
    dp = {}

    max_length = 1

    for word in word_list:
        dp[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i + 1:]
            if prev in word_list:
                dp[word] = max(dp[word], dp[prev] + 1)
        max_length = max(max_length, dp[word])

    return max_length


def read_input(path_to_infile):
    """
    reads input from file
    """
    with open(path_to_infile, "r", encoding="utf-8") as infile:
        n = int(infile.readline().strip())
        list_of_words = [infile.readline().strip() for _ in range(n)]
    return list_of_words


def write_output(result, path_to_outfile):
    """
    writes result to file
    """
    with open(path_to_outfile, "w", encoding="utf-8") as outfile:
        outfile.write(str(result) + "\n")

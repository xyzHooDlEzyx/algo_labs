def max_chain_length(in_list):
    in_list.sort(key=len)
    dp = {}

    max_length = 1

    for word in in_list:
        dp[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i + 1:]
            if prev in in_list:
                dp[word] = max(dp[word], dp[prev] + 1)
        max_length = max(max_length, dp[word])

    return max_length


def read_input(path_to_infile):
    with open(path_to_infile, "r") as infile:
        n = int(infile.readline().strip())
        list_of_words = [infile.readline().strip() for _ in range(n)]
    return list_of_words


def write_output(result, path_to_outfile):
    with open(path_to_outfile, "w") as outfile:
        outfile.write(str(result) + "\n")

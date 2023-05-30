from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 1:
        return list([1])

    ans = [[1]]
    ans_cnt = 0

    for n in range(2, numRows + 1):
        tmp = [0] + ans[ans_cnt] + [0]

        out = [0] * n
        for i in range(len(tmp) - 1):
            out[i] = tmp[i] + tmp[i + 1]

        ans.append(out)
        ans_cnt += 1

    return ans


if __name__ == "__main__":
    numRows = 5
    print(generate(5))

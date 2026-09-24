class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(numRows - 1):
            # pad row above with 0s at the end
            rowAbove = result[-1]
            padded = [0] + rowAbove + [0]

            newRow = []
            # sum entries in the padded row above
            for j in range(len(rowAbove) + 1):
                newRow.append(padded[j] + padded[j+1])
            
            result.append(newRow)

        return result
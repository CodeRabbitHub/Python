class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If only one row is present we can return the string as it is
        if numRows < 2:
            return s

        # We will create an empty string for each row and then fill each element in each row
        # from row = 0 to row = numRows-1, if we reach bottom (i.e. row = numRows-1)
        # then we move up. Similarly if we reach top, we change direction and move down
        # Finally after filling up all the four rows we join them row0 + row1 +.. numRows

        result = [""] * numRows

        # We start with first row
        row = 0

        for character in s:
            # if we reach top we have to move down
            if row == 0:
                move_down = True
            # if we reach bottom then we have to move up
            elif row == numRows - 1:
                move_down = False

            # Add character to corresponding row
            result[row] += character

            # updating the row increment by 1 if we move down and decrement by 1 if we move up
            row = (row + 1) if move_down else row - 1

        # Finally join all rows and return
        return "".join(result)

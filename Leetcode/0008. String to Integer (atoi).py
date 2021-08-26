class Solution:
    def myAtoi(self, s: str) -> int:

        INTMAX = (2 ** 31) - 1
        INTMIN = -(2 ** 31)

        # Stripping the leading white spaces
        s = s.strip()

        result = 0

        # If string is empty
        if not s:
            return result

        # Getting hold of sign of the number at first place in the string
        if s[0] == "+":
            sign = 1
        elif s[0] == "-":
            sign = -1

        # If sign is present followed by digits then reading that number
        if s[0] == "+" or s[0] == "-":
            i = 1
            while i < len(s) and "0" <= s[i] <= "9":
                result = result * 10 + int(s[i])
                i += 1
            result = sign * result
            # Capping the result obtained
            if result > INTMAX:
                return INTMAX
            elif result < INTMIN:
                return INTMIN
            else:
                return result

        # If the sign is not present and the first element is digit
        elif "0" <= s[0] <= "9":
            i = 0
            while i < len(s) and "0" <= s[i] <= "9":
                result = result * 10 + int(s[i])
                i += 1
            # Capping the result obtained
            if result > INTMAX:
                return INTMAX
            else:
                return result

        # For all other cases
        else:
            return 0

class Codec(object):
    def encode(self, strs):
        encoded_str = ""
        for s in strs:
            encoded_str += "%0*x" % (8, len(s)) + s
        return encoded_str

    def decode(self, s):
        i = 0
        strs = []
        while i < len(s):
            l = int(s[i : i + 8], 16)
            strs.append(s[i + 8 : i + 8 + l])
            i += 8 + l
        return strs

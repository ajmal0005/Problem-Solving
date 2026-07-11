class Solution:
    def isNumber(self, s: str) -> bool:
      if "inf" in s or "Infinity" in s or "nan" == s:
        return False
      try:
        float(s)
        return True
      except:
        return False

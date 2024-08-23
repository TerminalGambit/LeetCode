class Solution:
    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def fractionAddition(self, expression: str) -> str:

        # Parse the expression into a list of fractions
        fractions = []
        i = 0
        while i < len(expression):
            # Find the next fraction
            j = i + 1
            while j < len(expression) and expression[j] != '/':
                j += 1
            numerator = int(expression[i:j])
            i = j + 1
            j += 1
            while j < len(expression) and expression[j] != '+' and expression[j] != '-':
                j += 1
            denominator = int(expression[i:j])
            fractions.append((numerator, denominator))
            i = j

        # Calculate the sum of the fractions
        numerator_sum = 0
        denominator_lcm = 1
        for numerator, denominator in fractions:
            # Calculate the least common multiple of the denominators
            denominator_gcd = self.gcd(denominator_lcm, denominator)
            denominator_lcm = denominator_lcm // denominator_gcd * denominator

            # Add the numerator to the sum
            numerator_sum += numerator * (denominator_lcm // denominator)

        # Calculate the greatest common divisor of the numerator and denominator
        numerator_gcd = self.gcd(abs(numerator_sum), denominator_lcm)

        # Return the simplified fraction
        return f'{numerator_sum // numerator_gcd}/{denominator_lcm // numerator_gcd}'

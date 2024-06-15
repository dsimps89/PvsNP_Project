#Non-trivial greatest common divisor




# Example usage



if __name__ == '__main__':
    def has_non_trivial_gcd(nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                gcd_value = gcd(nums[i], nums[j])
                if gcd_value > 1:
                    return True
        return False
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    numbers = [12, 18, 24, 36]
    has_non_trivial = has_non_trivial_gcd(numbers)
    print("Has non-trivial GCD:", has_non_trivial)

def test():
    print("Testing p_vs_np.database_problems.non_trivial_greatest_common_divisor...")
    main()
    print("p_vs_np.database_problems.non_trivial_greatest_common_divisor passed.")


if __name__ == '__main__':
    main()

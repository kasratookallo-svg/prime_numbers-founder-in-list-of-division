# Prime_devisions_founder Program
# Made by Kasra Tookallo in 2025
def is_prime(n):
    """بررسی اول بودن عدد"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def prime_divisors_count(n):
    """تعداد مقسوم‌علیه‌های اول عدد n"""
    divisors = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            if is_prime(i):
                divisors.add(i)
            if is_prime(n // i):
                divisors.add(n // i)
        i += 1
    # اگر خود عدد اول باشد هم اضافه شود
    if is_prime(n):
        divisors.add(n)
    return len(divisors)

def main():
    numbers = []
    for _ in range(10):
        num = int(input())
        numbers.append(num)

    best_num = None
    best_count = -1

    for num in numbers:
        count = prime_divisors_count(num)
        if count > best_count or (count == best_count and num > best_num):
            best_num = num
            best_count = count

    print(best_num, best_count)

if __name__ == "__main__":
    main()

"""
برنامه‌ای بنویسید که 10 عدد از ورودی بخواند و در انتها عددی که بیشترین تعداد مقسوم‌علیه عدد اول را دارد به همراه تعداد مقسوم‌علیه‌های اول آن، در خروجی چاپ کند. اگر چند عدد این حالت را داشتند، بزرگترین آن‌ها را چاپ کند.



ورودی نمونه:

123
43
54
12
76
84
98
678
543
231
خروجی نمونه:

678 3
"""
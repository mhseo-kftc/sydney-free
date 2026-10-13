"""간단한 구구단 프로그램.

사용법:
    python gugudan.py        # 2단부터 9단까지 전체 출력
    python gugudan.py 7      # 7단만 출력
"""
import sys


def print_dan(dan):
    print(f"=== {dan}단 ===")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
    print()


def main():
    if len(sys.argv) > 1:
        try:
            dan = int(sys.argv[1])
        except ValueError:
            print("숫자를 입력해주세요. 예: python gugudan.py 7")
            sys.exit(1)
        print_dan(dan)
    else:
        for dan in range(2, 10):
            print_dan(dan)


if __name__ == "__main__":
    main()

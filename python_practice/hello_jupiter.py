# print("Hello World");
# print("Hello jupiter");
# x = 4 + 945
# print(x)
import sys

sys.stdout.buffer.write(b"What your name?\n")
sys.stdout.flush()
name = sys.stdin.buffer.readline().rstrip()
print(f"I'm {name.decode()}! \nNice to meet you.")

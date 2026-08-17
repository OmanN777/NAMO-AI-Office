def Print(y):
    if not isinstance(y, int) or y < 1:
        print("Error: y must be >= 1")
        return
    for r in range(y):
        row = []
        for c in range(y):
            if c == 0 or c == y - 1 or c == r:
                row.append("X")
            else:
                row.append("O")
        print("  ".join(row))
if __name__ == "__main__":
    try:
        user_input = input("Input a Number : ").strip()
        if user_input:
            y_val = int(user_input)
            print(f"Output for y={y_val}")
            Print(y_val)
    except ValueError:
        print("Invalid input!")

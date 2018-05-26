
def remove_borders(parts):
    first = parts[0]
    last = parts[-1]
    if not first or "0" in first:
        parts.pop(0)
    if not last or "0" in last:
        parts.pop()
    return parts


def solution(N):
    binary_representation = f"{bin(N)}".replace("0b", "")
    print(f"binary_representation: {binary_representation}")

    binary_split = binary_representation.split("1")
    remove_borders(binary_split)

    if binary_split:
        binary_representation = max(binary_split)
        result = len(binary_representation)
    else:
        result = 0

    print(f"result: {result}")
    return result

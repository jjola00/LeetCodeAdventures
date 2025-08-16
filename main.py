
from binary_search.find_peak_element import find_peak_element

def main():
    array = [1, 4, 6, 2, 12, 17, 21, 31, 65, 72, 92932]
    idx = find_peak_element(array)
    print(f"Peak index: {idx}, value: {array[idx] if idx is not None else None}")

if __name__ == "__main__":
    main()

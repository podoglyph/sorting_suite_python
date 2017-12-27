import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', nargs='+', type=int, help='a list to sort', required=True)
args = parser.parse_args()

for _, unsorted in args._get_kwargs():
    if unsorted is not None:
        print("Unsorted list:", unsorted)

def bubbleSort(unsorted):
    for n in range(len(unsorted)-1, 0, -1):
        for i in range(n):
            if unsorted[i] > unsorted[i + 1]:
                p_temp = unsorted[i]
                unsorted[i] = unsorted[i + 1]
                unsorted[i + 1] = p_temp
    sorted = unsorted
    print("Bubble Sorted list:", sorted)

bubbleSort(unsorted)
import cProfile
from main import FenTree


with cProfile.Profile() as prof:
    fentree = FenTree()

    #construct
    for i in range(2000):
        arr = []
        for n in range(45):
            arr.append(n)
        fentree.construct(arr)

    #sum
    for f in range(45):
        for s in range(45):
            fentree.range_sum(f, s)

prof.print_stats()

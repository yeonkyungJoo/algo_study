def func(v):
    if v > 7:
        return

    func(v * 2)
    func(v * 2 + 1)
    print(v, end=' ')

func(1)

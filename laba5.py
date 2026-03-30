def r_s(arr, ind, rr):
    if ind == len(arr):
        return rr
    rr1 = arr[ind] + rr
    return r_s(arr, ind + 1, rr1)


def rm_s(arr, ind, rr):
    if ind == len(arr):
        return rr
    if arr[ind] < rr:
        rr = arr[ind]
    return rm_s(arr, ind + 1, rr)


def rma_s(arr, ind, rr):
    if ind == len(arr):
        return rr
    if arr[ind] > rr:
        rr = arr[ind]
    return rma_s(arr, ind + 1, rr)


arr1 = [1, 2, 3, 4, 56]
res1 = r_s(arr1, 0, 0)
res2 = rm_s(arr1, 0, arr1[0])
res3 = rma_s(arr1, 0, arr1[0])
print(res1, res2, res3)


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    _  """
    m1 = 0
    n1 = 0
    i = 0
    while m1 < m+n:
        print("-------------",i, "-----------")
        print("nums1: ", nums1)
        print("nums2: ", nums2)
        if n == 0:
            break
        elif m1 >= m:
            nums1[m1] = nums2[n1]
            n1 += 1
            m1 += 1
        elif nums1[m1] <= nums2[n1]:
            m1 += 1
        elif nums1[m1] > nums2[n1]:
            print("swapped")
            nums1[m1],nums2[n1] = nums2[n1],nums1[m1]
            m1 += 1
        i += 1
        
    print(nums1)

nums1 = [1,2,3,0,0,0]
# nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [1,2,3]
# nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
# 2, 3, 4, 5, 5, 6
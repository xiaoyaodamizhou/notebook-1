# 插入排序:
# 插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中
# 从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序
# 时间复杂度为O(n^2)
# c = [5, 2, 3, 7, 5, 4, 10]
def insert_sort(lists):
    for i in range(1, len(lists)):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j = (j - 1)
    return lists


# 希尔排序
# 希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，
# 是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法。
# 该方法因DL．Shell于1959年提出而得名。 希尔排序是把记录按下标的一定增量分组，
# 对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，
# 当增量减至1时，整个文件恰被分成一组，算法便终止。
# 思路点拨：
# 第一次将一组数组一分为二，并保证打一组的对应元素小于第二组的对应元素，
# 对应关系为（i + length/2）(0 < i <length/2)
# 第二次区第一组中的的某个元素按顺序逐一进行插入排序(首先key元素以前的元素都将小于key，后面的都将大于key)
def shell_sort(lists):
    length = len(lists)
    step = 2
    group = length / step
    while group > 0:
        group = int(group)
        for i in range(0, group):
            j = i + group
            while j < length:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k+group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists

# c = [5, 2, 3, 7, 5, 4, 10]
# a = shell_sort(c)
# print(a)

# 冒泡排序：
# 每一次循环可以保证将一个最大的数放置末尾（一次至少能排一个）
# 它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
# 走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


# 快速排序:

# 描述
# 选定一个数为参照值（先是前面的）
# 前提此时的范围内的左上限 < 此时的范围内的右上限：（其实一直都是再给key调位置）
# 缩小范围找到第一个右边小于参照值的数，交换（此时的范围内的左右上限做下标对应的数值进行交换）
# 缩小范围找到第一个左边大于参照值的数，交换（此时的范围内的左右上限做下标对应的数值进行交换）
# 实现了在该指定的范围类在key之前的数都比key小，在key之后的数都比key大
# 直至left = right 完成了第一次quick_sort，此时left=right=key值对应处在数组中的位置

# 递归一：quick_sort(lists, low, left-1)，递归直到left = right = low(原理是left-1)
# 递归二：quick_sort(lists, left+1, high)，递归直到left = right = high(原理是right+1)
# 其实该方法的意思就是每次给一个人定位置，最后把所有人的位置都定完

def quick_sort(lists, left, right):
    if left > right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    # print(lists)
    # print(left, right, "|")
    quick_sort(lists, low, left-1)
    # print(lists)
    quick_sort(lists, left+1, high)
    # print(lists)
    return lists


# 直接选择排序
#
# 基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；第2趟，
# 在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，
# 将它与r[i]交换，使有序序列不断增长直到全部排序完毕。

def select_sort(lists):
    for i in range(0, len(lists)):
        for j in range(i, len(lists)):
            if lists[j] <= lists[i]:
                swap = lists[j]
                lists[j] = lists[i]
                lists[i] = swap
    return lists

# 堆排序
#
# 堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，
# 它是选择排序的一种。可以利用数组的特点快速定位指定索引的元素。堆分为大根堆和小根堆，是完全二叉树
# 。大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。在数组的非降序排序中，
# 需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。


def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)

#
# 归并排序
#
#
# 归并排序是建立在归并操作上的一种有效的排序算法,
# 该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
# 将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
# 若将两个有序表合并成一个有序表，称为二路归并。
#
# 归并过程为：比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，
# 并令i和k分别加上1；否则将第二个有序表中的元素a[j]复制到r[k]中，并令j和k分别加上1，
# 如此循环下去，直到其中一个有序表取完，
# 然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。
# 归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，
# 接着把左边子区间排序，再把右边子区间排序，
# 最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)

# 基数排序
#
# 描述
#
# 基数排序（radix sort）属于“分配式排序”（distribution sort），
# 又称“桶子法”（bucket sort）或bin sort，顾名思义，它是透过键值的部份资讯，
# 将要排序的元素分配至某些“桶”中，藉以达到排序的作用，基数排序法是属于稳定性的排序，
# 其时间复杂度为O (nlog(r)m)，其中r为所采取的基数，而m为堆数，
# 在某些时候，基数排序法的效率高于其它的稳定性排序法。


import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists


# 触发器
'''

'''




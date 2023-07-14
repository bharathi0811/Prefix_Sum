class PrefixSum:
    @staticmethod
    def prefix_sum(array):
        l = []
        l.append(array[0])
        n = len(array)
        for i in range(1, n):
            l.append(l[i - 1] + array[i])
        return l
array= list(map(int,input("Enter the array element: ").split()))
obj=PrefixSum()
print(obj.prefix_sum(array))

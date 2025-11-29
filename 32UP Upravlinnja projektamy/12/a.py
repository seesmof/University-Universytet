def get_median(array: list) -> int:
    pos=len(array)
    return array[pos//2] if pos%2==0 else array[pos//2-1]+array[pos//2]

given='1,1,0.75,1,1,0,0,0'
array=given.split(',')
sorted_array=sorted(array)
median=get_median(array=sorted_array)
print(f'{sorted_array = }')
print(f'{median = }')
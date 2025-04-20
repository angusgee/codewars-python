# Complete the solution. It should try to retrieve the value of the array at the index provided. If the index is out of the array's max bounds then it should return the default value instead. 

def solution(items: list[str], index: int, default_value: str) -> str:
    try:
        return items[index]
    except IndexError:
        return default_value

data = ['a', 'b', 'c']
print(solution(data, 1, 'd')) # should == 'b'
print(solution(data, 5, 'd')) # should == 'd'

# negative values work as long as they aren't out of the length bounds
print(solution(data, -1, 'd')) # should == 'c'
print(solution(data, -5, 'd')) # should == 'd'

def pythagorean_traingle(arr:list)->bool:
    if len(arr)==3:
        arr.sort()
        return arr[2]**2==arr[0]**2+arr[1]**2
    else:
        return False



if __name__=="__main__":
    print(pythagorean_traingle([5, 3, 4])) 
    print(pythagorean_traingle([6, 8, 10])) 
    print(pythagorean_traingle([100, 3, 65])) 
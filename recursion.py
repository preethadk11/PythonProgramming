def func(num):
    if num==0:
        return
    
    func(num-1)
    print(num)
func(5)
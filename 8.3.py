result = []
def divider(a, b):
    try:
        c =0
        a,b = int(a), int(b)
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        c= a/b
    except ValueError:
        print("число",a ,"менше за ",b)
    except IndexError:
        print("число менше за 100")
    except:
        print("Невірний тип даних")

    return  c
data = {10: 2, 2: 5, "123": 4, 18: 0, 10: 15, 8 : 4}
for key in data:
 res = divider(key, data[key])
 result.append(res)

print(result)
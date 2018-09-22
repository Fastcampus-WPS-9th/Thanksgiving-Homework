# 랭킹 출력
def print_rank():
    before_rank = read_rank()
    print("{:=^40}".format(""))
    print("{:=^40}".format(" RANKING "))
    for i, item in enumerate(before_rank, start=1):
        print(f"{i}위 {item[0]}님 최고강화: {item[1]}, 최대 돈: {item[2]}")
    print("{:=^40}\n".format("")*2)

# 랭킹 읽기
def read_rank():
    before_rank = []
    try:
        with open('./save_data/record.txt', 'rt') as f:
            while True:
                line = f.readline()
                if not line: break
                ranking = line.split(', ')
                # Delete \n
                ranking[2] = ranking[2][:-1]
                before_rank.append(tuple(ranking))
    except FileNotFoundError as e:
        pass
    finally:
        return before_rank
    
# 랭킹 쓰기
def write_rank(user):
    before_rank = read_rank()
    my_rank = (user.name, str(user.max_enchant), str(user.max_money))
    before_rank.append(my_rank)
    after_rank = sorted(before_rank, key=lambda x: int(x[1]), reverse=True)

    try:
        with open('./save_data/record.txt', 'wt') as f:
            for i in after_rank[:5]:
                string = ", ".join(i)+"\n"
                f.write(string)
    except Exception as ex:
        print(ex)

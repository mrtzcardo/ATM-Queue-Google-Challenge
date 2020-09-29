def input_values():
    cases = 1
    info_dic = {}
    T = int(input())
    while cases <= T:
        first_line = input()
        queue_max = list(map(int, first_line.split()))
        second_line = input()
        withdraw_amounts = list(map(int, second_line.split()))
        info_dic.update({cases: {"queue_max": queue_max, "withdraw_amounts": withdraw_amounts}})
        cases += 1
    return info_dic


def populate_queue(N):
    queue = []
    i = 1
    while i <= N:
        queue.append(i)
        i += 1
    return queue


def withdraw(queue_list, atm_limit):
    final_order = []

    while True:
        person = queue_list.pop(0)
        if person[1] <= atm_limit:
            final_order.append(person[0])
            if len(queue_list) == 0:
                break
        else:
            queue_list.append([person[0], person[1] - atm_limit])

    return final_order


def process_dic(info_dic):
    count = 1
    for i in info_dic:
        N, X = info_dic[i]["queue_max"]
        queue = populate_queue(N)
        atm_limit = X

        queue_list = []
        for amount in queue:
            queue_list.append([amount, info_dic[i]["withdraw_amounts"][amount - 1]])

        print("Case #{}:".format(count), withdraw(queue_list, atm_limit))
        i += 1
        count += 1


def main():
    info_dic = input_values()
    process_dic(info_dic)


if __name__ == "__main__":
    main()

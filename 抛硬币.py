import random
import os
while True:
    def toss_coin(num_tosses):
        heads = 0
        tails = 0
    
        for _ in range(num_tosses):
            # 通过随机选择0或1来模拟硬币正反面
            result = random.randint(0, 1)
        
            if result == 0:
                heads += 1
            else:
                tails += 1
    
        return heads, tails

# 获取用户输入的扔硬币次数
    while True:
        print("随机扔硬币结果生成器（用于数学23章概率学习）")
        print("版本号:1.0.0.0")
        num_tosses = int(input("请输入扔硬币的次数（小于一百万）："))
        if num_tosses > 0 and num_tosses < 1000000:
            break
        else:
            print("请输入一个介于1和999999之间的数字。")
            os.system('pause')
            os.system('cls')


# 调用函数模拟扔硬币
    heads_count, tails_count = toss_coin(num_tosses)

# 计算正反面的概率
    heads_probability = heads_count / num_tosses
    tails_probability = tails_count / num_tosses

# 输出结果
    print("正面次数：", heads_count)
    print("反面次数：", tails_count)
    print("正面概率：", heads_probability)
    print("反面概率：", tails_probability)
    os.system('pause')
    os.system('cls')
#!/usr/bin/env Python3
r1 = 0.0175
r2 = 0.0225
r3 = 0.0275
r5 = 0.0325
# 一次性存5年
income1 = 1000 * r5 * 5
print("一次性存5年的利息收益为：", income1)
# 先存2年，到期后将本息再存3年
income2_1 = 1000 * r2 * 2
income2_2 = (income2_1 + 1000) * r3 * 3
print("先存2年，到期后将本息再存3年的利息收益为：", income2_2)
# 先存3年，到期后将本息再存2年
income3_1 = 1000 * r3 * 3
income3_2 = (income3_1 + 1000) * r2 * 2
print("先存3年，到期后将本息再存2年的利息收益为：", income3_2)
# 存1年，到期后将本息继续存，连续存5年
income4_1 = 1000 * r1 * 1
income4_2 = (income4_1 + 1000) * r1 * 1
income4_3 = (income4_1 + income4_2 + 1000) * r1 * 1
income4_4 = (income4_1 + income4_2 + income4_3 + 1000) * r1 * 1
income4_5 = (income4_1 + income4_2 + income4_3 + income4_4 + 1000) * r1 * 1
print("存1年，到期后将本息继续存，连续存5年的利息收益为：", income4_5)
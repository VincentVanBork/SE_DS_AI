
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from population import Population

df = pd.read_excel("GA_task.xlsx", engine="openpyxl")
df = df.rename(columns={"R":"R.0", "T":"T.0"})
# print(df.columns)
# resources = df[df.columns[::2]]
df[df.columns[1::2]] = df[df.columns[1::2]].cumsum()
# print(times["T.0"])

print(df.columns)
# fig,ax = plt.subplots()
# ax.bar(resources["R.0"],times["T.0"])
# plt.show()

p = Population(df)
for i in range(10):
    p.mutate_generation()
    p.next_generation()
    p.repopulate_generation()
    
    print("after mutation", p.best.current_time_value)
# for i in p.best:
#     print(i.genes.start_time)

print("MAX", p.best.current_time_value)
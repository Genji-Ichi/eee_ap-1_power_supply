import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["font.family"] = "IPAexGothic"  # 漢字フォント導入
plt.rcParams["mathtext.fontset"] = "cm"  # 数式フォント導入
plt.rcParams["xtick.direction"] = "in"  # x軸の目盛りの向き
plt.rcParams["ytick.direction"] = "in"  # y軸の目盛りの向き
plt.rcParams["xtick.major.width"] = 1.0  # x軸主目盛りの太さ
plt.rcParams["ytick.major.width"] = 1.0  # y軸主目盛りの太さ
plt.rcParams["font.size"] = 12  # フォントサイズ
plt.rcParams["axes.linewidth"] = 1.0  # 軸の太さ

fig = plt.figure()
ax = fig.add_subplot(111)

text_V = r"$V\,/\mathrm{V}$"
text_I = r"$I\,/\mathrm{A}$"
ax.set_xlabel(text_V)
ax.set_ylabel(text_I)


file_path_60 = "data/1_2.csv"
dataset_60 = pd.read_csv(file_path_60, comment="#")
V_60 = np.array(dataset_60["V"])
I_60 = np.array(dataset_60["I"])

file_path_120 = "data/1_3.csv"
dataset_120 = pd.read_csv(file_path_120, comment="#")
V_120 = np.array(dataset_120["V"])
I_120 = np.array(dataset_120["I"])

file_path_105 = "data/1_4.csv"
dataset_105 = pd.read_csv(file_path_105, comment="#")
V_105 = np.array(dataset_105["V"])
I_105 = np.array(dataset_105["I"])


ax.plot(
    V_60,
    I_60,
    linestyle="none",
    marker="o",
    label=r"$x=60\,\mathrm{cm}$",
)
ax.plot(
    V_105,
    I_105,
    linestyle="none",
    marker="o",
    label=r"$x=105\,\mathrm{cm}$",
)
ax.plot(
    V_120,
    I_120,
    linestyle="none",
    marker="o",
    label=r"$x=120\,\mathrm{cm}$",
)

ax.grid()
ax.legend()


plt.show()

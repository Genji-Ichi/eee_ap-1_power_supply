import os

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

# csv ファイルの読み込み
file_path = "figures/data/4_90cm_-5.csv"
dataset = pd.read_csv(file_path, comment="#")

x = np.array(dataset["Vin"])
y = np.array(dataset["Iin"])


text_x = r"入力電圧 $V_\mathrm{in}\,/\mathrm{V}$"
text_y = r"入力電流 $I_\mathrm{in}\,/\mathrm{A}$"
ax.set_xlabel(text_x)
ax.set_ylabel(text_y)

ax.plot(
    x,
    y,
    linestyle="none",
    marker="o",
    label=r"$\mathrm{AC}=85.5\,\mathrm{cm}$",
)

ax.grid()
# ax.legend()

file_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig(f"figures/{file_name}.pdf", bbox_inches="tight")

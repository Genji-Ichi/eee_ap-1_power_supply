import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import ScalarFormatter

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
file_path = "figures/data/1_1.csv"
dataset = pd.read_csv(file_path, comment="#")

distance = np.array(dataset["d"]) - 4.5
illuminance = np.array(dataset["E"])

text_d = r"間隔 $d\,/\mathrm{cm}$"
text_E = r"照度 $E\,/\mathrm{lx}$"
ax.set_xlabel(text_d)
ax.set_ylabel(text_E)

ax.plot(distance, illuminance, linestyle="none", marker="o", label="実験結果")

ax.grid()

ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

file_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig(f"figures/{file_name}.pdf", bbox_inches="tight")

plt.show()

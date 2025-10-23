import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

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
file_path = "figures/data/add_comp_0R2.csv"
dataset = pd.read_csv(file_path, comment="#")

x_0R2 = np.array(dataset["V_in"])
y_0R2 = np.array(dataset["D"])

text_x = r"加算器回路への入力電圧 $V_\mathrm{in}\,/\mathrm{V}$"
text_y = r"デューティ比 $D$"
ax.set_xlabel(text_x)
ax.set_ylabel(text_y)
ax.plot(
    -x_0R2,
    y_0R2,
    linestyle="none",
    marker="o",
    label=r"$K_\mathrm{fb}=-0.2$",
    color="blue",
)


file_path = "figures/data/add_comp_0R51.csv"
dataset = pd.read_csv(file_path, comment="#")
x_0R51 = np.array(dataset["V_in"])
y_0R51 = np.array(dataset["D"])
ax.plot(
    -x_0R51,
    y_0R51,
    linestyle="none",
    marker="o",
    label=r"$K_\mathrm{fb}=-0.51$",
    color="red",
)


file_path = "figures/data/add_comp_0R71.csv"
dataset = pd.read_csv(file_path, comment="#")
x_0R71 = np.array(dataset["V_in"])
y_0R71 = np.array(dataset["D"])
ax.plot(
    -x_0R71,
    y_0R71,
    linestyle="none",
    marker="o",
    label=r"$K_\mathrm{fb}=-0.71$",
    color="green",
)


V_pp = 13
V_ref = 8.03
x_thm = np.arange(-16.5, -3.5, 0.1)


def _y_0R2(x):
    return 1 / 2 - (-0.2) / V_pp * (V_ref + x)


def _y_0R51(x):
    return 1 / 2 - (-0.51) / V_pp * (V_ref + x)


def _y_0R71(x):
    return 1 / 2 - (-0.71) / V_pp * (V_ref + x)


ax.plot(x_thm, _y_0R2(x_thm), label=r"$K_\mathrm{fb}=0.2$", color=("blue", 0.75))
ax.plot(x_thm, _y_0R51(x_thm), label=r"$K_\mathrm{fb}=0.51$", color=("red", 0.75))
ax.plot(x_thm, _y_0R71(x_thm), label=r"$K_\mathrm{fb}=0.71$", color=("green", 0.75))


ax.grid()
ax.set_xlim(-16.5, -3.5)
ax.set_ylim(bottom=0)

custom_lines = [
    Line2D(
        [0],
        [0],
        color="blue",  # 線の色
        linestyle="-",  # 線の種類
        marker="o",  # マーカーの種類
        markerfacecolor="blue",  # マーカーの塗りつぶし色
        markeredgecolor="blue",  # マーカーの縁の色
        # markersize=7,  # マーカーのサイズ
        label=r"$K_\mathrm{fb}=-0.2$",
    ),
    Line2D(
        [0],
        [0],
        color="red",  # 線の色
        linestyle="-",  # 線の種類
        marker="o",  # マーカーの種類
        markerfacecolor="red",  # マーカーの塗りつぶし色
        markeredgecolor="red",  # マーカーの縁の色
        # markersize=7,  # マーカーのサイズ
        label=r"$K_\mathrm{fb}=-0.51$",
    ),
    Line2D(
        [0],
        [0],
        color="green",  # 線の色
        linestyle="-",  # 線の種類
        marker="o",  # マーカーの種類
        markerfacecolor="green",  # マーカーの塗りつぶし色
        markeredgecolor="green",  # マーカーの縁の色
        # markersize=7,  # マーカーのサイズ
        label=r"$K_\mathrm{fb}=-0.71$",
    ),
]
ax.legend(handles=custom_lines)

file_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig(f"figures/{file_name}.pdf", bbox_inches="tight")

fig = plt.figure()
ax = fig.add_subplot(111)

delta_0R2 = (y_0R2 - _y_0R2(-x_0R2)) / _y_0R2(-x_0R2)
print(y_0R2)
print(_y_0R2(-x_0R2))

delta_0R51 = (y_0R51 - _y_0R51(-x_0R51)) / _y_0R51(-x_0R51)

delta_0R71 = (y_0R71 - _y_0R71(-x_0R71)) / _y_0R71(-x_0R71)

ax.plot(-x_0R2, delta_0R2, linestyle="none", marker="o", color="blue")
ax.plot(-x_0R51, delta_0R51, linestyle="none", marker="o", color="red")
ax.plot(-x_0R71, delta_0R71, linestyle="none", marker="o", color="green")
text_x = r"加算器回路への入力電圧 $V_\mathrm{in}\,/\mathrm{V}$"
text_y = r""
ax.set_xlabel(text_x)
ax.set_ylabel(text_y)
ax.set_ylim(bottom=0)
ax.grid()

plt.show()

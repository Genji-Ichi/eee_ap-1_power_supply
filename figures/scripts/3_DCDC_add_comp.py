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
file_path = "figures/data/DCDC_add_comp_0R2.csv"
dataset = pd.read_csv(file_path, comment="#")

x = np.array(dataset["V_in"])
y = np.array(dataset["V_out"])

text_x = r"DCDCコンバータへの入力電圧 $V_\mathrm{in}\,/\mathrm{V}$"
text_y = r"DCDCコンバータからの出力電圧 $V_\mathrm{out}\,/\mathrm{V}$"
ax.set_xlabel(text_x)
ax.set_ylabel(text_y)
ax.plot(
    x, -y, linestyle="none", marker="o", label=r"$K_\mathrm{fb}=-0.2$", color="blue"
)


file_path = "figures/data/DCDC_add_comp_0R51.csv"
dataset = pd.read_csv(file_path, comment="#")
x = np.array(dataset["V_in"])
y = np.array(dataset["V_out"])
ax.plot(
    x, -y, linestyle="none", marker="o", label=r"$K_\mathrm{fb}=-0.51$", color="red"
)


V_pp = 13
V_ref = 8.03
x_range = np.arange(1.5, 16.5, 0.1)
y_range = np.arange(-13.5, -2.25, 0.1)
# x_range = np.arange(-10, 10, 0.1)
# y_range = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x_range, y_range)

K_fb = -0.2
Z = Y * (V_pp + 2 * K_fb * (V_ref + Y)) / (V_pp - 2 * K_fb * (V_ref + Y)) + X
plt.contour(X, Y, Z, [0], colors="blue", alpha=0.75)

K_fb = -0.51
Z = Y * (V_pp + 2 * K_fb * (V_ref + Y)) / (V_pp - 2 * K_fb * (V_ref + Y)) + X
plt.contour(X, Y, Z, [0], colors="red", alpha=0.75)

ax.grid()
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
]
ax.legend(handles=custom_lines)

file_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig(f"figures/{file_name}.pdf", bbox_inches="tight")


# plt.show()

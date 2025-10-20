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
file_path = "figures/data/2_60p.csv"
dataset = pd.read_csv(file_path, comment="#")

x = np.array(dataset["P_i"])
y = np.array(dataset["P_o"])

p_fit = np.polyfit(x, y, 1)
m, b = p_fit

# フィッティング直線を描画するための x 座標を生成 (データの最小値から最大値まで)
x_fit = np.linspace(x.min(), x.max(), 100)

# フィッティング直線上の y 座標を計算 (y = mx + b)
y_fit = m * x_fit + b

# フィッティング結果のラベルを生成
# {:.2e} は指数表記で有効数字2桁
label_fit = rf"直線回帰: $P_\mathrm{{o}} = ({m:.2e}) P_\mathrm{{i}} + ({b:.2e})$"

text_x = r"入力電力$P_\mathrm{i}\,/\mathrm{W}$"
text_y = r"出力電力$P_\mathrm{o}\,/\mathrm{W}$"
ax.set_xlabel(text_x)
ax.set_ylabel(text_y)


ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

ax.plot(x, y, linestyle="none", marker="o", label="実験結果")
ax.plot(
    x_fit,
    y_fit,
    linestyle="-",  # 実線で描画
    color="tab:red",  # 赤色で強調
    label=label_fit,  # フィッティング式を凡例に表示
    linewidth=1.5,
)
ax.grid()
ax.legend()

file_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig(f"figures/{file_name}.pdf", bbox_inches="tight")

# plt.show()

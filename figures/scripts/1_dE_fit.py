import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import ScalarFormatter
from scipy.optimize import curve_fit

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

# csv ファイルの読み込み（変更なし）
file_path = "figures/data/1_1.csv"
dataset = pd.read_csv(file_path, comment="#")

distance = np.array(dataset["d"]) - 4.5
illuminance = np.array(dataset["E"])

text_d = r"間隔 $d\,/\mathrm{cm}$"
text_E = r"照度 $E\,/\/\mathrm{lx}$"
ax.set_xlabel(text_d)
ax.set_ylabel(text_E)

ax.plot(distance, illuminance, linestyle="none", marker="o", label="実験結果")

# --- フィッティング処理の修正 ---

# 1. フィッティング関数の定義の修正
# E = A / (a*x**2 + b*x + c)。分子Aは定数パラメータ。
def fit_func(x, A, a, b, c): # パラメータAを新たに追加
    """フィッティング関数 $E = A / (ax^2 + bx + c)$"""
    denominator = a * x**2 + b * x + c
    return A / denominator

# 2. curve_fitの実行
# パラメータは(A, a, b, c)の4つ。初期値も4つ設定する。
# Aの初期値は E * x^2 のオーダー (例: 3e3 * 60^2 ≈ 1e7) を目安とする。
try:
    # A, a, b, c の初期値
    p0_initial = [1e7, 1e-6, 1e-4, 1e-2]

    popt, pcov = curve_fit(fit_func, distance, illuminance, p0=p0_initial)
    A_opt, a_opt, b_opt, c_opt = popt # パラメータのアンパック順序を変更

    # 3. フィッティング結果のプロット
    x_fit = np.linspace(distance.min(), distance.max(), 100)
    y_fit = fit_func(x_fit, A_opt, a_opt, b_opt, c_opt)

    # ★ 凡例のラベルを修正し、分子を定数Aとして表示 ★
    label_fit = (
        r"フィッティング:" + "\n" +
        r"$E = \frac{A}{" +
        f"{a_opt:.2e}x^2 + {b_opt:.2e}x + {c_opt:.2e}" + r"}$" + "\n" +
        r"($A \approx " + f"{A_opt:.2e}" + "$)" # Aの値を表示
    )

    ax.plot(x_fit, y_fit, color="red", linestyle="-", label=label_fit)

    ax.legend(fontsize=10)

except RuntimeError:
    print("Error: フィッティングに失敗しました。初期値 (p0) を見直してください。")
# -----------------------------

ax.grid()

ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

file_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig(f"figures/{file_name}.pdf", bbox_inches="tight")

plt.show()
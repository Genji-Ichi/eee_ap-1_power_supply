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

text_V = r"$V\,/\mathrm{V}$"
text_I = r"$I\,/\mathrm{A}$"
ax.set_xlabel(text_V)
ax.set_ylabel(text_I)


file_path_60 = "figures/data/1_2.csv"
dataset_60 = pd.read_csv(file_path_60, comment="#")
V_60 = np.array(dataset_60["V"])
I_60 = np.array(dataset_60["I"])

file_path_120 = "figures/data/1_3.csv"
dataset_120 = pd.read_csv(file_path_120, comment="#")
V_120 = np.array(dataset_120["V"])
I_120 = np.array(dataset_120["I"])

file_path_105 = "figures/data/1_4.csv"
dataset_105 = pd.read_csv(file_path_105, comment="#")
V_105 = np.array(dataset_105["V"])
I_105 = np.array(dataset_105["I"])


# --- OB=105cm (V_105, I_105) のフィッティング処理を追加 ---

# V_105 と I_105 をDataFrameに結合し、Vでソート
# この処理により、データが昇順に並べ替えられます
df_105 = (
    pd.DataFrame({"V": V_105, "I": I_105}).sort_values(by="V").reset_index(drop=True)
)

# 1. 小さい方から4点でのフィッティング (Low V)
V_low = df_105["V"].iloc[:4]
I_low = df_105["I"].iloc[:4]
p_low = np.polyfit(V_low, I_low, 1)  # [slope, intercept]
V_fit_low = np.linspace(V_low.min(), V_low.max(), 100)
I_fit_low = np.poly1d(p_low)(V_fit_low)

# 2. 大きい方から4点でのフィッティング (High V)
V_high = df_105["V"].iloc[-4:]
I_high = df_105["I"].iloc[-4:]
p_high = np.polyfit(V_high, I_high, 1)  # [slope, intercept]
V_fit_high = np.linspace(V_high.min(), V_high.max(), 100)
I_fit_high = np.poly1d(p_high)(V_fit_high)

# --- 既存のプロット処理の後ろに追加するフィッティングラインのプロット ---
# 既存の ax.plot(...) の後ろに続けて以下のコードを追加してください。

# 既存の OB=105cm のプロット色を取得 (今回は3番目にプロットされている色)
# V_60 (0番目), V_105 (1番目), V_120 (2番目) の順番でプロットされているため、インデックスは 1 です。
# ただし、確実な色取得のため、元のコードの V_105 プロット部分を以下のように修正・分割することを推奨します。

# **********【推奨される修正】**********
# 既存のプロット部分を以下のように変更すると、色の取得が確実になります。
# --------------------------------------------------------------------------------
# # 既存のV_105プロットの行を以下に置き換える:
# plot_105 = ax.plot(
#     V_105,
#     I_105,
#     linestyle="none",
#     marker="o",
#     label=r"$\mathrm{OB}=105\,\mathrm{cm}$",
# )
# color_105 = plot_105[0].get_color() # プロット色を取得

# # V_120 のプロットはそのまま続ける:
# ax.plot(
#     V_120,
#     I_120,
#     linestyle="none",
#     marker="o",
#     label=r"$\mathrm{OB}=120\,\mathrm{cm}$",
# )
# --------------------------------------------------------------------------------
ax.plot(
    V_60,
    I_60,
    linestyle="none",
    marker="o",
    label=r"$\mathrm{OB}=60\,\mathrm{cm}$",
)
plot_105 = ax.plot(
    V_105,
    I_105,
    linestyle="none",
    marker="o",
    label=r"$\mathrm{OB}=105\,\mathrm{cm}$",
)
ax.plot(
    V_120,
    I_120,
    linestyle="none",
    marker="o",
    label=r"$\mathrm{OB}=120\,\mathrm{cm}$",
)
color_105 = plot_105[0].get_color()
# ****************************************

# 既存コードを変更しないため、ここでは強引に3番目のラインの色を取得（不安定な方法であることに注意）
# 実行する際には、上記の【推奨される修正】を適用してください。
try:
    # 既存の ax.lines はまだ存在しないため、ここでは仮に色を変数で保持します。
    # 実際には、 ax.plot(...) の後にこの部分を記述してください。
    pass
except IndexError:
    # 既存のプロットの色を取得できない場合は、デフォルトの 'green' を使用
    color_105 = "tab:green"


# --- 新しいフィッティング線のプロット ---

# Low V フィッティング (V_105と color_105 を使用)
label_low = f"$\mathrm{{OB}}=105\,\mathrm{{cm}}$ $I={p_low[0]:.2e}V+{p_low[1]:.2e}$"
ax.plot(
    V_fit_low,
    I_fit_low,
    linestyle="-",  # 実線
    color=color_105,
    linewidth=1.5,
    label=label_low,
    zorder=0,
)

# High V フィッティング (V_105と color_105 を使用)
label_high = f"$\mathrm{{OB}}=105\,\mathrm{{cm}}$ $I={p_high[0]:.2e}V+{p_high[1]:.2e}$"
ax.plot(
    V_fit_high,
    I_fit_high,
    linestyle="--",  # 破線
    color=color_105,
    linewidth=1.5,
    label=label_high,
    zorder=0,
)


ax.grid()
ax.legend()

file_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig(f"figures/{file_name}.pdf", bbox_inches="tight")

# plt.show()

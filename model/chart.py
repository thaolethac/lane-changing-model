import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Các tham số đầu vào
v_TL_range = np.linspace(10, 30, 50)  # Khoảng tốc độ của v_TL (m/s)
v_M_range = np.linspace(0, 20, 50)    # Khoảng tốc độ của v_M (m/s)
a_M_range = np.arange(2, 3.2, 0.2)    # Khoảng của a_M từ 2 đến 3 với bước nhảy 0.2

# Các tham số cố định
t0 = 15
c_v = 0.05
c_a = 0.3
w = 3.5
theta = np.deg2rad(3)  # Chuyển đổi 3 độ sang radian
a_TL_values = [-1, 0, 1]  # Các giá trị khác nhau của a_TL như trong hình ảnh

# Chuẩn bị hình vẽ
fig, axes = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})
fig.suptitle("Khoảng cách chấp nhận được khi chuyển làn giữa phương tiện M và TL")

for idx, a_TL in enumerate(a_TL_values):
    ax = axes[idx]
    
    # Tạo lưới cho v_TL và v_M, nhưng hoán đổi trục x và y
    v_M, v_TL = np.meshgrid(v_M_range, v_TL_range)
    
    # Vòng lặp qua từng giá trị a_M
    for a_M in a_M_range:
        # Tính G_min cho từng giá trị a_M và a_TL
        G_min = (t0 - c_v * (v_TL - v_M) - c_a * (a_TL - a_M)) * v_M

        # Tính G_a^M-TL cho từng giá trị a_M
        G_a_M_TL = -((v_TL - v_M)**2 / (2 * (a_M - a_TL))) + G_min + w * np.sin(theta)
        
        # Vẽ mặt phẳng
        ax.plot_surface(v_M, v_TL, G_a_M_TL, alpha=0.5, rstride=1, cstride=1, cmap='viridis')
    
    # Đặt nhãn và tiêu đề
    ax.set_xlabel("vM (m/s)")
    ax.set_ylabel("vTL (m/s)")
    ax.set_zlabel("Ga (m)")
    ax.set_title(f"aTL = {a_TL} m/s²")
    ax.view_init(elev=10, azim=-150)

plt.show()

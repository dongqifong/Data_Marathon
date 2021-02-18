
##建立好環境(python=3.8)
##安裝numpy(conda install numpy)
##直接裝basemap(conda install -c anaconda basemap)，不要先安裝matplotlib
##會自動把欠的安裝上去
##conda install -c conda-forge basemap-data-hires
##conda install -c conda-forge cartopy
import os
os.system('clear')
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
map = Basemap()
#Basemap有很多屬性，這里全都使用默認参數
# 畫圖
map.drawcoastlines()

# 顯示结果
plt.show()
import mpl_toolkits.basemap
print(mpl_toolkits.basemap.supported_projections)
# 更改投影方式
map = Basemap(projection = 'ortho', lat_0 = 0, lon_0 = 0)
#’ortho’指正射投影，後面两個参數是设置中心點

# 给整個地圖上藍色
map.drawmapboundary(fill_color = 'aqua')

# 给陸地塗上珊瑚色，湖泊塗上藍色
map.fillcontinents(color = 'coral', lake_color = 'aqua')

# 畫圖
map.drawcoastlines()

# 顯示结果
plt.show()
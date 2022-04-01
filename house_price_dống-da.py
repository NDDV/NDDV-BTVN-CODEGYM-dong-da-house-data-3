#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# %%
df = pd.read_excel('house_price_dống-da.xlsx')
df = df.dropna()
df.info()
#%%
df

# %%
#Vẽ biểu đồ xu hướng phân tích mối quan hệ giữa giá nhà với diện tích, giá nhà với số lượng phòng ngủ, nhận xét.
area_df = df[["area",'price']]
area_df
# %%
sns.lmplot(x="area", y="price",data = area_df)
print("Giá nhà tăng theo diện tích")
# %%
bedroom_df = df[["bedroom",'price']]
bedroom_df
#%%
sns.lmplot(x="bedroom", y="price",data = bedroom_df)
print("Giá nhà không tăng theo số lượng phòng ngủ")

# %%
#Vẽ biểu đồ phân bố thể hiện phân bố của giá nhà theo các hướng, nhận xét.
balcony_direction_df = df[["balcony_direction",'price']]
sns.violinplot(x = "balcony_direction",y='price', data=balcony_direction_df)
print("Giá nhà hướng đông-nam được giá nhất so với tấ cả các hướng còn lại")
# %%
#Vẽ biểu đồ tần số để đếm số nhà ở mỗi hướng nhà, nhận xét.
sns.countplot(x = "balcony_direction", data = df)
print("Giá nhà hướng đông-nam được giá nhất so với tấ cả các hướng còn lại")
# %%
#Vẽ biểu đồ boxplot thể hiện phân bố của giá nhà theo các hướng, nhận xét.
balcony_direction_df = df[["balcony_direction",'price']]
sns.boxplot(x=balcony_direction_df["price"])
print("Giá cả giao động ổn định")
# %%

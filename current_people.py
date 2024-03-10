import pandas as pd

# v1.0→v1.1

source_path = 'processed_data_v1.0.csv'
destination_path = 'current_people.csv'
encoding_methods = 'GB2312'

# 读取源表数据
source_data = pd.read_csv(source_path, encoding=encoding_methods)

# 去除上行28站点的行
source_data.drop(index=source_data[(source_data['方向'] == 0) & (source_data['站点序号'] == 28)].index, inplace=True)

# 按班次和站点进行分组，并计算每个站点车上的总人数
source_data['current_people'] = source_data.groupby('班次')['客流量'].cumsum()  # cumsum()方法：累计求和

# 保存结果到文件
source_data.to_csv(destination_path, index=False, encoding=encoding_methods)

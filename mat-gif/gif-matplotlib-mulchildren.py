# matplotlib多子图动态可视化

# 读取数据
df = pd.read_csv('weather_hourly_darksky.csv')
df = df.rename(columns={"time": "date"})

@gif.frame
def plot(df, date):
    df = df.loc[df.index[0]:pd.Timestamp(date)]

    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(10, 6), dpi=100)

    ax1.plot(df.temperature, marker='o', linestyle='--', linewidth=1, markersize=3, color='g')
    maxi = round(df.temperature.max() + 3)
    ax1.set_xlim([START, END])
    ax1.set_ylim([0, maxi])
    ax1.set_ylabel('TEMPERATURE', color='green')

    ax2.plot(df.windSpeed, marker='o', linestyle='--', linewidth=1, markersize=3, color='b')
    maxi = round(df.windSpeed.max() + 3)
    ax2.set_xlim([START, END])
    ax2.set_ylim([0, maxi])
    ax2.set_ylabel('WIND', color='blue')

    ax3.plot(df.visibility, marker='o', linestyle='--', linewidth=1, markersize=3, color='r')
    maxi = round(df.visibility.max() + 3)
    ax3.set_xlim([START, END])
    ax3.set_ylim([0, maxi])
    ax3.set_ylabel('VISIBILITY', color='red')

frames = []
for date in pd.date_range(start=df.index[0], end=df.index[-1], freq='1M'):
    frame = plot(df, date)
    frames.append(frame)

gif.save(frames, "文件名称.gif", duration=0.5, unit='s')


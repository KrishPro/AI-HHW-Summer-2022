[Github Codebase](https://github.com/KrishPro/AI-HHW-Summer-2022)


```python
import matplotlib.pyplot as plt
import json

with open('Data/detailed.json') as file:
    data = json.load(file)
```


```python
def is_float(f):
    try:
        float(f)
        return True
    except:
        return False

print("Hourly Quantities:\n")
hourly_quantities = [k for k, i in data['data']['weather'][0]['hourly'][0].items() if is_float(i)]
print(hourly_quantities)
print('\n---\n')
print("Daily Quantities:\n")
transposed_data = {k: [float(day[k]) for day in  data['data']['weather']] for k, i in data['data']['weather'][0].items() if is_float(i)}
print(list(transposed_data.keys()))
```

    Hourly Quantities:
    
    ['time', 'tempC', 'tempF', 'windspeedMiles', 'windspeedKmph', 'winddirDegree', 'weatherCode', 'precipMM', 'precipInches', 'humidity', 'visibility', 'visibilityMiles', 'pressure', 'pressureInches', 'cloudcover', 'HeatIndexC', 'HeatIndexF', 'DewPointC', 'DewPointF', 'WindChillC', 'WindChillF', 'WindGustMiles', 'WindGustKmph', 'FeelsLikeC', 'FeelsLikeF', 'uvIndex']
    
    ---
    
    Daily Quantities:
    
    ['maxtempC', 'maxtempF', 'mintempC', 'mintempF', 'avgtempC', 'avgtempF', 'totalSnow_cm', 'sunHour', 'uvIndex']



```python
def plot_hourly(quantity_name: str, nrows=3, ncols=5, figsize=(25, 15)):
    qs = list()
    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    fig.suptitle(quantity_name.title(), fontsize=50)
    
    for i, (ax, day) in enumerate(zip(axes.flatten(), data['data']['weather'])):
        
        quantity = [float(h[quantity_name]) for h in day['hourly']]
        time = [int(h['time'])//100  for h in day['hourly']]
        
        ax.plot(time, quantity)
        ax.set_title(f"Day {i}")
        
        qs.append(quantity)
        
    average_quantity = list(map(lambda quantity: sum(quantity)/len(quantity), list(zip(*qs))))
    all_time_quantity = [q for quantity in qs for q in quantity]
    
    plt.figure(figsize=(figsize[0], 7))
    plt.title("A Average Day")
    plt.plot(time, average_quantity)
    plt.show()

    plt.figure(figsize=(figsize[0], 7))
    plt.title("All 15 Days joint *vertically")
    plt.plot(all_time_quantity)
    plt.show()
```


```python
for quantity_name in hourly_quantities:
    plot_hourly(quantity_name)
    print('\n---\n')
```


    
![png](Assets/output_3_0.png)
    



    
![png](Assets/output_3_1.png)
    



    
![png](Assets/output_3_2.png)
    


    
    ---
    



    
![png](Assets/output_3_4.png)
    



    
![png](Assets/output_3_5.png)
    



    
![png](Assets/output_3_6.png)
    


    
    ---
    



    
![png](Assets/output_3_8.png)
    



    
![png](Assets/output_3_9.png)
    



    
![png](Assets/output_3_10.png)
    


    
    ---
    



    
![png](Assets/output_3_12.png)
    



    
![png](Assets/output_3_13.png)
    



    
![png](Assets/output_3_14.png)
    


    
    ---
    



    
![png](Assets/output_3_16.png)
    



    
![png](Assets/output_3_17.png)
    



    
![png](Assets/output_3_18.png)
    


    
    ---
    



    
![png](Assets/output_3_20.png)
    



    
![png](Assets/output_3_21.png)
    



    
![png](Assets/output_3_22.png)
    


    
    ---
    



    
![png](Assets/output_3_24.png)
    



    
![png](Assets/output_3_25.png)
    



    
![png](Assets/output_3_26.png)
    


    
    ---
    



    
![png](Assets/output_3_28.png)
    



    
![png](Assets/output_3_29.png)
    



    
![png](Assets/output_3_30.png)
    


    
    ---
    



    
![png](Assets/output_3_32.png)
    



    
![png](Assets/output_3_33.png)
    



    
![png](Assets/output_3_34.png)
    


    
    ---
    



    
![png](Assets/output_3_36.png)
    



    
![png](Assets/output_3_37.png)
    



    
![png](Assets/output_3_38.png)
    


    
    ---
    



    
![png](Assets/output_3_40.png)
    



    
![png](Assets/output_3_41.png)
    



    
![png](Assets/output_3_42.png)
    


    
    ---
    



    
![png](Assets/output_3_44.png)
    



    
![png](Assets/output_3_45.png)
    



    
![png](Assets/output_3_46.png)
    


    
    ---
    



    
![png](Assets/output_3_48.png)
    



    
![png](Assets/output_3_49.png)
    



    
![png](Assets/output_3_50.png)
    


    
    ---
    



    
![png](Assets/output_3_52.png)
    



    
![png](Assets/output_3_53.png)
    



    
![png](Assets/output_3_54.png)
    


    
    ---
    



    
![png](Assets/output_3_56.png)
    



    
![png](Assets/output_3_57.png)
    



    
![png](Assets/output_3_58.png)
    


    
    ---
    



    
![png](Assets/output_3_60.png)
    



    
![png](Assets/output_3_61.png)
    



    
![png](Assets/output_3_62.png)
    


    
    ---
    



    
![png](Assets/output_3_64.png)
    



    
![png](Assets/output_3_65.png)
    



    
![png](Assets/output_3_66.png)
    


    
    ---
    



    
![png](Assets/output_3_68.png)
    



    
![png](Assets/output_3_69.png)
    



    
![png](Assets/output_3_70.png)
    


    
    ---
    



    
![png](Assets/output_3_72.png)
    



    
![png](Assets/output_3_73.png)
    



    
![png](Assets/output_3_74.png)
    


    
    ---
    



    
![png](Assets/output_3_76.png)
    



    
![png](Assets/output_3_77.png)
    



    
![png](Assets/output_3_78.png)
    


    
    ---
    



    
![png](Assets/output_3_80.png)
    



    
![png](Assets/output_3_81.png)
    



    
![png](Assets/output_3_82.png)
    


    
    ---
    



    
![png](Assets/output_3_84.png)
    



    
![png](Assets/output_3_85.png)
    



    
![png](Assets/output_3_86.png)
    


    
    ---
    



    
![png](Assets/output_3_88.png)
    



    
![png](Assets/output_3_89.png)
    



    
![png](Assets/output_3_90.png)
    


    
    ---
    



    
![png](Assets/output_3_92.png)
    



    
![png](Assets/output_3_93.png)
    



    
![png](Assets/output_3_94.png)
    


    
    ---
    



    
![png](Assets/output_3_96.png)
    



    
![png](Assets/output_3_97.png)
    



    
![png](Assets/output_3_98.png)
    


    
    ---
    



    
![png](Assets/output_3_100.png)
    



    
![png](Assets/output_3_101.png)
    



    
![png](Assets/output_3_102.png)
    


    
    ---
    



```python
plt.figure(figsize=(15, 7))
plt.fill_between(range(15), transposed_data['maxtempC'], transposed_data['mintempC'], alpha=0.3)
plt.plot(transposed_data['maxtempC'], color='#1f77b4', label='max temperature')
plt.plot(transposed_data['avgtempC'], color='#0e3651', label='avg temperature')
plt.plot(transposed_data['mintempC'], color='#1f77a4', label='min temperature')
plt.title("Temperature Plot")
plt.xlabel('Days (#)')
plt.ylabel('Temperature (°C)')
plt.show()

print("The upper and lower boundaries indicate maximum and minimum temperature reached")
print("The darker line in mid indicates average temperature")
```


    
![png](Assets/output_4_0.png)
    


    The upper and lower boundaries indicate maximum and minimum temperature reached
    The darker line in mid indicates average temperature



```python
plt.figure(figsize=(15, 7))
plt.title("Snowfall")
plt.ylabel("Snowfall")
plt.xlabel("Days (#)")
plt.plot(transposed_data['totalSnow_cm'])
plt.show()
print("We can see there is no snowfall at all")
```


    
![png](Assets/output_5_0.png)
    


    We can see there is no snowfall at all



```python
plt.figure(figsize=(15, 7))
plt.plot(transposed_data['sunHour'])
plt.title('Sun Hour')
plt.xlabel('Days (#)')
plt.ylabel('Sun Hours (hr)')
plt.show()

print("We can see sun hours are in upward trend")
```


    
![png](Assets/output_6_0.png)
    


    We can see sun hours are in upward trend


![image.png](Assets/uv-index.png)


```python
plt.figure(figsize=(15, 4))
plt.title("UV Index")
plt.ylabel('UV Index')
plt.xlabel('Days (#)')
plt.plot(transposed_data['uvIndex'])
plt.show()
print('UV Index is very high')
```


    
![png](Assets/output_8_0.png)
    


    UV Index is very high


# Thank You 🙏

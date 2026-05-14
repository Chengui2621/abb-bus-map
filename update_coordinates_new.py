import json
import csv

# 读取新的CSV坐标文件
coordinates = {}
with open('站点坐标结果_智能.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        stop_name = row['站点名称'].strip()
        coord_str = row['坐标'].strip().strip('"')
        try:
            lng, lat = coord_str.split(',')
            coordinates[stop_name] = {
                'lng': float(lng.strip()),
                'lat': float(lat.strip())
            }
        except:
            print(f"无法解析坐标: {stop_name} -> {coord_str}")

print(f"从CSV读取了 {len(coordinates)} 个站点坐标")

# 读取routes_data.json
with open('routes_data.json', 'r', encoding='utf-8') as f:
    routes_data = json.load(f)

# 更新坐标
updated_count = 0
not_found = []

for route in routes_data:
    for stop in route['stops']:
        stop_name = stop['name'].strip()
        if stop_name in coordinates:
            stop['lng'] = coordinates[stop_name]['lng']
            stop['lat'] = coordinates[stop_name]['lat']
            updated_count += 1
        else:
            not_found.append(f"{route['name']} - {stop_name}")

# 保存更新后的数据
with open('routes_data.json', 'w', encoding='utf-8') as f:
    json.dump(routes_data, f, ensure_ascii=False, indent=2)

print(f"\n✅ 更新了 {updated_count} 个站点的坐标")
print(f"\n未找到坐标的站点: {len(not_found)} 个")
if not_found:
    print("\n前10个未找到的站点:")
    for item in not_found[:10]:
        print(f"  - {item}")

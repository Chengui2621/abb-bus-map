import json
import re

# ABB HUB的准确坐标
ABB_HUB_LNG = 118.22
ABB_HUB_LAT = 24.65

# 读取routes_data.json
with open('routes_data.json', 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式查找所有ABB HUB/HUB/hub站点并更新坐标
# 匹配模式："name": "ABB HUB" 或 "ABB Hub" 后面的坐标
pattern = r'("name":\s*"ABB\s*[Hh][Uu][Bb]",\s*"time":\s*"[^"]*",\s*"location":\s*"[^"]*",\s*"lng":\s*)[\d.]+(,\s*"lat":\s*)[\d.]+'
replacement = r'\g<1>' + str(ABB_HUB_LNG) + r'\g<2>' + str(ABB_HUB_LAT)

updated_content = re.sub(pattern, replacement, content)

# 保存更新后的数据
with open('routes_data.json', 'w', encoding='utf-8') as f:
    f.write(updated_content)

# 统计更新的数量
original_count = len(re.findall(pattern, content))
print(f"✅ 已更新所有ABB HUB的坐标为: {ABB_HUB_LNG}, {ABB_HUB_LAT}")
print(f"共更新了 {original_count} 个ABB HUB站点")

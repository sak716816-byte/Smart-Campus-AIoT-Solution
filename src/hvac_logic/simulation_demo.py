import time
import random

def simulate_classroom_environment():
    # 模拟初始状态
    co2_level = 450  # 正常室外水平
    temp = 24.5      # 初始舒适温度
    ac_status = "ECO模式"
    fan_speed = "关闭"

    print("="*50)
    print("智慧教学楼 AIoT 暖通联动系统 - 逻辑模拟运行中")
    print("="*50)
    print(f"初始状态: 温度 {temp}°C | CO2 {co2_level}ppm | 新风: {fan_speed}")
    print("-" * 50)

    try:
        # 模拟一节课从开始到结束的过程
        for minute in range(1, 11):
            print(f"\n[第 {minute*5} 分钟运行监测]")
            
            # 模拟人多，CO2 快速上升
            co2_level += random.randint(150, 250)
            # 模拟呼吸产热，温度微升
            temp += round(random.uniform(0.1, 0.3), 1)

            print(f">>> 实时感知数据: 温度 {temp}°C | CO2 {co2_level}ppm")

            if co2_level > 1000:
                print("【系统预警】二氧化碳浓度超标！已达疲劳阈值。")
                print("【联动动作】1. 开启高阶新风换气模式...")
                fan_speed = "HIGH"
                
                print("【前馈补偿】2. 检测到新风热负荷，空调启动 -1.0°C 补偿...")
                temp_target = temp - 1.0
                ac_status = f"补偿制冷中 (目标:{temp_target}°C)"
            else:
                print("【状态正常】环境指标在舒适区间内。")

            print(f"当前执行状态: 新风[{fan_speed}] | 空调[{ac_status}]")
            time.sleep(2)  # 演示时缩短时间步长

    except KeyboardInterrupt:
        print("\n模拟停止。")

if __name__ == "__main__":
    simulate_classroom_environment()


import pandas as pd
import json

def analyze_students(csv_file):
    # 读取 CSV
    df = pd.read_csv(csv_file)

    # 统计总人数
    total_students = len(df)

    # 各国家人数统计
    country_counts = df['country'].value_counts().to_dict()

    # 对赌完成率
    completed = (df['bet_status'] == 'completed').sum()
    completion_rate = completed / total_students

    # 结果字典
    report = {
        "total_students": total_students,
        "country_counts": country_counts,
        "completion_rate": round(completion_rate, 2)
    }

    # 保存为 JSON
    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("分析完成！结果已保存到 report.json")
    return report


if __name__ == "__main__":
    analyze_students("students.csv")

import csv
from datetime import datetime



def save_report(data_list, file_prefix="diagnostic_report"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_file = f"{file_prefix}_{timestamp}.csv"
    md_file = f"{file_prefix}_{timestamp}.md"

    # 保存 CSV 报表
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Step", "Request (Hex)", "Response (Hex)"])
        for item in data_list:
            writer.writerow(item)

    # 保存 Markdown 报表
    with open(md_file, "w", encoding='utf-8') as file:
        file.write(f"# Diagnostic Report ({timestamp})\n\n")
        for idx, (step, req, resp) in enumerate(data_list, 1):
            file.write(f"## Step {idx}: {step}\n")
            file.write(f"- Request: `{req}`\n")
            file.write(f"- Response: `{resp}`\n\n")

    print(f"[INFO] Saved report to {csv_file}, {md_file}")

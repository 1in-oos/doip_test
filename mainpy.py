from doip_client import DoIPClient
from report_utils import save_report
import time

doip = DoIPClient("192.168.0.10")  # 改成你 ECU 的 IP
doip.connect()

results = []

resp1 = doip.routing_activation(0x0E00)
results.append(("Routing Activation", "02 00 00 0E", resp1.hex()))

resp2 = doip.uds_request(b"\x10\x03")
results.append(("Session Control", "10 03", resp2.hex()))

resp3 = doip.uds_request(b"\x22\xF1\x90")
results.append(("Read VIN", "22 F1 90", resp3.hex()))

resp4 = doip.uds_request(b"\x14\xFF\xFF")
results.append(("Clear DTC", "14 FF FF", resp4.hex()))

doip.disconnect()

# 保存报表
save_report(results)

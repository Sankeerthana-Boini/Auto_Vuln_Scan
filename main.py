import os
from scanner.zap_scanner import scan_target
from scanner.parser import parse_alerts
from reports.pdf_generator import generate_pdf

def main():
    try:
        target = "http://testphp.vulnweb.com"  # ✅ Replace with your actual target
        print(f"Starting vulnerability scan on: {target}")

        alerts = scan_target(target)
        if not alerts:
            print("No alerts found or scan failed.")
            return

        parsed_alerts = parse_alerts(alerts)

        # Ensure the 'reports' directory exists
        os.makedirs("reports", exist_ok=True)

        generate_pdf(parsed_alerts, output_path="reports\\report.pdf")
        print("✅ Scan complete. Report saved to 'reports\\report.pdf'")
    
    except Exception as e:
        print(f"❌ Error occurred during scan: {e}")

if __name__ == '__main__':
    main()

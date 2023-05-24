from ioc_framework.ioc import IP, Domain
from ioc_framework.framework import IOCFramework


def main():
    framework = IOCFramework()

    ip = IP("91.203.193.91")
    domain = Domain("anydeskupdates.com")

    platform = input("Select platform (1: VirusTotal, 2: UrlScan, 3: AbuseIPDB): ")

    if platform == "1":
        # VirusTotal için endpoint'i ayarla
        ip.endpoint = "https://www.virustotal.com/api/v3/ip_addresses/"
        framework.add_ioc(ip)
        framework.query_all()
        framework.print_results_all()

        domain.endpoint = "https://www.virustotal.com/api/v3/domains/"
        framework.add_ioc(domain)
        framework.query_all()
        framework.print_results_all()

    elif platform == "2":
        # UrlScan için endpoint'i ayarla
        ip.endpoint = "https://urlscan.io/api/v1/search/?q=ip:"
        domain.endpoint = "https://urlscan.io/api/v1/search/?q=domain:"
    elif platform == "3":
        # AbuseIPDB için endpoint'i ayarla
        ip.endpoint = "https://abuseipdb.com/api/v2/check?ipAddress="
        domain.endpoint = "https://abuseipdb.com/api/v2/check-domain?domain="
    else:
        print("Invalid platform selection.")


if __name__ == "__main__":
    main()

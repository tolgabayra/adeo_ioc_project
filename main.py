from ioc_framework.ioc import IP, Domain
from ioc_framework.framework import IOCFramework


def main():
    framework = IOCFramework()

    ip = IP("91.203.193.91")
    domain = Domain("anydeskupdates.com")
    print("Welcome the ioc project.")

    platform = input("Select platform (1: VirusTotal, 2: UrlScan, 3: AbuseIPDB): ")

    if platform == "1":
        ip.endpoint = "https://www.virustotal.com/api/v3/ip_addresses/"
        framework.add_ioc(ip)
        print("Loading...")
        framework.query_all()
        framework.print_results_all()

        domain.endpoint = "https://www.virustotal.com/api/v3/domains/"
        framework.add_ioc(domain)
        print("Loading...")
        framework.query_all()
        framework.print_results_all()

        save_results = input(
            "Do you want to save and write the results to a file? (y/n): "
        )
        if save_results.lower() == "y":
            framework.write_results()
            print("Successfull. By by :D")
        else:
            print("By by")

    elif platform == "2":
        ip.endpoint = "https://urlscan.io/api/v1/search/?q=ip:"
        framework.add_ioc(ip)
        framework.query_all()
        framework.print_results_all()

        domain.endpoint = "https://urlscan.io/api/v1/search/?q=domain:"
        framework.add_ioc(domain)
        framework.query_all()
        framework.print_results_all()

        save_results = input(
            "Do you want to save and write the results to a file? (y/n): "
        )
        if save_results.lower() == "y":
            framework.write_results()
            print("Sucessfull. By by :D")
        else:
            print("By by")
    elif platform == "3":
        ip.endpoint = "https://abuseipdb.com/api/v2/check?ipAddress="
        domain.endpoint = "https://abuseipdb.com/api/v2/check-domain?domain="
    else:
        print("Invalid platform selection.")


if __name__ == "__main__":
    main()

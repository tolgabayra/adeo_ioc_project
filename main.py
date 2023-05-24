from ioc_framework.ioc import IP, Domain, SHA256
from ioc_framework.framework import IOCFramework


def main():
    framework = IOCFramework()

    ip = IP("91.203.193.91")
    domain = Domain("anydeskupdates.com")
    sha256 = SHA256("ed01ebfbc9eb5bbea545af4d01bf5f1071661840480439c6e5babe8e080e41aa")

    framework.add_ioc(ip)
    # framework.add_ioc(domain)
    # framework.add_ioc(sha256)

    framework.query_all()
    framework.print_results_all()


if __name__ == "__main__":
    main()

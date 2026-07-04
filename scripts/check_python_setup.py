import importlib.util
import platform
import sys


MIN_VERSION = (3, 10)

PACKAGES = {
    "pandas": "pandas",
    "numpy": "numpy",
    "scikit-learn": "sklearn",
    "matplotlib": "matplotlib",
    "ipykernel": "ipykernel",
    "pytest": "pytest",
}


def check_python_version():
    current = sys.version_info[:3]
    ok = current >= MIN_VERSION
    version_text = ".".join(str(part) for part in current)
    required_text = ".".join(str(part) for part in MIN_VERSION)
    status = "PASS" if ok else "FAIL"
    print(f"{status}: Python {version_text} detected; Python {required_text}+ required")
    return ok


def check_package(package_name, import_name):
    ok = importlib.util.find_spec(import_name) is not None
    status = "PASS" if ok else "MISSING"
    print(f"{status}: {package_name}")
    return ok


def main():
    print("ANL559 local Python setup check")
    print("-" * 36)
    print(f"Executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    print("-" * 36)

    checks = [check_python_version()]
    for package_name, import_name in PACKAGES.items():
        checks.append(check_package(package_name, import_name))

    print("-" * 36)
    if all(checks):
        print("Setup check passed. You are ready for the local Python labs.")
        return 0

    print("Setup check incomplete.")
    print("Run this from the course folder after activating your virtual environment:")
    print("python -m pip install -r requirements.txt")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

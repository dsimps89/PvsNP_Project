import importlib
import pkgutil

def run_module(module_name):
    print(f"Running tests for {module_name}...")
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, 'test'):
            print(f"Testing {module_name}...")
            module.test()
        else:
            print(f"No test function found in {module_name}, skipping...")
    except Exception as e:
        print(f"Failed to run tests in {module_name} due to {e}.")

def discover_and_run_tests(package):
    package = importlib.import_module(package)
    for importer, modname, ispkg in pkgutil.walk_packages(package.__path__):
        full_modname = package.__name__ + '.' + modname
        if modname != '__init__':  # Skip __init__ files
            run_module(full_modname)

if __name__ == '__main__':
    discover_and_run_tests('p_vs_np')

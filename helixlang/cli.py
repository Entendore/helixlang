import argparse
import sys
from .interpreter import HelixLangInterpreter

def main():
    p = argparse.ArgumentParser(prog="helixlang", description="HelixLang Biophysical DSL CLI")
    p.add_argument("script", help="Path to the .hl script to execute")
    args = p.parse_args()

    try:
        with open(args.script, "r") as f:
            source = f.read()
        ir = HelixLangInterpreter()
        ir.execute(source)
    except FileNotFoundError:
        print(f"Error: Script {args.script} not found.", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()

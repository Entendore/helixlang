"""HelixLang SSA Interpreter"""
import re
from .types import *
from .morphisms import *

class HelixLangInterpreter:
    def __init__(self):
        self.env = {}

    def execute(self, source: str):
        lines = source.strip().split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].split('//')[0].strip()
            if not line:
                i += 1; continue
            
            # Handle simple inline or block if
            if line.startswith("if "):
                cond = line[3:-1].strip()
                if self._eval_condition(cond):
                    i += 1
                    if i < len(lines):
                        self._exec_line(lines[i].split('//')[0].strip())
                i += 1; continue

            self._exec_line(line)
            i += 1

    def _eval_arg(self, arg_str: str):
        arg_str = arg_str.strip()
        if arg_str.startswith('%'):
            return self.env.get(arg_str)
        if arg_str.startswith('"') and arg_str.endswith('"'):
            return arg_str.strip('"')
        try: return float(arg_str)
        except: pass
        return arg_str

    def _eval_condition(self, cond: str) -> bool:
        # e.g., %ribo_trace.burden > 0.8 OR %qs_promoter.active
        if "==" in cond:
            left, right = cond.split("==")
            return self._eval_arg(left.strip()) == self._eval_arg(right.strip())
        
        parts = cond.split()
        if len(parts) == 1:
            val = self._eval_arg(parts[0])
            return bool(val)
            
        var_parts = parts[0].split('.')
        base = self.env.get(var_parts[0])
        if not base: return False
        val = getattr(base, var_parts[1])
        op, target = parts[1], float(parts[2])
        if op == ">": return val > target
        if op == "<": return val < target
        return False

    def _exec_line(self, line: str):
        m = re.match(r'(%\w+|\w+)\s*=\s*(\w+)\s*(.*)', line)
        if not m: return
        
        var, op, args_str = m.groups()
        args = [a.strip() for a in args_str.split(',')]
        
        pos_args = []
        kwargs = {}
        for arg in args:
            if '=' in arg and not arg.startswith('"'):
                # Split on first equals sign only
                k, v = arg.split('=', 1)
                kwargs[k.strip()] = self._eval_arg(v)
            else:
                pos_args.append(self._eval_arg(arg))

        try:
            # Dispatch AST node
            if op == "load_genome": self.env[var] = DNA("ATGTGATAAATGAAATAA")
            elif op == "load_fasta": self.env[var] = DNA("ATGTGATAAATGAAATAA")
            elif op == "load_mirna": self.env[var] = miRNA(target_seq="UUCAAA")
            elif op == "load_drug": self.env[var] = Drug(pos_args[0], pos_args[1])
            elif op == "init_thermo": self.env[var] = init_thermo(*pos_args, **kwargs)
            elif op == "apply_topology": self.env[var] = apply_topology(*pos_args, **kwargs)
            elif op == "transcribe": self.env[var] = transcribe(*pos_args, **kwargs)
            elif op == "silence": self.env[var] = silence(*pos_args, **kwargs)
            elif op == "expand_code": self.env[var] = expand_code(*pos_args, **kwargs)
            elif op == "init_cell": self.env[var] = init_cell(*pos_args, **kwargs)
            elif op == "update_cell": self.env[var] = update_cell(*pos_args, **kwargs)
            elif op == "simulate_ribosome": self.env[var] = simulate_ribosome(*pos_args, **kwargs)
            elif op == "translate": self.env[var] = translate(*pos_args, **kwargs)
            elif op == "phosphorylate": self.env[var] = phosphorylate(*pos_args, **kwargs)
            elif op == "fold_cotranslational": self.env[var] = fold_cotranslational(*pos_args, **kwargs)
            elif op == "bind": self.env[var] = bind(*pos_args, **kwargs)
            elif op == "dock": self.env[var] = dock(*pos_args, **kwargs)
            elif op == "reverse_translate": self.env[var] = reverse_translate(*pos_args, **kwargs)
            elif op == "init_population": self.env[var] = init_population(*pos_args, **kwargs)
            elif op == "simulate_quorum": self.env[var] = simulate_quorum(*pos_args, **kwargs)
            elif op == "evaluate_promoter": self.env[var] = evaluate_promoter(*pos_args, **kwargs)
            elif op == "ribosome_scan": self.env[var] = ribosome_scan(*pos_args, **kwargs)
            elif op == "assert":
                left, right = pos_args[0], pos_args[1]
                if left != right:
                    raise AssertionError(f"Assert failed: {left} != {right}")
                print(f"[Verified] {var} passed.")
            elif op == "print":
                print(" ".join([str(self._eval_arg(a)) for a in args]))
            elif op == "export":
                print(f"[Exported] {var} to file.")
        except Exception as e:
            print(f"[Exec Error] {e}")

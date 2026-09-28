# shell_es.py
class Fact:
    def __init__(self, predicate, value=True):
        self.predicate = predicate
        self.value = value

    def __repr__(self):
        return f"{self.predicate}={self.value}"

    def __eq__(self, other):
        return isinstance(other, Fact) and self.predicate == other.predicate and self.value == other.value

    def __hash__(self):
        return hash((self.predicate, self.value))


class Rule:
    def __init__(self, conditions, conclusion, name=None):
        self.conditions = conditions
        self.conclusion = conclusion
        self.name = name or f"R{id(self)}"

    def __repr__(self):
        conds = " E ".join(str(c) for c in self.conditions)
        return f"SE {conds} ENTÃO {self.conclusion}"


class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def remove_fact(self, fact):
        self.facts.discard(fact)

    def remove_rule(self, rule):
        if rule in self.rules:
            self.rules.remove(rule)


class InferenceEngine:
    def __init__(self, kb):
        self.kb = kb
        self.trace = []

    def forward_chain(self, goal=None):
        facts = set(self.kb.facts)
        changed = True
        while changed:
            changed = False
            for rule in self.kb.rules:
                if all(cond in facts for cond in rule.conditions):
                    if rule.conclusion not in facts:
                        facts.add(rule.conclusion)
                        self.trace.append(f"Forward: {rule} (novo fato {rule.conclusion})")
                        changed = True
                        if goal and rule.conclusion == goal:
                            return True, facts
        return (goal in facts if goal else True), facts

    def backward_chain(self, goal, visited=None):
        if visited is None:
            visited = set()
        if goal in self.kb.facts:
            self.trace.append(f"Backward: {goal} já é fato.")
            return True
        if goal in visited:
            return False
        visited.add(goal)
        for rule in self.kb.rules:
            if rule.conclusion == goal:
                if all(self.backward_chain(c, visited) for c in rule.conditions):
                    self.trace.append(f"Backward: {rule}")
                    return True
        return False

    def mixed_chain(self, goal):
        ok, _ = self.forward_chain(goal)
        if ok:
            return True
        return self.backward_chain(goal)


class Explanation:
    def __init__(self, engine):
        self.engine = engine

    def why(self, goal):
        return [t for t in self.engine.trace if str(goal) in t]

    def how(self, goal):
        return [t for t in self.engine.trace if "=>" in t or "ENTÃO" in t]

    def trace(self):
        return self.engine.trace


class Interface:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)
        self.expl = Explanation(self.engine)

    def run(self):
        print("Shell de Sistema Especialista. Comandos: add_fact, add_rule, forward, backward, mixed, why, how, trace, list, exit")

        while True:
            cmd = input("> ").strip().split()

            if not cmd:
                continue

            op = cmd[0].lower()

            if op == "exit":
                break

            elif op == "add_fact":
                self.kb.add_fact(Fact(cmd[1]))
                print("Fato adicionado.")

            elif op == "add_rule":
                conds = [Fact(c) for c in cmd[1:-1]]
                concl = Fact(cmd[-1])
                self.kb.add_rule(Rule(conds, concl))
                print("Regra adicionada.")

            elif op == "forward":
                goal = Fact(cmd[1]) if len(cmd) > 1 else None
                ok, facts = self.engine.forward_chain(goal)
                print("Sucesso:", ok)
                print("Fatos:", facts)

            elif op == "backward":
                goal = Fact(cmd[1])
                ok = self.engine.backward_chain(goal)
                print("Sucesso:", ok)

            elif op == "mixed":
                goal = Fact(cmd[1])
                ok = self.engine.mixed_chain(goal)
                print("Sucesso:", ok)

            elif op == "why":
                goal = Fact(cmd[1])
                print("\n".join(self.expl.why(goal)) or "Sem explicação.")

            elif op == "how":
                goal = Fact(cmd[1])
                print("\n".join(self.expl.how(goal)) or "Sem explicação.")

            elif op == "trace":
                print("\n".join(self.expl.trace()) or "Trilha vazia.")

            elif op == "list":
                print("Fatos:", self.kb.facts)
                print("Regras:")
                for r in self.kb.rules:
                    print(" ", r)

            else:
                print("Comando inválido.")


if __name__ == "__main__":
    Interface().run()

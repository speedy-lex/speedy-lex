with open("template.md") as r:
    template = r.read()

with open("README.md", "w") as w:
    w.write(template)

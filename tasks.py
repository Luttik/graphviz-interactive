from invoke import task


def simple_task(name: str, commands: str) -> task:
    def caller(c):  # noqa
        c.run(f"echo running {name}")
        c.run(commands)

    return task(caller, name=name)


format = simple_task(name="format", commands="inv black isort")
black = simple_task(name="black", commands="black -q .")
isort = simple_task(name="isort", commands="isort .")

flake8 = simple_task(name="lint", commands="flake8 .")

test = simple_task(name="test", commands="pytest --cov")

check = simple_task(name="check", commands="inv format flake8 test")

publish = simple_task(name="publish", commands="poetry publish --build")
